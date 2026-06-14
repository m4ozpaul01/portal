#!/bin/bash
# Sunday celestial research — comprehensive multi-source generator
set -e

cd "$HOME/Desktop/PROJECTS/natural events"

# Run the comprehensive event generator (writes directly to portal/events.json)
python3 comprehensive_research.py

# Save a copy to natural events dir
cp "$HOME/Desktop/PROJECTS/portal/events.json" "$HOME/Desktop/PROJECTS/natural events/events.json"

# Commit and push portal changes
cd "$HOME/Desktop/PROJECTS/portal"
git add events.json
git commit -m "Celestial events research — $(date +%Y-%m-%d)" || echo "No new events"
git push origin gh-pages

echo "Celestial research complete — $(date)"
