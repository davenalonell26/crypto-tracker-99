import time
import functools
import logging

logger = logging.getLogger("crypto-tracker-99")

def retry_network_operation(max_retries=3, delay=2, backoff=2):
    """Decorator to retry network operations with exponential backoff."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            current_delay = delay
            for attempt in range(1, max_retries + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries:
                        logger.error(f"Operation {func.__name__} failed after {max_retries} attempts: {e}")
                        raise
                    logger.warning(f"Attempt {attempt} for {func.__name__} failed: {e}. Retrying in {current_delay}s...")
                    time.sleep(current_delay)
                    current_delay *= backoff
        return wrapper
    return decorator

def safe_api_call(api_func, *args, **kwargs):
    """Execute an API function safely with default retry logic wrapper."""
    @retry_network_operation()
    def _execute():
        return api_func(*args, **kwargs)
    
    try:
        return _execute()
    except Exception as exc:
        logger.critical(f"Critical failure during API execution: {exc}")
        return None
