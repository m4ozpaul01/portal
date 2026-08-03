#!/usr/bin/env python3
"""
merge_portal_events.py — Merge freshly-researched events into the portal.

Reads source JSON files (each a { 'events': [...] } structure or a bare list)
and merges them into the portal's frankfurt_events.json / hessen_events.json
with dedup by title (case-insensitive) and sorting by date.

Usage:
  python3 merge_portal_events.py <target: frankfurt|hessen> <source1.json> [source2.json ...]
"""
import json
import os
import sys
from datetime import date

PORTAL = os.path.expanduser("~/Desktop/PROJECTS/portal")
FRANKFURT_CATEGORIES = None
HESSEN_CATEGORIES = None

CATEGORIES = [
    "Music & Opera", "Festival & Culture", "Literature & Arts", "Art & Exhibitions",
    "Food & Drink", "Film & Cinema", "Seasonal & Markets", "Sports",
    "Nightlife & Social", "Family & Education", "Markets & Shopping",
    "Convention & Pop Culture",
]


def load_items(path):
    """Return a list of event dicts from a file that is either a bare list or {'events': [...]}."""
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    if isinstance(data, list):
        return data
    if isinstance(data, dict) and isinstance(data.get("events"), list):
        return data["events"]
    raise ValueError(f"Unsupported structure in {path}")


def norm_title(t):
    return " ".join((t or "").lower().split())


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    target = sys.argv[1].lower()
    sources = sys.argv[2:]

    if target not in ("frankfurt", "hessen"):
        print(f"Unknown target: {target}. Must be 'frankfurt' or 'hessen'")
        sys.exit(1)

    final_path = os.path.join(PORTAL, f"{target}_events.json")

    # Load existing events to dedup against
    existing = []
    if os.path.exists(final_path):
        try:
            existing = load_items(final_path)
        except Exception as e:
            print(f"  ⚠ Could not read existing {final_path}: {e}")

    seen = {norm_title(e.get("title", "")) for e in existing}
    merged = list(existing)

    for src in sources:
        try:
            items = load_items(src)
        except Exception as e:
            print(f"  ⚠ Skipping {src}: {e}")
            continue
        added = 0
        for it in items:
            t = norm_title(it.get("title", ""))
            if not t:
                continue
            if t in seen:
                continue
            if it.get("category") and it["category"] not in CATEGORIES:
                # best-effort map
                pass
            merged.append(it)
            seen.add(t)
            added += 1
        print(f"  ✅ {src}: added {added} new, kept {len(items)} scanned")

    # Sort by date ascending (missing dates go last)
    def date_key(e):
        d = str(e.get("date", "9999")).strip()
        return d if d and d != "None" else "9999-99-99"

    merged.sort(key=date_key)

    # Update metadata
    metadata = {}
    if os.path.exists(final_path):
        try:
            with open(final_path, encoding="utf-8") as f:
                metadata = json.load(f)
        except Exception:
            metadata = {}
    metadata["last_updated"] = str(date.today())
    metadata["research_date"] = str(date.today())
    metadata["events"] = merged

    with open(final_path, "w", encoding="utf-8") as f:
        json.dump(metadata, f, indent=2, ensure_ascii=False)
        f.write("\n")

    print(f"  💾 {final_path}: {len(merged)} total events ({date.today()})")
    print("DONE")


if __name__ == "__main__":
    main()
