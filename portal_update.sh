#!/bin/bash
# Portal updater — auto-fetches DeepSeek balance, syncs projects + events, pushes to GitHub
set -e

PORTAL_DIR="$HOME/Desktop/PROJECTS/portal"
EVENTS_SRC="$HOME/Desktop/PROJECTS/natural events/events.json"
FRANKFURT_SRC="$HOME/Desktop/PROJECTS/Frankfurt Events/frankfurt_events.json"

cd "$PORTAL_DIR"

# Sync celestial events if available
if [[ -f "$EVENTS_SRC" ]]; then
  cp "$EVENTS_SRC" "$PORTAL_DIR/events.json"
  echo "Synced celestial events"
fi

# Sync Frankfurt events if available
if [[ -f "$FRANKFURT_SRC" ]]; then
  cp "$FRANKFURT_SRC" "$PORTAL_DIR/frankfurt_events.json"
  echo "Synced Frankfurt events"
fi

# Run the config updater
python3 update_portal.py

if [[ -n $(git status --porcelain) ]]; then
  git add config.json events.json frankfurt_events.json
  git commit -m "Portal auto-update — $(date +%Y-%m-%d\ %H:%M)"
  git push origin gh-pages
  echo "Pushed portal update to GitHub Pages"
else
  echo "No changes to push"
fi
