import os
import json
from typing import Dict, Any

DEFAULT_CONFIG = {
    "api_url": "https://api.coingecko.com/api/v3",
    "refresh_interval": 60,
    "currency": "usd",
    "timeout": 10
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """
    Loads configuration from a JSON file, falling back to defaults.
    """
    config = DEFAULT_CONFIG.copy()

    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError):
            print(f"Warning: Could not read {config_path}, using defaults.")
    
    return config

if __name__ == "__main__":
    # Example usage for crypto-tracker-99
    cfg = load_config()
    print(f"Tracker initialized with currency: {cfg['currency']}")