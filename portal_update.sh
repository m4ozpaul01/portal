#!/bin/bash
# Portal updater — auto-fetches DeepSeek balance, syncs projects, pushes to GitHub
set -e

cd "$HOME/Desktop/PROJECTS/portal"

python3 update_portal.py

if [[ -n $(git status --porcelain) ]]; then
  git add config.json
  git commit -m "Portal auto-update — $(date +%Y-%m-%d\ %H:%M)"
  git push origin gh-pages
  echo "Pushed portal update to GitHub Pages"
else
  echo "No changes to push"
fi
