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

# Sync build folder to server, deleting files on remote that no longer exist locally.
#
# Do NOT use -a here. It implies -p -o -g -t, and the build folder on Windows reports
# mode 700 for every file, so -a pushes that onto the server. The live site serves via
# POSIX ACLs (user:nginx:r-x per file), and since the group bits are the ACL mask, mode
# 700 sets mask::--- and makes every ACL entry ineffective. nginx can then read nothing
# and the whole site 403s, homepage included. This took docs.soldered.com down on
# 2026-08-26. Set the modes explicitly instead: 2775 on directories matches the site
# root and keeps the setgid bit, so new files stay in the docs group.
#
# -t is kept so file times transfer and later deploys stay incremental; only
# --omit-dir-times is dropped, because the directories are root-owned. Without it rsync emits about
# 1500 'failed to set times' errors and exits 23, which masks real failures.
rsync -rltvz --delete --omit-dir-times --no-perms --no-owner --no-group \
    --chmod=D2775,F664 \
    -e "ssh -i $SSH_KEY" \
    "$DOCUSAURUS_DIR/build/" \
    "$REMOTE_USER@$REMOTE_HOST:$REMOTE_PATH/"

if [ $? -eq 0 ]; then
    echo "Deploy complete."
else
    echo "Deploy failed."
    exit 1
fi
