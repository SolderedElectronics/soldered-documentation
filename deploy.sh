#!/bin/bash

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DOCUSAURUS_DIR="$SCRIPT_DIR/soldered-documentation"
SSH_KEY="$HOME/.ssh/soldered_droplet_rsoric_pk_openssh_format"
REMOTE_USER="root"
REMOTE_HOST="134.209.253.96"
REMOTE_PATH="/var/www/docs.soldered.com/html"

# Build
echo "Building Docusaurus..."
cd "$DOCUSAURUS_DIR" && npm run build

if [ $? -ne 0 ]; then
    echo "Build failed. Aborting deploy."
    exit 1
fi

echo "Deploying to $REMOTE_HOST:$REMOTE_PATH..."

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
