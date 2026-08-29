"""Centralized constants for crypto-tracker-99.
This module was created during cleanup to consolidate all magic values
and configuration constants from across the codebase.
"""

from typing import Dict, List

# Supported cryptocurrency pairs (quote is always USDT for simplicity)
SUPPORTED_PAIRS: List[str] = [
    "BTCUSDT",
    "ETHUSDT",
    "SOLUSDT",
    "ADAUSDT",
]

# Available data providers and their base API URLs
DATA_PROVIDERS: Dict[str, str] = {
    "binance": "https://api.binance.com/api/v3",
    "coingecko": "https://api.coingecko.com/api/v3",
}

# Timeframe mappings: key is API format, value is minutes
TIMEFRAME_MINUTES: Dict[str, int] = {
    "1m": 1,
    "5m": 5,
    "15m": 15,
    "1h": 60,
    "4h": 240,
    "1d": 1440,
}

# Default parameters for tracking operations
DEFAULT_PARAMS: Dict[str, object] = {
    "timeframe": "1h",
    "limit": 500,
    "provider": "binance",
    "include_volume": True,
}

# Limits to prevent excessive resource use
MAX_CANDLES_PER_REQUEST = 1000
MAX_TRACKED_ASSETS = 50
MAX_DAYS_HISTORY = 365

# Common HTTP headers for API requests
DEFAULT_HEADERS: Dict[str, str] = {
    "Content-Type": "application/json",
    "User-Agent": "crypto-tracker-99/1.0",
}

# Error code mappings specific to crypto APIs
API_ERROR_CODES: Dict[int, str] = {
    400: "invalid_parameter",
    429: "rate_limit_exceeded",
    500: "server_error",
}

# Environment variable keys used by the application
ENVIRONMENT_VARIABLES: Dict[str, str] = {
    "api_key": "CRYPTO_API_KEY",
    "api_secret": "CRYPTO_API_SECRET",
}

def get_all_pairs() -> List[str]:
    """Return copy of supported pairs list."""
    return SUPPORTED_PAIRS.copy()

def is_supported_pair(pair: str) -> bool:
    """Check if the given pair is supported."""
    return pair in SUPPORTED_PAIRS