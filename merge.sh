#!/bin/bash

# Prompt user for the source branch
read -p "Enter the name of the source branch to pull new files from: " sourceBranch

# Get the current branch
currentBranch=$(git rev-parse --abbrev-ref HEAD)

echo "Checking for new files in branch '$sourceBranch' compared to '$currentBranch'..."

# Get added and modified files in the source branch (ignores deletions)
addedFiles=$(git diff --diff-filter=AM --name-only "$currentBranch" "$sourceBranch")

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
    git checkout "$sourceBranch" -- "$file"
done

# Stage and commit the new files
echo "$addedFiles" | xargs git add
git commit -m "Add new files from $sourceBranch"

echo "Successfully added and committed new files from '$sourceBranch' to '$currentBranch'."
