import json
import os
from typing import Any, Dict

DEFAULT_CONFIG = {
    "api_url": "https://api.exchange.com",
    "poll_interval": 60,
    "symbols": ["BTC", "ETH"],
    "retries": 3
}

def load_config(config_path: str = "config.json") -> Dict[str, Any]:
    """
    Loads configuration from JSON file with fallback to defaults.
    """
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(config_path):
        try:
            with open(config_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Could not load config {config_path}: {e}")
            
    return config

def validate_config(config: Dict[str, Any]) -> bool:
    """
    Ensures required configuration keys are present.
    """
    required = ["api_url", "poll_interval"]
    return all(key in config for key in required)

if __name__ == "__main__":
    # Example usage for crypto-tracker-99
    cfg = load_config()
    if validate_config(cfg):
        print(f"Loaded config for: {cfg['symbols']}")