#!/bin/bash
# Portal daily updater — syncs projects, commits, and pushes to GitHub
set -e

PORTAL_DIR="$HOME/Desktop/PROJECTS/portal"
cd "$PORTAL_DIR"

# Parse optional kredyt/tokens from command line
ARGS=""
while [[ $# -gt 0 ]]; do
  case $1 in
    --kredyt) ARGS="$ARGS --kredyt $2"; shift 2 ;;
    --tokens) ARGS="$ARGS --tokens $2"; shift 2 ;;
    *) echo "Unknown: $1"; exit 1 ;;
  esac
done

# Run the Python updater
python3 update_portal.py $ARGS

# Commit and push if there are changes
if [[ -n $(git status --porcelain) ]]; then
  git add config.json
  git commit -m "Portal auto-update — $(date +%Y-%m-%d)"
  git push origin main
  echo "Pushed to GitHub"
else
  echo "No changes to push"
fi
