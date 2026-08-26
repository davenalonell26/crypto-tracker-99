import datetime
from typing import List, Dict, Any

def calculate_total_value(holdings: List[Dict[str, Any]], current_prices: Dict[str, float]) -> float:
    total = 0.0
    for holding in holdings:
        symbol = holding.get("symbol", "").upper()
        amount = holding.get("amount", 0.0)
        if symbol in current_prices:
            total += amount * current_prices[symbol]
    return total

def get_percentage_change(previous_price: float, current_price: float) -> float:
    if previous_price == 0:
        return 0.0
    change = ((current_price - previous_price) / previous_price) * 100
    return round(change, 2)

def format_price(price: float, symbol: str = "USD") -> str:
    if symbol == "USD":
        return f"${price:,.2f}"
    return f"{price:,.2f} {symbol}"

def is_valid_crypto_symbol(symbol: str) -> bool:
    if not isinstance(symbol, str):
        return False
    symbol = symbol.strip().upper()
    return len(symbol) >= 2 and len(symbol) <= 10 and symbol.isalpha()

def convert_timestamp_to_date(timestamp: int) -> str:
    dt = datetime.datetime.fromtimestamp(timestamp)
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def filter_holdings_by_symbol(holdings: List[Dict[str, Any]], symbol: str) -> List[Dict[str, Any]]:
    symbol = symbol.upper()
    return [h for h in holdings if h.get("symbol", "").upper() == symbol]

def calculate_average_price(prices: List[float]) -> float:
    if not prices:
        return 0.0
    return sum(prices) / len(prices)

def get_top_performers(holdings: List[Dict[str, Any]], prices: Dict[str, float], n: int = 3) -> List[str]:
    if not holdings or not prices:
        return []
    values = []
    for h in holdings:
        sym = h.get("symbol", "").upper()
        amt = h.get("amount", 0)
        if sym in prices:
            values.append((sym, amt * prices[sym]))
    values.sort(key=lambda x: x[1], reverse=True)
    return [v[0] for v in values[:n]]
