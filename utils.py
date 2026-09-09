import time
import functools
import logging
from typing import Callable, Any

# crypto-tracker-99 network resilience utilities

logger = logging.getLogger(__name__)

def retry_request(max_retries: int = 3, delay: float = 1.5):
    """Decorator for retrying network operations on failure."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            last_exception = None
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    last_exception = e
                    logger.warning(
                        f"Attempt {attempt + 1} failed for {func.__name__}: {e}"
                    )
                    if attempt < max_retries - 1:
                        time.sleep(delay * (2 ** attempt))
            logger.error(f"Final attempt failed for {func.__name__}")
            raise last_exception
        return wrapper
    return decorator

def format_crypto_price(price: float) -> str:
    """Helper for normalizing price data strings."""
    return f"${price:,.2f}"