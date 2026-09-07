from typing import Dict, Any, Optional

def format_currency(value: float, currency: str = "USD") -> str:
    """Formats a numeric value as a currency string."""
    if currency.upper() == "USD":
        return f"${value:,.2f}"
    elif currency.upper() == "EUR":
        return f"€{value:,.2f}"
    return f"{value:,.2f} {currency.upper()}"

def calculate_percentage_change(old_price: float, new_price: float) -> float:
    """Calculates the percentage change between two prices."""
    if old_price == 0:
        return 0.0
    return ((new_price - old_price) / old_price) * 100.0

def extract_ticker_data(raw_data: Dict[str, Any]) -> Dict[str, Any]:
    """Extracts standard ticker fields from a raw API response."""
    return {
        "symbol": raw_data.get("symbol", "UNKNOWN").upper(),
        "price": float(raw_data.get("price", 0.0)),
        "volume": float(raw_data.get("volume24h", 0.0)),
        "change_24h": float(raw_data.get("percentChange24h", 0.0))
    }

def is_price_alert_triggered(current_price: float, target_price: float, condition: str) -> bool:
    """Checks if a price alert condition is met (above or below)."""
    cond = condition.lower()
    if cond == "above":
        return current_price >= target_price
    elif cond == "below":
        return current_price <= target_price
    return False