#!/bin/bash

# Prompt user for the source branch
read -p "Enter the name of the source branch to pull new files from: " sourceBranch

# Get the current branch
currentBranch=$(git rev-parse --abbrev-ref HEAD)

echo "Checking for new files in branch '$sourceBranch' compared to '$currentBranch'..."

# Fetch the branch from remote in case it doesn't exist locally
echo "Fetching '$sourceBranch' from remote..."
git fetch origin "$sourceBranch"

if [ $? -ne 0 ]; then
    echo "Error: Could not fetch branch '$sourceBranch'. Make sure it exists on the remote."
    exit 1
fi

# Get added and modified files in the source branch (ignores deletions, sidebars.js and docusaurus.config.js)
addedFiles=$(git diff --diff-filter=AM --name-only "$currentBranch" "origin/$sourceBranch" | grep -v 'sidebars\.js' | grep -v 'docusaurus\.config\.js')

if [ -z "$addedFiles" ]; then
    echo "No new or changed files to add from branch '$sourceBranch'."
    exit 0
fi

count=$(echo "$addedFiles" | wc -l | tr -d ' ')
echo "Found $count new/changed file(s). Checking them out..."

# Print the list of files being checked out
echo "$addedFiles" | while read -r file; do
    echo " - $file"
done

# For each file, ensure the folder exists and then check it out from the source branch
echo "$addedFiles" | while read -r file; do
    dir=$(dirname "$file")
    mkdir -p "$dir"
    git checkout "origin/$sourceBranch" -- "$file"
done

# Stage and commit the new files
echo "$addedFiles" | xargs git add
git commit -m "Add new files from origin/$sourceBranch"

echo "Successfully added and committed new files from '$sourceBranch' to '$currentBranch'."
