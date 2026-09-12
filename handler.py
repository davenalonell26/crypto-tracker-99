import functools
import time
from typing import Dict, Any

# Cache crypto price lookup results for 30 seconds to minimize API calls
_price_cache: Dict[str, tuple[float, float]] = {}
CACHE_TTL = 30

@functools.lru_cache(maxsize=128)
def get_normalized_ticker(ticker: str) -> str:
    return ticker.strip().upper()

def get_cached_price(symbol: str, fetch_func: callable) -> float:
    """Retrieves price with short-term memoization."""
    normalized = get_normalized_ticker(symbol)
    now = time.time()
    
    if normalized in _price_cache:
        timestamp, price = _price_cache[normalized]
        if now - timestamp < CACHE_TTL:
            return price

    # Fetch fresh data if expired or missing
    new_price = fetch_func(normalized)
    _price_cache[normalized] = (now, new_price)
    return new_price

def batch_process_prices(tickers: list, fetch_func: callable) -> Dict[str, float]:
    """Optimized batch fetcher reducing redundant network I/O."""
    results = {}
    for ticker in tickers:
        results[ticker] = get_cached_price(ticker, fetch_func)
    return results