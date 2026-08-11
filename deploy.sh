#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DOCUSAURUS_DIR="$SCRIPT_DIR/soldered-documentation"
ENV_FILE="$SCRIPT_DIR/deploy.env"

# Load config. Values live in deploy.env, which is gitignored.
if [ ! -f "$ENV_FILE" ]; then
    echo "Error: deploy.env not found."
    echo "Copy deploy.env.example to deploy.env and fill in your values."
    exit 1
fi

set -a
source "$ENV_FILE"
set +a

# Expand $HOME if it was written literally in deploy.env
SSH_KEY=$(eval echo "$SSH_KEY")

for var in REMOTE_HOST REMOTE_USER REMOTE_PATH SSH_KEY; do
    if [ -z "${!var}" ]; then
        echo "Error: $var is not set in deploy.env."
        exit 1
    fi
done

if [ ! -f "$SSH_KEY" ]; then
    echo "Error: SSH key not found at $SSH_KEY"
    echo "Check the SSH_KEY line in deploy.env. Run check_env.ps1 to test your setup."
    exit 1
fi

# Build
echo "Building Docusaurus..."
cd "$DOCUSAURUS_DIR" && npm run build

if [ $? -ne 0 ]; then
    echo "Build failed. Aborting deploy."
    exit 1
fi

# Guard against pushing an empty or broken build, since rsync --delete
# would then wipe the live site.
if [ ! -f "$DOCUSAURUS_DIR/build/index.html" ]; then
    echo "Build folder has no index.html. Aborting deploy."
    exit 1
fi

echo "Deploying to $REMOTE_HOST:$REMOTE_PATH as $REMOTE_USER..."

# Sync build folder to server, deleting files on remote that no longer exist locally
rsync -avz --delete \
    -e "ssh -i $SSH_KEY" \
    "$DOCUSAURUS_DIR/build/" \
    "$REMOTE_USER@$REMOTE_HOST:$REMOTE_PATH/"

if [ $? -eq 0 ]; then
    echo "Deploy complete."
else
    echo "Deploy failed."
    exit 1
fi
