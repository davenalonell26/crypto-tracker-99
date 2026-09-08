from typing import Dict, List, Optional

class CryptoTracker:
    """Core engine for tracking cryptocurrency price data."""

    def __init__(self, symbols: List[str]) -> None:
        self.symbols: List[str] = symbols
        self.data: Dict[str, float] = {}

    def update_price(self, symbol: str, price: float) -> None:
        """Updates internal price cache for a given symbol."""
        if symbol in self.symbols:
            self.data[symbol] = price

    def get_price(self, symbol: str) -> Optional[float]:
        """Retrieves the cached price for a specific asset."""
        return self.data.get(symbol)

    def get_summary(self) -> Dict[str, float]:
        """Returns the current state of tracked assets."""
        return self.data.copy()

    def calculate_portfolio_value(self, holdings: Dict[str, float]) -> float:
        """Calculates total value based on provided holdings dictionary."""
        total: float = 0.0
        for symbol, amount in holdings.items():
            price = self.get_price(symbol)
            if price:
                total += price * amount
        return total