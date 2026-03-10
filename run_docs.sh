#!/bin/bash
# Script to launch both Docusaurus and Documentation Buddy applications

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DOCUSAURUS_DIR="$SCRIPT_DIR/soldered-documentation"
BUDDY_DIR="$SCRIPT_DIR/documentation-buddy"

clear
echo "Starting Soldered Documentation Tools..."

# Check if required directories exist
if [ ! -d "$DOCUSAURUS_DIR" ]; then
    echo "Error: Directory '$DOCUSAURUS_DIR' does not exist."
    exit 1
fi

if [ ! -d "$BUDDY_DIR" ]; then
    echo "Error: Directory '$BUDDY_DIR' does not exist."
    exit 1
fi

# Launch Docusaurus in a new terminal tab/window
echo "Starting Docusaurus in soldered-documentation directory..."
osascript -e "tell application \"Terminal\" to do script \"cd '$DOCUSAURUS_DIR' && npm start\""

# Brief pause to allow first window to initialize
sleep 2

# Launch Documentation Buddy in another new terminal window
echo "Starting Documentation Buddy in documentation-buddy directory..."
osascript -e "tell application \"Terminal\" to do script \"cd '$BUDDY_DIR' && python documentation_buddy.py\""

# Wait for Documentation Buddy to initialize, then open browser
sleep 5
echo "Opening Documentation Buddy in your default browser..."
open "http://localhost:5000"

echo "Both applications have been launched in separate windows."
echo "- Docusaurus is running in the first window"
echo "- Documentation Buddy is running in the second window"
echo "Keep these windows open while you work. Close them when you're finished."
