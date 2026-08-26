import time
from typing import Dict, Any, Optional


def format_crypto_amount(amount: float, decimals: int = 8) -> str:
    """Format cryptocurrency amount to a fixed decimal string."""
    if amount < 0:
        raise ValueError("Amount cannot be negative")
    
    format_string = f"{{:.{decimals}f}}"
    return format_string.format(amount).rstrip('0').rstrip('.')


def calculate_price_change(current_price: float, previous_price: float) -> Optional[float]:
    """Calculate percentage change between two prices safely."""
    if previous_price == 0 or previous_price is None:
        return None
    
    change = ((current_price - previous_price) / previous_price) * 100.0
    return round(change, 4)


def sanitize_ticker_symbol(symbol: str) -> str:
    """Clean and normalize crypto ticker symbols."""
    if not isinstance(symbol, str):
        return ""
    
    return symbol.strip().upper().replace("/", "-")


def current_timestamp() -> int:
    """Return current Unix timestamp in seconds."""
    return int(time.time())


def parse_ticker_payload(payload: Dict[str, Any]) -> Dict[str, Any]:
    """Extract essential fields from raw exchange ticker payload."""
    return {
        "symbol": sanitize_ticker_symbol(payload.get("symbol", "")),
        "price": float(payload.get("price", 0.0)),
        "volume": float(payload.get("volume", 0.0)),
        "timestamp": payload.get("timestamp", current_timestamp())
    }
