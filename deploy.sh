#!/bin/bash
# Builds the docs and deploys them to the server. Git Bash / POSIX version of deploy.ps1.
# Run from the repo root:   ./deploy.sh
#
#   ./deploy.sh -n            show what would be uploaded and deleted, change nothing
#   ./deploy.sh --skip-build  upload the existing build folder without rebuilding
#   ./deploy.sh --force       bypass the checkout and mass-deletion guards
#
# Run check_env.ps1 first if you have never deployed from this machine.

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DOCUSAURUS_DIR="$SCRIPT_DIR/soldered-documentation"
ENV_FILE="$SCRIPT_DIR/deploy.env"

DRY_RUN=0
SKIP_BUILD=0
FORCE=0
# Above this many server-side deletions the deploy stops and asks to be looked at.
# A normal deploy deletes only the previous build's hashed assets, a few dozen files.
# Hundreds means the build is partial or aimed at the wrong directory, and --delete
# would take real pages off the live site.
MAX_DELETES=500
# A build with fewer pages than this is not a real build of this site.
MIN_PAGES=100

usage() {
    echo "Usage: ./deploy.sh [options]"
    echo ""
    echo "  -n, --dry-run       list what would change on the server, change nothing"
    echo "      --skip-build    deploy the existing build folder without rebuilding"
    echo "      --force         bypass the stale-checkout and mass-deletion guards"
    echo "      --max-deletes N raise the mass-deletion limit for this run (default 500)"
    echo "  -h, --help          show this help"
}

while [ $# -gt 0 ]; do
    case "$1" in
        -n|--dry-run)   DRY_RUN=1 ;;
        --skip-build)   SKIP_BUILD=1 ;;
        --force)        FORCE=1 ;;
        --max-deletes)
            shift
            MAX_DELETES="$1"
            if ! echo "$MAX_DELETES" | grep -qE '^[0-9]+$'; then
                echo "Error: --max-deletes needs a number."
                exit 1
            fi
            ;;
        -h|--help)      usage; exit 0 ;;
        *)
            echo "Error: unknown option '$1'."
            usage
            exit 1
            ;;
    esac
    shift
done

# ---------------------------------------------------------------
# 1. Config
# ---------------------------------------------------------------
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

# REMOTE_PATH is handed to rsync with --delete, so a stray value here empties the
# wrong directory. Refuse the paths that would do the most damage.
case "$REMOTE_PATH" in
    ""|"/"|"/var"|"/var/www"|"/home"|"/root"|"/etc"|"/usr")
        echo "Error: REMOTE_PATH is '$REMOTE_PATH', too broad to sync with --delete."
        echo "Set it to the site's html directory in deploy.env."
        exit 1
        ;;
esac

# ---------------------------------------------------------------
# 2. Checkout guard
# ---------------------------------------------------------------
# The failure this prevents: on 2026-09-08 a deploy ran from a checkout made
# before the Algolia search commit was merged. The build was valid and the upload
# succeeded, so nothing looked wrong, but it replaced the live site with a
# searchless one. A deploy is only as current as the tree it is built from, and
# nothing else in this script notices.
CHECKOUT_PROBLEMS=""

if ! command -v git >/dev/null 2>&1; then
    echo "Warning: git not found; cannot check whether this checkout is current."
elif [ ! -d "$SCRIPT_DIR/.git" ]; then
    echo "Warning: not a git checkout; cannot check whether it is current."
else
    if [ -n "$(cd "$SCRIPT_DIR" && git status --porcelain)" ]; then
        CHECKOUT_PROBLEMS="$CHECKOUT_PROBLEMS  - uncommitted changes, so this deploy matches no commit
"
    fi

    if ! (cd "$SCRIPT_DIR" && git fetch --quiet origin); then
        echo "Warning: could not reach origin. Comparing against the last known origin/master."
    fi

    LOCAL_HEAD=$(cd "$SCRIPT_DIR" && git rev-parse HEAD 2>/dev/null)
    REMOTE_HEAD=$(cd "$SCRIPT_DIR" && git rev-parse origin/master 2>/dev/null)

    if [ -z "$REMOTE_HEAD" ]; then
        echo "Warning: origin/master not found locally; skipping the staleness check."
    elif [ "$LOCAL_HEAD" != "$REMOTE_HEAD" ]; then
        BEHIND=$(cd "$SCRIPT_DIR" && git rev-list --count HEAD..origin/master 2>/dev/null)
        AHEAD=$(cd "$SCRIPT_DIR" && git rev-list --count origin/master..HEAD 2>/dev/null)
        if [ "${BEHIND:-0}" -gt 0 ]; then
            CHECKOUT_PROBLEMS="$CHECKOUT_PROBLEMS  - HEAD is $BEHIND commit(s) behind origin/master, so this build is missing other people's work
"
        fi
        if [ "${AHEAD:-0}" -gt 0 ]; then
            CHECKOUT_PROBLEMS="$CHECKOUT_PROBLEMS  - HEAD is $AHEAD commit(s) ahead of origin/master, so this build contains unpushed work
"
        fi
    fi
fi

if [ -n "$CHECKOUT_PROBLEMS" ]; then
    echo ""
    echo "Checkout is not a clean copy of origin/master:"
    printf '%s' "$CHECKOUT_PROBLEMS"
    if [ "$FORCE" -eq 1 ]; then
        echo "Continuing anyway because --force was given."
        echo ""
    else
        echo "Fix with:  git fetch origin && git merge --ff-only origin/master"
        echo "Or pass --force if you mean to deploy exactly this tree."
        exit 1
    fi
fi

# ---------------------------------------------------------------
# 3. Build
# ---------------------------------------------------------------
cd "$DOCUSAURUS_DIR" || exit 1

if [ "$SKIP_BUILD" -eq 1 ]; then
    echo "Skipping build (--skip-build)."
else
    echo "Building Docusaurus..."
    npm run build
    if [ $? -ne 0 ]; then
        echo "Build failed. Aborting deploy."
        exit 1
    fi
fi

# Guard against pushing an empty or broken build, since rsync --delete would then
# wipe the live site. index.html alone is not enough: a build that died partway
# through still writes one, so check the page count and the asset folder every
# page loads its bundle from.
if [ ! -f "$DOCUSAURUS_DIR/build/index.html" ]; then
    echo "Build folder has no index.html. Aborting deploy."
    exit 1
fi

if [ ! -d "$DOCUSAURUS_DIR/build/assets/js" ]; then
    echo "Build folder has no assets/js. Aborting deploy."
    exit 1
fi

PAGE_COUNT=$(find "$DOCUSAURUS_DIR/build" -name 'index.html' | wc -l | tr -d '[:space:]')
if [ "$PAGE_COUNT" -lt "$MIN_PAGES" ]; then
    echo "Error: build has only $PAGE_COUNT pages, expected at least $MIN_PAGES."
    echo "That is a partial build, and --delete would strip the missing pages off the live site."
    exit 1
fi
echo "Build looks complete: $PAGE_COUNT pages."

# ---------------------------------------------------------------
# 4. How to reach the server
# ---------------------------------------------------------------
# Plain ssh everywhere except Git Bash on Windows, where two separate filesystem
# views get in the way and cost an afternoon if you meet them cold:
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
            # The Cygwin ssh has no HOME of its own, so known_hosts must be named
            # explicitly. Without this it writes to /known_hosts, fails, and the
            # server's key is re-accepted unverified on every deploy. Create the
            # directory so the first accepted key is actually recorded.
            mkdir -p "$HOME/.ssh"
            RSH="/cygdrive${CYG_SSH} -i /cygdrive${SSH_KEY}"
            RSH="$RSH -o UserKnownHostsFile=/cygdrive${HOME}/.ssh/known_hosts"
            RSH="$RSH -o StrictHostKeyChecking=accept-new"
        else
            echo "Warning: Cygwin ssh not found next to rsync; falling back to ssh on PATH."
            echo "If rsync fails with 'dup() in/out/err failed', that is why."
        fi
        ;;
esac

# ---------------------------------------------------------------
# 5. Deploy
# ---------------------------------------------------------------
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
# The source is relative on purpose; see note 1 above.
TARGET="$REMOTE_USER@$REMOTE_HOST:$REMOTE_PATH/"
RSYNC_OPTS=(-rltvz --delete --omit-dir-times --no-perms --no-owner --no-group
    --chmod=D2775,F664 -e "$RSH")

echo ""
if [ "$DRY_RUN" -eq 1 ]; then
    echo "DRY RUN - nothing on the server will change."
fi
echo "Deploying to $REMOTE_HOST:$REMOTE_PATH as $REMOTE_USER..."

if [ "$DRY_RUN" -eq 1 ]; then
    rsync -n "${RSYNC_OPTS[@]}" build/ "$TARGET"
    if [ $? -eq 0 ]; then
        echo ""
        echo "Dry run complete. Nothing was changed on the server."
        exit 0
    fi
    echo "Dry run failed."
    exit 1
fi

# Count the deletions before committing to them. This pass changes nothing; it
# exists so a partial build or a wrong REMOTE_PATH is caught while the live site
# is still intact, rather than after --delete has already run.
echo "Checking what would be deleted..."
PREVIEW=$(rsync -n "${RSYNC_OPTS[@]}" build/ "$TARGET")
if [ $? -ne 0 ]; then
    echo "Error: could not preview the deploy. Nothing was changed on the server."
    exit 1
fi

DELETE_COUNT=$(printf '%s\n' "$PREVIEW" | grep -c '^deleting ')
echo "$DELETE_COUNT file(s) would be deleted on the server."

if [ "$DELETE_COUNT" -gt "$MAX_DELETES" ]; then
    echo ""
    echo "Error: that is more than the limit of $MAX_DELETES."
    echo "A normal deploy deletes only the last build's hashed assets. Check the build"
    echo "and REMOTE_PATH, then rerun with --dry-run to see the full list."
    if [ "$FORCE" -eq 0 ]; then
        echo "Pass --force, or --max-deletes N, if the deletions are expected."
        exit 1
    fi
    echo "Continuing anyway because --force was given."
fi

rsync "${RSYNC_OPTS[@]}" build/ "$TARGET"

if [ $? -eq 0 ]; then
    echo "Deploy complete."
else
    echo "Deploy failed."
    exit 1
fi
