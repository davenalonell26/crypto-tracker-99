import os
from typing import List


class Config:
    """Application configuration for crypto-tracker-99.

    Handles environment variables and provides sensible defaults
    for tracking cryptocurrencies.
    """

    # Coingecko API configuration
    API_BASE_URL: str = os.getenv(
        "CRYPTO_API_URL", "https://api.coingecko.com/api/v3"
    )
    API_KEY: str = os.getenv("CRYPTO_API_KEY", "")

    # Default coins to track if none provided
    DEFAULT_COINS: List[str] = [
        "bitcoin",
        "ethereum",
        "solana",
        "cardano",
        "ripple",
    ]

    # Tracking settings
    UPDATE_INTERVAL_SEC: int = int(os.getenv("UPDATE_INTERVAL_SEC", "60"))
    FIAT_CURRENCY: str = os.getenv("FIAT_CURRENCY", "usd")

    # Logging configuration
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")

    @classmethod
    def get_tracked_coins(cls) -> List[str]:
        """Parse and return the list of coins to track from environment."""
        coins_env = os.getenv("TRACKED_COINS")
        if coins_env:
            return [coin.strip().lower() for coin in coins_env.split(",")]
        return cls.DEFAULT_COINS

    @classmethod
    def as_dict(cls) -> dict:
        """Return config settings as a dictionary for logging or debugging."""
        return {
            "api_base_url": cls.API_BASE_URL,
            "tracked_coins": cls.get_tracked_coins(),
            "update_interval": cls.UPDATE_INTERVAL_SEC,
            "fiat_currency": cls.FIAT_CURRENCY,
            "log_level": cls.LOG_LEVEL,
        }
