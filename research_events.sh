#!/bin/bash
# Sunday celestial research — finds upcoming events, updates portal
set -e

cd "$HOME/Desktop/PROJECTS/natural events"
python3 research.py

cd "$HOME/Desktop/PROJECTS/portal"
cp "$HOME/Desktop/PROJECTS/natural events/events.json" events.json
git add events.json
git commit -m "Celestial events research — $(date +%Y-%m-%d)" || echo "No new events"
git push origin gh-pages

echo "Celestial research complete"
