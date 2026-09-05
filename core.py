from typing import Dict, List, Optional
import requests

class CryptoTracker:
    """Main service for tracking cryptocurrency market data."""

    def __init__(self, api_url: str, timeout: int = 10) -> None:
        self.api_url = api_url
        self.timeout = timeout

    def fetch_price(self, symbol: str) -> Optional[float]:
        """Retrieve current price for a specific ticker symbol."""
        try:
            response = requests.get(f"{self.api_url}/price/{symbol}", timeout=self.timeout)
            response.raise_for_status()
            data: Dict[str, float] = response.json()
            return data.get("price")
        except (requests.RequestException, ValueError):
            return None

    def get_portfolio_value(self, holdings: Dict[str, float]) -> float:
        """Calculate total market value of all held assets."""
        total: float = 0.0
        for symbol, amount in holdings.items():
            price = self.fetch_price(symbol)
            if price:
                total += price * amount
        return total

    def validate_tickers(self, symbols: List[str]) -> List[str]:
        """Filter list of symbols to ensure they exist."""
        valid_list: List[str] = []
        for symbol in symbols:
            if self.fetch_price(symbol) is not None:
                valid_list.append(symbol)
        return valid_list