# Builds the docs and deploys them to the server. Windows / PowerShell version of deploy.sh.
# Run from the repo root:   .\deploy.ps1
#
#   .\deploy.ps1 -DryRun      show what would be uploaded and deleted, change nothing
#   .\deploy.ps1 -SkipBuild   upload the existing build folder without rebuilding
#   .\deploy.ps1 -Force       bypass the stale-checkout and mass-deletion guards
#
# Run .\check_env.ps1 first if you have never deployed from this machine.

[CmdletBinding()]
param(
    [switch]$DryRun,
    [switch]$SkipBuild,
    [switch]$Force,
    # Above this many server-side deletions the deploy stops and asks to be looked
    # at. A normal deploy deletes only the previous build's hashed assets, a few
    # dozen files. Hundreds means the build is partial or aimed at the wrong
    # directory, and --delete would take real pages off the live site.
    [int]$MaxDeletes = 500
)

# A build with fewer pages than this is not a real build of this site.
$minPages = 100

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

# REMOTE_PATH is handed to rsync with --delete, so a stray value here empties the
# wrong directory. Refuse the paths that would do the most damage.
$forbiddenPaths = @("/", "/var", "/var/www", "/home", "/root", "/etc", "/usr")
if ($forbiddenPaths -contains $config["REMOTE_PATH"].TrimEnd("/")) {
    Fail "REMOTE_PATH is '$($config['REMOTE_PATH'])', too broad to sync with --delete." `
         "Set it to the site's html directory in deploy.env."
}

# ---------------------------------------------------------------
# 2. Checkout guard
# ---------------------------------------------------------------
# The failure this prevents: on 2026-09-08 a deploy ran from a checkout made
# before the Algolia search commit was merged. The build was valid and the upload
# succeeded, so nothing looked wrong, but it replaced the live site with a
# searchless one. A deploy is only as current as the tree it is built from, and
# nothing else in this script notices.
$checkoutProblems = @()

if (-not (Get-Command git -ErrorAction SilentlyContinue)) {
    Write-Host "Warning: git not found; cannot check whether this checkout is current." -ForegroundColor Yellow
} elseif (-not (Test-Path (Join-Path $PSScriptRoot ".git"))) {
    Write-Host "Warning: not a git checkout; cannot check whether it is current." -ForegroundColor Yellow
} else {
    Push-Location $PSScriptRoot
    try {
        # git writes progress to stderr, which $ErrorActionPreference = "Stop" would
        # turn into a terminating error, so each call is wrapped rather than trusted.
        $dirty = & git status --porcelain
        if ($LASTEXITCODE -eq 0 -and $dirty) {
            $checkoutProblems += "uncommitted changes, so this deploy matches no commit"
        }

        & git fetch --quiet origin
        if ($LASTEXITCODE -ne 0) {
            Write-Host "Warning: could not reach origin. Comparing against the last known origin/master." -ForegroundColor Yellow
        }

        # No 2>$null on these: redirecting a native command's stderr in PowerShell 5.1
        # wraps each line in an ErrorRecord, which $ErrorActionPreference = "Stop"
        # then throws on even when git exited 0.
        $localHead = & git rev-parse HEAD
        if ($LASTEXITCODE -ne 0) { $localHead = $null }
        $remoteHead = & git rev-parse origin/master
        if ($LASTEXITCODE -ne 0) { $remoteHead = $null }

        if (-not $remoteHead) {
            Write-Host "Warning: origin/master not found locally; skipping the staleness check." -ForegroundColor Yellow
        } elseif ($localHead -ne $remoteHead) {
            $behind = [int](& git rev-list --count HEAD..origin/master)
            $ahead  = [int](& git rev-list --count origin/master..HEAD)
            if ($behind -gt 0) {
                $checkoutProblems += "HEAD is $behind commit(s) behind origin/master, so this build is missing other people's work"
            }
            if ($ahead -gt 0) {
                $checkoutProblems += "HEAD is $ahead commit(s) ahead of origin/master, so this build contains unpushed work"
            }
        }
    } finally {
        Pop-Location
    }
}

if ($checkoutProblems.Count -gt 0) {
    Write-Host ""
    Write-Host "Checkout is not a clean copy of origin/master:" -ForegroundColor Red
    foreach ($problem in $checkoutProblems) {
        Write-Host "  - $problem" -ForegroundColor Red
    }
    if ($Force) {
        Write-Host "Continuing anyway because -Force was given." -ForegroundColor Yellow
        Write-Host ""
    } else {
        Fail "Refusing to deploy from this checkout." `
             "Fix with:  git fetch origin; git merge --ff-only origin/master    (or pass -Force)"
    }
}

# ---------------------------------------------------------------
# 3. rsync and its ssh
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
# 4. Build
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

# Guard against pushing an empty or broken build, since rsync --delete would then
# wipe the live site. index.html alone is not enough: a build that died partway
# through still writes one, so check the page count and the asset folder every
# page loads its bundle from.
if (-not (Test-Path (Join-Path $docusaurusDir "build\index.html"))) {
    Fail "Build folder has no index.html. Aborting deploy."
}

if (-not (Test-Path (Join-Path $docusaurusDir "build\assets\js"))) {
    Fail "Build folder has no assets\js. Aborting deploy."
}

$pageCount = @(Get-ChildItem -Path (Join-Path $docusaurusDir "build") -Filter "index.html" -Recurse -File -ErrorAction SilentlyContinue).Count
if ($pageCount -lt $minPages) {
    Fail "Build has only $pageCount pages, expected at least $minPages." `
         "That is a partial build, and --delete would strip the missing pages off the live site."
}
Write-Host "Build looks complete: $pageCount pages." -ForegroundColor Green

# ---------------------------------------------------------------
# 5. Deploy
# ---------------------------------------------------------------
$target = "$($config['REMOTE_USER'])@$($config['REMOTE_HOST']):$($config['REMOTE_PATH'])/"
$cygKey = ConvertTo-CygPath $keyPath

# The Cygwin ssh has no HOME of its own, so known_hosts must be named explicitly.
# Without this it writes to /known_hosts, fails, and the server's key is
# re-accepted unverified on every deploy. Create the directory so the first
# accepted key is actually recorded and a later change is noticed.
$sshDir = Join-Path $HOME ".ssh"
if (-not (Test-Path $sshDir)) {
    New-Item -ItemType Directory -Path $sshDir -Force | Out-Null
}
$cygKnownHosts = ConvertTo-CygPath (Join-Path $sshDir "known_hosts")

Write-Host ""
if ($DryRun) {
    Write-Host "DRY RUN - nothing on the server will change." -ForegroundColor Yellow
}
Write-Host "Deploying to $($config['REMOTE_HOST']):$($config['REMOTE_PATH']) as $($config['REMOTE_USER'])..." -ForegroundColor Cyan

# Three server-side facts drive the flags below:
#
#   no -a         Do NOT use -a here, and do not reintroduce it. It implies -p -o -g -t,
#                 and cwRsync reports every file in the build folder as mode 770, so -a
#                 pushes that onto the server. The live site serves via POSIX ACLs
#                 (user:nginx:r-x per file), and since the group bits are the ACL mask,
#                 770 sets mask::--- and makes every ACL entry ineffective. nginx can
#                 then read nothing and the whole site 403s, homepage included. This
#                 took docs.soldered.com down on 2026-08-26. The flags are spelled out
#                 instead, matching deploy.sh: -rltvz plus --no-perms --no-owner
#                 --no-group. --chmod alone did mask the problem while -a was here, but
#                 it left the site one edited flag away from another outage.
#
#   --chmod       Modes are set explicitly rather than preserved. F664 keeps files
#                 world-readable for nginx. D2775 matches the directories already on
#                 the server, so rsync sees no difference and skips chmod on them,
#                 and it keeps the setgid bit so new files stay in the docs group.
#
#   --omit-dir-times  the directories are owned by root, and setting mtime needs
#                 ownership rather than write access, so every one of them would
#                 otherwise report "failed to set times: Operation not permitted".
#                 -t is kept for files, so later deploys stay incremental.
$rsyncArgs = @(
    "-rltvz", "--delete", "--omit-dir-times",
    "--no-perms", "--no-owner", "--no-group",
    "--chmod=D2775,F664",
    "-e", "ssh -i $cygKey -o UserKnownHostsFile=$cygKnownHosts -o StrictHostKeyChecking=accept-new"
)
# relative on purpose: an absolute path reintroduces the "C:" problem
$rsyncTail = @("build/", $target)

# Running from inside the build folder's parent keeps the source argument relative.
Push-Location $docusaurusDir
try {
    if (-not $DryRun) {
        # Count the deletions before committing to them. This pass changes nothing;
        # it exists so a partial build or a wrong REMOTE_PATH is caught while the
        # live site is still intact, rather than after --delete has already run.
        Write-Host "Checking what would be deleted..." -ForegroundColor Cyan
        $preview = & rsync @($rsyncArgs + "-n" + $rsyncTail)
        if ($LASTEXITCODE -ne 0) {
            Fail "Could not preview the deploy. Nothing was changed on the server."
        }

        $deleteCount = @($preview | Where-Object { $_ -like "deleting *" }).Count
        Write-Host "$deleteCount file(s) would be deleted on the server."

        if ($deleteCount -gt $MaxDeletes) {
            Write-Host ""
            Write-Host "That is more than the limit of $MaxDeletes." -ForegroundColor Red
            Write-Host "A normal deploy deletes only the last build's hashed assets. Check the" -ForegroundColor Yellow
            Write-Host "build and REMOTE_PATH, then rerun with -DryRun to see the full list." -ForegroundColor Yellow
            if (-not $Force) {
                Fail "Refusing to delete $deleteCount files." `
                     "Pass -Force, or -MaxDeletes N, if the deletions are expected."
            }
            Write-Host "Continuing anyway because -Force was given." -ForegroundColor Yellow
        }
    }

    if ($DryRun) { $rsyncArgs += "-n" }
    & rsync @($rsyncArgs + $rsyncTail)
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
