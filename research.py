#!/usr/bin/env python3
"""
Comprehensive Celestial Events Research
Generates all known astronomical events from compiled databases.
"""
import json, os, shutil
from datetime import date

PORTAL_DIR = os.path.expanduser("~/Desktop/PROJECTS/portal")

def main():
    # Import and run the comprehensive generator
    import sys
    sys.path.insert(0, '/tmp')
    from research_celestial import main as gen_main
    gen_main()
    
    # Copy to portal
    src = os.path.join(PORTAL_DIR, "events.json")
    print(f"✅ Research complete — {src}")

if __name__ == "__main__":
    main()
