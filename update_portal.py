#!/usr/bin/env python3
"""
Portal Updater — syncs ~/Desktop/PROJECTS/ folder to portal config.json
Run: python3 update_portal.py [--kredyt N] [--tokens N]

Usage:
  python3 update_portal.py                  # Just sync projects, keep tokens/kredyt
  python3 update_portal.py --kredyt 150      # Update kredyt to 150
  python3 update_portal.py --tokens 42000    # Update tokens to 42000
  python3 update_portal.py --kredyt 150 --tokens 42000  # Update both
"""

import json
import os
import sys
from datetime import date

PORTAL_DIR = os.path.expanduser("~/Desktop/PROJECTS/portal")
PROJECTS_DIR = os.path.expanduser("~/Desktop/PROJECTS")
CONFIG_PATH = os.path.join(PORTAL_DIR, "config.json")

def load_config():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH) as f:
            return json.load(f)
    return {
        "credentials": {
            "username": "m4oz",
            "password_hash": "b34447c239a3831f511359efb8f8f7fd528fc485e824ea4a23d9ff611d7e2245"
        },
        "kredyt": 0,
        "tokens": 0,
        "projects": [],
        "last_updated": str(date.today())
    }

def save_config(config):
    with open(CONFIG_PATH, 'w') as f:
        json.dump(config, f, indent=2)
        f.write('\n')

def sync_projects(config):
    """Add any new project folders as tabs in the portal."""
    existing = {p["name"] for p in config["projects"]}

    for item in sorted(os.listdir(PROJECTS_DIR)):
        item_path = os.path.join(PROJECTS_DIR, item)
        if os.path.isdir(item_path) and not item.startswith('.') and item != 'portal':
            if item not in existing:
                config["projects"].append({
                    "name": item,
                    "status": "active",
                    "description": f"A new project called {item}",
                    "display": "placeholder",
                    "last_updated": str(date.today()),
                    "notes": ""
                })
                print(f"  ➕ Added new project: {item}")
            else:
                # Update last_updated for existing projects
                for p in config["projects"]:
                    if p["name"] == item:
                        p["last_updated"] = str(date.today())
                        break

    config["last_updated"] = str(date.today())
    return config

def main():
    config = load_config()

    # Parse CLI args for kredyt/tokens
    args = sys.argv[1:]
    for i, arg in enumerate(args):
        if arg == '--kredyt' and i + 1 < len(args):
            config["kredyt"] = int(args[i + 1])
            print(f"  💰 Kredyt set to: {config['kredyt']}")
        elif arg == '--tokens' and i + 1 < len(args):
            config["tokens"] = int(args[i + 1])
            print(f"  🔑 Tokens set to: {config['tokens']}")

    config = sync_projects(config)
    save_config(config)
    print(f"  ✅ Portal config updated — {str(date.today())}")

if __name__ == "__main__":
    main()
