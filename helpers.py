import os
import json
from typing import Any, Dict

DEFAULT_CONFIG: Dict[str, Any] = {
    "api_url": "https://api.coingecko.com/api/v3",
    "refresh_interval": 60,
    "currency": "usd",
    "log_level": "INFO"
}

def load_config(file_path: str = "config.json") -> Dict[str, Any]:
    """Loads configuration from file or returns defaults."""
    config = DEFAULT_CONFIG.copy()
    
    if os.path.exists(file_path):
        try:
            with open(file_path, "r") as f:
                user_config = json.load(f)
                config.update(user_config)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Warning: Failed to load config file: {e}. Using defaults.")
    
    return config

def get_config_value(key: str, default: Any = None) -> Any:
    """Fetches specific config key with fallback."""
    config = load_config()
    return config.get(key, default)