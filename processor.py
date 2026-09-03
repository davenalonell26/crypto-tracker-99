import time
import logging
from typing import Callable, Any

logger = logging.getLogger('crypto-tracker-99')

def execute_with_retry(func: Callable, retries: int = 3, delay: float = 1.0) -> Any:
    """
    Executes a network-dependent function with exponential backoff.
    """
    last_exception = None
    
    for attempt in range(retries):
        try:
            return func()
        except (ConnectionError, TimeoutError) as e:
            last_exception = e
            wait_time = delay * (2 ** attempt)
            logger.warning(f"Attempt {attempt + 1} failed: {e}. Retrying in {wait_time}s...")
            time.sleep(wait_time)
        except Exception as e:
            logger.error(f"Critical failure: {e}")
            raise

    logger.error(f"Max retries exceeded. Final error: {last_exception}")
    raise last_exception

def fetch_ticker_data(api_client, symbol: str):
    """
    Example usage for fetching crypto market data.
    """
    return execute_with_retry(lambda: api_client.get_price(symbol))