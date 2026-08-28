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

# How to reach the server. Plain ssh everywhere except Git Bash on Windows, where
# two separate filesystem views get in the way and cost an afternoon if you meet
# them cold:
#
#  1. Git Bash rewrites POSIX paths into C:/... before handing them to a native
#     exe. rsync then reads the drive letter as a hostname and dies with "The
#     source and destination cannot both be remote". MSYS_NO_PATHCONV=1 stops the
#     rewriting, and the source path below is relative so there is no drive letter
#     left to rewrite.
#  2. The rsync on PATH here is a Cygwin build. It cannot exec the MSYS ssh at
#     /usr/bin/ssh ("dup() in/out/err failed"), and it cannot see /c/... paths at
#     all, so point it at the ssh.exe that ships beside it and hand that ssh both
#     the key and known_hosts in /cygdrive form.
RSH="ssh -i $SSH_KEY"
case "$(uname -s)" in
    MINGW*|MSYS*|CYGWIN*)
        export MSYS_NO_PATHCONV=1
        CYG_SSH="/c/ProgramData/chocolatey/lib/rsync/tools/bin/ssh.exe"
        if [ -f "$CYG_SSH" ]; then
            RSH="/cygdrive${CYG_SSH} -i /cygdrive${SSH_KEY}"
            RSH="$RSH -o UserKnownHostsFile=/cygdrive${HOME}/.ssh/known_hosts"
            RSH="$RSH -o StrictHostKeyChecking=accept-new"
        else
            echo "Warning: Cygwin ssh not found next to rsync; falling back to ssh on PATH."
            echo "If rsync fails with 'dup() in/out/err failed', that is why."
        fi
        ;;
esac

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
# The source is relative on purpose; see note 1 above. We are already in
# $DOCUSAURUS_DIR from the build step, but cd again so this does not rely on it.
cd "$DOCUSAURUS_DIR" || exit 1

rsync -rltvz --delete --omit-dir-times --no-perms --no-owner --no-group \
    --chmod=D2775,F664 \
    -e "$RSH" \
    build/ \
    "$REMOTE_USER@$REMOTE_HOST:$REMOTE_PATH/"

if [ $? -eq 0 ]; then
    echo "Deploy complete."
else
    echo "Deploy failed."
    exit 1
fi
