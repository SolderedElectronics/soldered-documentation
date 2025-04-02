# Prompt user for the source branch
$sourceBranch = Read-Host "Enter the name of the source branch to pull new files from"

# Get the current branch
$currentBranch = git rev-parse --abbrev-ref HEAD

Write-Output "Checking for new files in branch '$sourceBranch' compared to '$currentBranch'..."

# Get only newly added files in the source branch (ignores modifications and deletions)
$addedFiles = git diff --diff-filter=A --name-only $currentBranch $sourceBranch

if (-not $addedFiles -or $addedFiles.Count -eq 0) {
    Write-Output "No new files to add from branch '$sourceBranch'."
    exit 0
}

Write-Output "Found $($addedFiles.Count) new file(s). Checking them out..."

# Print the list of files being checked out
$addedFiles | ForEach-Object { Write-Output " - $_" }

# For each file, ensure the folder exists and then check it out from the source branch
foreach ($file in $addedFiles) {
    $dir = Split-Path $file -Parent
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir -Force | Out-Null
    }

    git checkout $sourceBranch -- $file
}

# Stage and commit the new files
git add $addedFiles
git commit -m "Add new files from $sourceBranch without modifying existing files"

Write-Output "✅ Successfully added and committed new files from '$sourceBranch' to '$currentBranch'."
