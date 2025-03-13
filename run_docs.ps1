# PowerShell script to launch both Docusaurus and Documentation Buddy applications

# Function to check if a directory exists
function Test-DirectoryExists {
    param (
        [string]$Path
    )
    
    if (-not (Test-Path -Path $Path -PathType Container)) {
        Write-Host "Error: Directory '$Path' does not exist." -ForegroundColor Red
        return $false
    }
    
    return $true
}

# Clear the console for a clean start
Clear-Host
Write-Host "Starting Soldered Documentation Tools..." -ForegroundColor Cyan

# Check if the required directories exist
$docusaurusDir = Join-Path -Path $PSScriptRoot -ChildPath "soldered-documentation"
$buddyDir = Join-Path -Path $PSScriptRoot -ChildPath "documentation-buddy"

if (-not (Test-DirectoryExists -Path $docusaurusDir)) {
    Write-Host "Exiting script." -ForegroundColor Red
    exit 1
}

if (-not (Test-DirectoryExists -Path $buddyDir)) {
    Write-Host "Exiting script." -ForegroundColor Red
    exit 1
}

# Launch Docusaurus in a new PowerShell window
Write-Host "Starting Docusaurus in soldered-documentation directory..." -ForegroundColor Green
Start-Process powershell -ArgumentList "-NoExit", "-Command", "Set-Location -Path '$docusaurusDir'; npm start"

# Brief pause to allow first window to initialize
Start-Sleep -Seconds 2

# Launch Documentation Buddy in another new PowerShell window
Write-Host "Starting Documentation Buddy in documentation-buddy directory..." -ForegroundColor Green
Start-Process powershell -ArgumentList "-NoExit", "-Command", "Set-Location -Path '$buddyDir'; python documentation_buddy.py"

# Open the browser to Documentation Buddy after a short delay (default port is 5000)
Start-Sleep -Seconds 5  # Give Documentation Buddy a short time to initialize
Write-Host "Opening Documentation Buddy in your default browser..." -ForegroundColor Green
Start-Process "http://localhost:5000"

Write-Host "Both applications have been launched in separate windows." -ForegroundColor Cyan
Write-Host "- Docusaurus is running in the first window" -ForegroundColor Yellow
Write-Host "- Documentation Buddy is running in the second window" -ForegroundColor Yellow
Write-Host "Keep these windows open while you work. Close them when you're finished." -ForegroundColor Yellow