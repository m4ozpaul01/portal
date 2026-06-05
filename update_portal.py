#!/usr/bin/env python3
"""
Portal Updater — syncs PROJECTS folder + DeepSeek balance → portal config.json
Auto-fetches DeepSeek API balance and estimates tokens.
Run: python3 update_portal.py [--kredyt N] [--tokens N]

Usage:
  python3 update_portal.py                  # Auto-fetch DeepSeek balance + sync projects
  python3 update_portal.py --kredyt 150     # Override kredyt to 150
  python3 update_portal.py --tokens 42000   # Override tokens to 42000
"""

import json
import os
import sys
from datetime import date

try:
    import urllib.request
    HAS_URLLIB = True
except ImportError:
    HAS_URLLIB = False

PORTAL_DIR = os.path.expanduser("~/Desktop/PROJECTS/portal")
PROJECTS_DIR = os.path.expanduser("~/Desktop/PROJECTS")
CONFIG_PATH = os.path.join(PORTAL_DIR, "config.json")
ENV_PATH = os.path.expanduser("~/.hermes/.env")

# Model pricing estimates (per million tokens)
MODEL_PRICING = {
    "deepseek-v4-flash": {"input": 0.15, "output": 0.60, "avg": 0.30},
    "deepseek-v4-pro": {"input": 2.00, "output": 8.00, "avg": 4.00},
}


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
        "model": "deepseek-v4-flash",
        "provider": "deepseek",
        "projects": [],
        "last_updated": str(date.today())
    }


def save_config(config):
    with open(CONFIG_PATH, 'w') as f:
        json.dump(config, f, indent=2)
        f.write('\n')


def get_deepseek_api_key():
    """Extract DeepSeek API key from .env file."""
    if not os.path.exists(ENV_PATH):
        return None
    with open(ENV_PATH) as f:
        for line in f:
            line = line.strip()
            if line.startswith('DEEPSEEK_API_KEY=') and not line.startswith('#'):
                return line.split('=', 1)[1].strip().strip('"').strip("'")
    return None


def fetch_deepseek_balance():
    """Query DeepSeek API for account balance."""
    api_key = get_deepseek_api_key()
    if not api_key:
        return None, None

    try:
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Accept': 'application/json',
            'User-Agent': 'Hermes-Portal'
        }
        req = urllib.request.Request(
            'https://api.deepseek.com/user/balance',
            headers=headers
        )
        resp = urllib.request.urlopen(req, timeout=10)
        data = json.loads(resp.read())

        if data.get('is_available') and data.get('balance_infos'):
            for info in data['balance_infos']:
                if info['currency'] == 'USD':
                    balance = float(info['total_balance'])
                    return balance, 'deepseek-v4-flash'
        return None, None
    except Exception:
        return None, None


def estimate_tokens(balance, model_id):
    """Estimate remaining tokens based on balance and model pricing."""
    pricing = MODEL_PRICING.get(model_id, MODEL_PRICING["deepseek-v4-flash"])
    avg_cost = pricing["avg"]
    if avg_cost > 0 and balance > 0:
        return int(balance / avg_cost * 1_000_000)
    return 0


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
                for p in config["projects"]:
                    if p["name"] == item:
                        p["last_updated"] = str(date.today())
                        break

    config["last_updated"] = str(date.today())
    return config


def main():
    config = load_config()

    # Parse CLI args for kredyt/tokens overrides
    args = sys.argv[1:]
    kredyt_override = None
    tokens_override = None
    i = 0
    while i < len(args):
        if args[i] == '--kredyt' and i + 1 < len(args):
            kredyt_override = float(args[i + 1])
            i += 2
        elif args[i] == '--tokens' and i + 1 < len(args):
            tokens_override = int(args[i + 1])
            i += 2
        else:
            i += 1

    # Fetch DeepSeek balance (unless overridden)
    if kredyt_override is not None:
        config["kredyt"] = kredyt_override
        print(f"  💰 Kredyt (manual): ${kredyt_override}")
    else:
        balance, model_id = fetch_deepseek_balance()
        if balance is not None:
            config["kredyt"] = balance
            config["model"] = model_id or config.get("model", "deepseek-v4-flash")
            config["provider"] = "deepseek"
            print(f"  💰 Kredyt (from API): ${balance}")
        else:
            print(f"  ⚠️  Could not fetch DeepSeek balance — keeping existing value: ${config.get('kredyt', 0)}")

    # Estimate tokens (unless overridden)
    if tokens_override is not None:
        config["tokens"] = tokens_override
        print(f"  🔑 Tokens (manual): {tokens_override:,}")
    else:
        balance_to_use = kredyt_override if kredyt_override is not None else config.get("kredyt", 0)
        model_id = config.get("model", "deepseek-v4-flash")
        tokens = estimate_tokens(balance_to_use, model_id)
        config["tokens"] = tokens
        print(f"  🔑 Tokens (estimated): {tokens:,}")

    config["last_updated"] = str(date.today())
    config = sync_projects(config)
    save_config(config)
    print(f"  ✅ Portal config saved — {str(date.today())}")


if __name__ == "__main__":
    main()
