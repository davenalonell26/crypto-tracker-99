import time
import functools
import requests
from typing import Callable, Any

def retry_request(max_retries: int = 3, backoff: float = 2.0):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            current_delay = backoff
            
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except (requests.exceptions.RequestException, ConnectionError) as e:
                    last_exception = e
                    if attempt < max_retries - 1:
                        time.sleep(current_delay)
                        current_delay *= 2
                    continue
            
            raise last_exception
        return wrapper
    return decorator

@retry_request(max_retries=3)
def fetch_crypto_price(symbol: str) -> dict:
    """Example usage for fetching crypto market data."""
    url = f"https://api.exchange.com/v1/ticker/{symbol}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()