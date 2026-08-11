# Checks whether this computer is set up to build and deploy the docs.
# Run from the repo root:   .\check_env.ps1
# Nothing here changes the server. It only reads and tests.

Clear-Host
Write-Host "Soldered Docs - Deploy Environment Check" -ForegroundColor Cyan
Write-Host ""

$problems = @()

function Report-Ok {
    param([string]$Message)
    Write-Host "  [ OK ]  $Message" -ForegroundColor Green
}

function Report-Fail {
    param([string]$Message, [string]$Fix)
    Write-Host "  [FAIL]  $Message" -ForegroundColor Red
    if ($Fix) { Write-Host "          $Fix" -ForegroundColor Yellow }
    $script:problems += $Message
}

# ---------------------------------------------------------------
# 1. Required tools
# ---------------------------------------------------------------
Write-Host "Checking required tools..." -ForegroundColor Cyan

foreach ($tool in @("ssh", "npm", "git")) {
    if (Get-Command $tool -ErrorAction SilentlyContinue) {
        Report-Ok "$tool is installed"
    } else {
        $fix = switch ($tool) {
            "ssh" { "Install OpenSSH: Settings > Apps > Optional Features > OpenSSH Client" }
            "npm" { "Install Node.js from https://nodejs.org" }
            "git" { "Install Git for Windows from https://git-scm.com/download/win" }
        }
        Report-Fail "$tool is NOT installed" $fix
    }
}

# deploy.sh needs a bash shell. Git Bash provides it.
$gitBash = @(
    "C:\Program Files\Git\bin\bash.exe",
    "C:\Program Files (x86)\Git\bin\bash.exe"
) | Where-Object { Test-Path $_ } | Select-Object -First 1

if ($gitBash) {
    Report-Ok "Git Bash found (needed to run deploy.sh)"
} else {
    Report-Fail "Git Bash not found - deploy.sh cannot run without it" `
                "Install Git for Windows from https://git-scm.com/download/win"
}

# ---------------------------------------------------------------
# 2. deploy.env
# ---------------------------------------------------------------
Write-Host ""
Write-Host "Checking deploy.env..." -ForegroundColor Cyan

$envFile = Join-Path -Path $PSScriptRoot -ChildPath "deploy.env"
$config = @{}

if (-not (Test-Path $envFile)) {
    Report-Fail "deploy.env not found" `
                "Copy deploy.env.example to deploy.env and fill it in."
} else {
    Report-Ok "deploy.env exists"

    # Parse simple KEY=VALUE lines, skipping comments and blanks.
    Get-Content $envFile | ForEach-Object {
        $line = $_.Trim()
        if ($line -and -not $line.StartsWith("#") -and $line.Contains("=")) {
            $parts = $line.Split("=", 2)
            $config[$parts[0].Trim()] = $parts[1].Trim()
        }
    }

    foreach ($key in @("REMOTE_HOST", "REMOTE_USER", "REMOTE_PATH", "SSH_KEY")) {
        if ($config.ContainsKey($key) -and $config[$key]) {
            Report-Ok "$key is set"
        } else {
            Report-Fail "$key is missing or empty in deploy.env" "Ask whoever administers the docs server for the correct value."
        }
    }

    if ($config["REMOTE_USER"] -eq "root") {
        Write-Host "  [WARN]  REMOTE_USER is 'root' - it should be the 'deploy' account." -ForegroundColor Yellow
    }
}

# ---------------------------------------------------------------
# 3. SSH key
# ---------------------------------------------------------------
Write-Host ""
Write-Host "Checking SSH key..." -ForegroundColor Cyan

$keyPath = $null
if ($config.ContainsKey("SSH_KEY") -and $config["SSH_KEY"]) {
    # deploy.env uses bash-style $HOME; translate it for Windows.
    $keyPath = $config["SSH_KEY"] -replace '\$HOME', $HOME -replace '~', $HOME
    $keyPath = $keyPath -replace '/', '\'
}

if (-not $keyPath) {
    Report-Fail "No SSH_KEY path to check" "Fix deploy.env first, then re-run this script."
} elseif (-not (Test-Path $keyPath)) {
    Report-Fail "Private key not found at $keyPath" `
                "Generate one with:  ssh-keygen -t ed25519 -C ""your.name@soldered.com"""
} else {
    Report-Ok "Private key found at $keyPath"

    if (Test-Path "$keyPath.pub") {
        Report-Ok "Public key found at $keyPath.pub"
        Write-Host ""
        Write-Host "  Your public key (send THIS to the server admin, never the other file):" -ForegroundColor Cyan
        Write-Host "  $(Get-Content "$keyPath.pub")" -ForegroundColor White
    } else {
        Report-Fail "Public key not found at $keyPath.pub" `
                    "Regenerate it with:  ssh-keygen -y -f ""$keyPath"" > ""$keyPath.pub"""
    }
}

# ---------------------------------------------------------------
# 4. Live connection test
# ---------------------------------------------------------------
Write-Host ""
Write-Host "Testing connection to the server..." -ForegroundColor Cyan

if ($problems.Count -gt 0) {
    Write-Host "  [SKIP]  Fix the problems above first." -ForegroundColor Yellow
} else {
    $target = "$($config['REMOTE_USER'])@$($config['REMOTE_HOST'])"

    # BatchMode=yes makes ssh fail instead of prompting for a password,
    # so an unauthorized key gives a clean failure rather than hanging.
    $sshArgs = @(
        "-i", $keyPath,
        "-o", "BatchMode=yes",
        "-o", "StrictHostKeyChecking=accept-new",
        "-o", "ConnectTimeout=10",
        $target,
        "test -w '$($config['REMOTE_PATH'])' && echo DEPLOY_OK"
    )

    $result = & ssh @sshArgs 2>&1
    $sshExit = $LASTEXITCODE

    if ($sshExit -eq 0 -and $result -match "DEPLOY_OK") {
        Report-Ok "Connected as $target"
        Report-Ok "You can write to $($config['REMOTE_PATH'])"
    } elseif ($sshExit -eq 0) {
        Report-Fail "Connected, but cannot write to $($config['REMOTE_PATH'])" `
                    "Your key works. Ask the server admin to grant write access to the docs folder."
    } else {
        Report-Fail "Could not connect to $target" `
                    "Send the server admin your public key (shown above) so it can be authorized."
        Write-Host "          ssh said: $result" -ForegroundColor DarkGray
    }
}

# ---------------------------------------------------------------
# Summary
# ---------------------------------------------------------------
Write-Host ""
if ($problems.Count -eq 0) {
    Write-Host "All checks passed. You are ready to deploy." -ForegroundColor Green
    Write-Host "Deploy by running this in Git Bash:  ./deploy.sh" -ForegroundColor Cyan
} else {
    Write-Host "$($problems.Count) problem(s) found. Fix them, then run this script again." -ForegroundColor Red
}
Write-Host ""
