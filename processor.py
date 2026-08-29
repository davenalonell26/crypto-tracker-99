import json
from typing import Dict, List, Optional

def calculate_percentage_change(previous: float, current: float) -> float:
    """Calculate the percentage change from previous to current price."""
    if previous == 0:
        return 0.0
    change = ((current - previous) / previous) * 100
    return round(change, 2)

def format_crypto_value(value: float, symbol: str = "USD") -> str:
    """Format the value with currency symbol for display."""
    if symbol == "USD":
        return f"${value:,.2f}"
    elif symbol == "EUR":
        return f"€{value:,.2f}"
    else:
        return f"{value:.6f} {symbol}"

def compute_total_value(holdings: Dict[str, float], prices: Dict[str, float]) -> float:
    """Calculate the total portfolio value in base currency."""
    total = 0.0
    for crypto, amount in holdings.items():
        price = prices.get(crypto, 0.0)
        total += amount * price
    return round(total, 2)

def get_average_price(prices: List[float]) -> float:
    """Compute average price from list of prices."""
    if not prices:
        return 0.0
    return round(sum(prices) / len(prices), 2)

def filter_by_change(percentage_changes: Dict[str, float], min_change: float = 1.0) -> Dict[str, float]:
    """Filter entries with absolute change above minimum."""
    return {k: v for k, v in percentage_changes.items() if abs(v) >= min_change}

def parse_price_json(json_str: str) -> Optional[Dict[str, float]]:
    """Parse JSON string into crypto prices dictionary."""
    try:
        data = json.loads(json_str)
        return {str(k): float(v) for k, v in data.items() if isinstance(v, (int, float))}
    except (json.JSONDecodeError, ValueError, TypeError):
        return None