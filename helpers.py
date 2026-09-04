from typing import Dict, List, Optional


def calculate_portfolio_value(prices: Dict[str, float], holdings: Dict[str, float]) -> float:
    """Calculate the total fiat value of a crypto portfolio based on current market prices.

    Args:
        prices: Dictionary mapping crypto symbols to current prices in USD.
        holdings: Dictionary mapping crypto symbols to amount held.

    Returns:
        Total portfolio value in USD.
    """
    total = 0.0
    for symbol, amount in holdings.items():
        price = prices.get(symbol, 0.0)
        total += price * amount
    return total


def format_currency(value: float, currency_symbol: str = "$") -> str:
    """Format a numeric value as a currency string with appropriate decimals.

    Args:
        value: The numerical amount to format.
        currency_symbol: Prefix symbol for currency representation.

    Returns:
        Formatted currency string.
    """
    if 0 < value < 0.01:
        return f"{currency_symbol}{value:.6f}"
    return f"{currency_symbol}{value:,.2f}"


def filter_top_gainers(market_data: List[Dict[str, float]], limit: int = 5) -> List[Dict[str, float]]:
    """Sort and filter market data entries to return the top gaining cryptocurrencies.

    Args:
        market_data: List of dictionaries containing coin data including 'change_24h'.
        limit: Maximum number of top gainers to return.

    Returns:
        Sorted list of top gaining coin records.
    """
    sorted_coins = sorted(
        market_data,
        key=lambda coin: coin.get("change_24h", 0.0),
        reverse=True
    )
    return sorted_coins[:limit]
