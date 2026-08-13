# Builds the docs and deploys them to the server. Windows / PowerShell version of deploy.sh.
# Run from the repo root:   .\deploy.ps1
#
#   .\deploy.ps1 -DryRun      show what would be uploaded and deleted, change nothing
#   .\deploy.ps1 -SkipBuild   upload the existing build folder without rebuilding
#
# Run .\check_env.ps1 first if you have never deployed from this machine.

[CmdletBinding()]
param(
    [switch]$DryRun,
    [switch]$SkipBuild
)

$ErrorActionPreference = "Stop"

Write-Host ""
Write-Host "Soldered Docs - Deploy" -ForegroundColor Cyan
Write-Host ""

function Fail {
    param([string]$Message, [string]$Fix)
    Write-Host "Error: $Message" -ForegroundColor Red
    if ($Fix) { Write-Host "       $Fix" -ForegroundColor Yellow }
    exit 1
}

# rsync here is cwRsync, a Cygwin build. It reads "C:\..." as "host C, path \...",
# which is what makes a plain Windows path fail with "source and destination cannot
# both be remote". Cygwin paths avoid that.
function ConvertTo-CygPath {
    param([string]$Path)

    $full = [System.IO.Path]::GetFullPath($Path)
    if ($full -match '^([A-Za-z]):[\\/](.*)$') {
        return "/cygdrive/" + $Matches[1].ToLower() + "/" + ($Matches[2] -replace '\\', '/')
    }
    return ($full -replace '\\', '/')
}

$docusaurusDir = Join-Path $PSScriptRoot "soldered-documentation"
$envFile       = Join-Path $PSScriptRoot "deploy.env"

# ---------------------------------------------------------------
# 1. Config
# ---------------------------------------------------------------
if (-not (Test-Path $envFile)) {
    Fail "deploy.env not found." "Copy deploy.env.example to deploy.env and fill in your values."
}

$config = @{}
Get-Content $envFile | ForEach-Object {
    $line = $_.Trim()
    if ($line -and -not $line.StartsWith("#") -and $line.Contains("=")) {
        $parts = $line.Split("=", 2)
        $config[$parts[0].Trim()] = $parts[1].Trim()
    }
}

foreach ($key in @("REMOTE_HOST", "REMOTE_USER", "REMOTE_PATH", "SSH_KEY")) {
    if (-not $config.ContainsKey($key) -or -not $config[$key]) {
        Fail "$key is not set in deploy.env."
    }
}

# deploy.env is shared with deploy.sh, so SSH_KEY is written bash-style.
$keyPath = $config["SSH_KEY"] -replace '\$HOME', $HOME -replace '^~', $HOME
$keyPath = $keyPath -replace '/', '\'

if (-not (Test-Path $keyPath)) {
    Fail "SSH key not found at $keyPath" "Check the SSH_KEY line in deploy.env. Run .\check_env.ps1 to test your setup."
}

# ---------------------------------------------------------------
# 2. rsync and its ssh
# ---------------------------------------------------------------
$rsync = Get-Command rsync -ErrorAction SilentlyContinue
if (-not $rsync) {
    Fail "rsync is not installed." "Install it with:  choco install rsync"
}

# cwRsync cannot drive Windows OpenSSH - the two disagree on file descriptors and
# the transfer dies with "dup() in/out/err failed" or a closed connection. Its own
# bundled ssh.exe is the one that works, so find that specifically. cygwin1.dll
# sitting alongside is what marks a binary as the Cygwin build.
$sshCandidates = @()
$sshCandidates += Join-Path (Split-Path -Parent $rsync.Source) "ssh.exe"
$sshCandidates += Get-ChildItem -Path (Join-Path $env:ProgramData "chocolatey\lib\rsync\tools") `
                                -Filter "ssh.exe" -Recurse -ErrorAction SilentlyContinue |
                  ForEach-Object { $_.FullName }
$sshCandidates += Join-Path $env:ProgramFiles "cwRsync\bin\ssh.exe"
$sshCandidates += Join-Path ${env:ProgramFiles(x86)} "cwRsync\bin\ssh.exe"

$cygSshDir = $null
foreach ($candidate in $sshCandidates) {
    if ($candidate -and (Test-Path $candidate)) {
        $dir = Split-Path -Parent $candidate
        if (Test-Path (Join-Path $dir "cygwin1.dll")) {
            $cygSshDir = $dir
            break
        }
    }
}

if (-not $cygSshDir) {
    Fail "Could not find the Cygwin ssh.exe that ships with cwRsync." `
         "Reinstall rsync with:  choco install rsync --force"
}

# Putting that folder first on PATH means rsync's "ssh" resolves to the Cygwin one,
# and keeps the -e string free of paths that could contain spaces.
$env:PATH = "$cygSshDir;$env:PATH"

# ---------------------------------------------------------------
# 3. Build
# ---------------------------------------------------------------
if ($SkipBuild) {
    Write-Host "Skipping build (-SkipBuild)." -ForegroundColor Yellow
} else {
    Write-Host "Building Docusaurus..." -ForegroundColor Cyan
    Push-Location $docusaurusDir
    try {
        & npm run build
        if ($LASTEXITCODE -ne 0) { Fail "Build failed. Aborting deploy." }
    } finally {
        Pop-Location
    }
}

# Guard against pushing an empty or broken build, since rsync --delete
# would then wipe the live site.
if (-not (Test-Path (Join-Path $docusaurusDir "build\index.html"))) {
    Fail "Build folder has no index.html. Aborting deploy."
}

# ---------------------------------------------------------------
# 4. Deploy
# ---------------------------------------------------------------
$target = "$($config['REMOTE_USER'])@$($config['REMOTE_HOST']):$($config['REMOTE_PATH'])/"
$cygKey = ConvertTo-CygPath $keyPath

Write-Host ""
if ($DryRun) {
    Write-Host "DRY RUN - nothing on the server will change." -ForegroundColor Yellow
}
Write-Host "Deploying to $($config['REMOTE_HOST']):$($config['REMOTE_PATH']) as $($config['REMOTE_USER'])..." -ForegroundColor Cyan

# Two server-side facts drive the flags below:
#
#   --chmod       cwRsync reports every Windows file as mode 770, and -a preserves
#                 that, which overrides the default ACL on the docs folder and leaves
#                 files unreadable by nginx - the whole site 403s. Forcing F664 keeps
#                 them world-readable. D2775 matches the directories already on the
#                 server, so rsync sees no difference and skips chmod on them; without
#                 it, -a would try to chmod root-owned directories and fail.
#
#   --omit-dir-times  the directories are owned by root, and setting mtime needs
#                 ownership rather than write access, so every one of them would
#                 otherwise report "failed to set times: Operation not permitted".
$rsyncArgs = @("-avz", "--delete", "--omit-dir-times", "--chmod=D2775,F664")
if ($DryRun) { $rsyncArgs += "-n" }
$rsyncArgs += @(
    "-e", "ssh -i $cygKey -o StrictHostKeyChecking=accept-new",
    "build/",          # relative on purpose: an absolute path reintroduces the "C:" problem
    $target
)

# Running from inside the build folder's parent keeps the source argument relative.
Push-Location $docusaurusDir
try {
    & rsync @rsyncArgs
    $rsyncExit = $LASTEXITCODE
} finally {
    Pop-Location
}

Write-Host ""
if ($rsyncExit -eq 0) {
    if ($DryRun) {
        Write-Host "Dry run complete. Nothing was changed on the server." -ForegroundColor Green
    } else {
        Write-Host "Deploy complete." -ForegroundColor Green
    }
} else {
    Write-Host "Deploy failed (rsync exit code $rsyncExit)." -ForegroundColor Red
    Write-Host "Run .\check_env.ps1 to test your connection and key." -ForegroundColor Yellow
    exit 1
}
Write-Host ""
