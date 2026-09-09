import logging

# Configuration Constants
API_BASE_URL = "https://api.crypto-tracker-99.io/v1"
TIMEOUT_SECONDS = 10
MAX_RETRIES = 3

# Error Messages
ERR_NETWORK = "Connection failed: check your internet configuration"
ERR_AUTH = "Authentication token expired or invalid"
ERR_LIMIT = "Rate limit exceeded: please wait before retrying"
ERR_PARSING = "Data format invalid: could not decode response"

# Logging configuration
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

def get_logger(name: str) -> logging.Logger:
    """Returns a standard logger for tracking modules."""
    return logging.getLogger(name)

# Supported Assets
SUPPORTED_ASSETS = {
    "BTC": "bitcoin",
    "ETH": "ethereum",
    "SOL": "solana"
}

# Status Codes
HTTP_SUCCESS = 200
HTTP_UNAUTHORIZED = 401
HTTP_RATE_LIMIT = 429
HTTP_SERVER_ERROR = 500