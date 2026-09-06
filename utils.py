import time
import logging
import functools
from typing import Callable, Any

# Configure logger for tracking
logger = logging.getLogger('crypto-tracker-99')

def retry_on_failure(retries: int = 3, delay: float = 2.0, backoff: float = 1.5):
    """Decorator for retrying network operations with exponential backoff."""
    def decorator(func: Callable):
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            current_delay = delay
            for attempt in range(retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == retries - 1:
                        logger.error(f'Operation failed after {retries} attempts: {e}')
                        raise
                    
                    logger.warning(f'Attempt {attempt + 1} failed, retrying in {current_delay}s...')
                    time.sleep(current_delay)
                    current_delay *= backoff
            return None
        return wrapper
    return decorator