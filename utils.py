from typing import Dict, List, Union

def calculate_price_change(open_price: float, current_price: float) -> float:
    """
    Calculates the percentage change between open and current price.
    Returns 0.0 if open price is invalid or zero.
    """
    if open_price <= 0:
        return 0.0
    return ((current_price - open_price) / open_price) * 100.0

def format_crypto_price(price: float) -> str:
    """
    Formats a crypto price to a readable string.
    Uses more decimal places for sub-dollar assets.
    """
    if price >= 1.0:
        return f"${price:,.2f}"
    if price > 0.0:
        return f"${price:,.6f}"
    return "$0.00"

def extract_ticker_symbols(raw_data: List[Dict[str, Union[str, float]]]) -> List[str]:
    """
    Extracts and standardizes ticker symbols from raw API payload.
    Converts all tickers to uppercase and removes duplicates.
    """
    tickers = set()
    for item in raw_data:
        symbol = item.get("symbol") or item.get("ticker")
        if isinstance(symbol, str):
            tickers.add(symbol.upper().strip())
    return sorted(list(tickers))