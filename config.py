import os
from typing import List
from dataclasses import dataclass, field


@dataclass
class Config:
    '''Configuration settings for the crypto-tracker-99 application.

    This class holds all necessary parameters for interacting with
    cryptocurrency APIs and managing tracking behavior.
    '''
    api_key: str = field(default_factory=lambda: os.getenv('CRYPTO_API_KEY', ''))
    base_url: str = field(default='https://api.coingecko.com/api/v3')
    tracked_cryptos: List[str] = field(default_factory=lambda: ['bitcoin', 'ethereum', 'solana'])
    update_interval: int = field(default=60)
    max_retries: int = field(default=3)
    request_timeout: int = field(default=10)
    enable_cache: bool = field(default=True)
    cache_ttl: int = field(default=300)


def load_config() -> Config:
    '''Load configuration from environment variables.

    Overrides default values with environment variables if set.
    Environment variables:
    - CRYPTO_API_KEY: API key for crypto data provider
    - TRACKED_CRYPTOS: Comma-separated list of crypto ids
    - UPDATE_INTERVAL: Seconds between updates

    Returns:
        Config: Initialized configuration instance with type annotations.
    '''
    tracked = os.getenv('TRACKED_CRYPTOS', 'bitcoin,ethereum,solana')
    return Config(
        api_key=os.getenv('CRYPTO_API_KEY', ''),
        base_url=os.getenv('CRYPTO_BASE_URL', 'https://api.coingecko.com/api/v3'),
        tracked_cryptos=tracked.split(',') if tracked else [],
        update_interval=int(os.getenv('UPDATE_INTERVAL', '60')),
        max_retries=int(os.getenv('MAX_RETRIES', '3')),
        request_timeout=int(os.getenv('REQUEST_TIMEOUT', '10')),
        enable_cache=os.getenv('ENABLE_CACHE', 'true').lower() == 'true',
        cache_ttl=int(os.getenv('CACHE_TTL', '300')),
    )


def get_api_endpoint(config: Config, path: str) -> str:
    '''Build complete API URL using config base and provided path.

    Args:
        config: Application configuration object.
        path: Relative API path without leading slash.

    Returns:
        str: Fully qualified API endpoint URL.
    '''
    if not path.startswith('/'):
        path = '/' + path
    return f'{config.base_url}{path}'


def is_config_valid(config: Config) -> bool:
    '''Check if the loaded config meets basic requirements.

    Args:
        config: The config to validate.

    Returns:
        bool: Whether the configuration is valid for use.
    '''
    if not config.tracked_cryptos:
        return False
    if config.update_interval < 30:
        return False
    return True