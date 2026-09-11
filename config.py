import os
import json
from typing import Any, Dict

DEFAULT_CONFIG = {
    "api_url": "https://api.coingecko.com/api/v3",
    "update_interval_seconds": 60,
    "supported_cryptos": ["bitcoin", "ethereum", "solana"],
    "fiat_currency": "usd",
    "retry_attempts": 3,
    "enable_cache": True
}

class ConfigLoader:
    """Loads configuration from a JSON file, environment variables, or defaults."""

    def __init__(self, config_path: str = "config.json"):
        self.config_path = config_path
        self.config: Dict[str, Any] = DEFAULT_CONFIG.copy()
        self.load()

    def load(self) -> Dict[str, Any]:
        """Loads config from file if it exists, then overrides with env variables."""
        if os.path.exists(self.config_path):
            try:
                with open(self.config_path, "r") as f:
                    file_config = json.load(f)
                    self.config.update(file_config)
            except (json.JSONDecodeError, OSError):
                pass

        for key in self.config:
            env_key = f"CRYPTO_TRACKER_{key.upper()}"
            env_value = os.getenv(env_key)
            if env_value is not None:
                self._set_cast_val(key, env_value)

        return self.config

    def _set_cast_val(self, key: str, value: str) -> None:
        """Casts environment variable string to the appropriate default type."""
        default_val = DEFAULT_CONFIG.get(key)
        if isinstance(default_val, bool):
            self.config[key] = value.lower() in ("true", "1", "yes")
        elif isinstance(default_val, int):
            try:
                self.config[key] = int(value)
            except ValueError:
                pass
        elif isinstance(default_val, list):
            try:
                self.config[key] = json.loads(value)
            except json.JSONDecodeError:
                self.config[key] = [item.strip() for item in value.split(",")]
        else:
            self.config[key] = value

    def get(self, key: str, default: Any = None) -> Any:
        """Retrieves a configuration value."""
        return self.config.get(key, default)
