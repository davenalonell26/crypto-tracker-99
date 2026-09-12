import decimal
from typing import Union

def format_currency(value: Union[float, str, decimal.Decimal], precision: int = 8) -> str:
    """Formats crypto values to strings with defined precision."""
    val = decimal.Decimal(str(value))
    format_str = f"0.{'0' * precision}"
    return format(val.quantize(decimal.Decimal(format_str), rounding=decimal.ROUND_DOWN))

def calculate_percentage_change(old: float, new: float) -> float:
    """Calculates percentage change between two price points."""
    if old == 0:
        return 0.0
    return ((new - old) / abs(old)) * 100

def sanitize_symbol(symbol: str) -> str:
    """Normalizes crypto symbols to uppercase format."""
    return symbol.strip().upper()

def get_market_cap_tier(market_cap: float) -> str:
    """Categorizes market cap into simple tiers."""
    if market_cap > 1_000_000_000:
        return "large-cap"
    elif market_cap > 100_000_000:
        return "mid-cap"
    return "small-cap"