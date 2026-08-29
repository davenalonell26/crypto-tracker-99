import requests
from typing import Dict, Any, Optional
import time

class CryptoPriceHandler:
    """Handler for fetching cryptocurrency prices."""

    def __init__(self, base_url: str = "https://api.coingecko.com/api/v3") -> None:
        """Initialize handler with API base URL.

        Args:
            base_url: The API base URL.
        """
        self.base_url = base_url

    def fetch_price(self, coin_id: str, currency: str = "usd") -> Dict[str, Any]:
        """Fetch price for a crypto coin.

        Args:
            coin_id: Coin identifier like 'bitcoin'.
            currency: Currency like 'usd'.

        Returns:
            Price data from API.
        """
        url = f"{self.base_url}/simple/price"
        params = {"ids": coin_id, "vs_currencies": currency}
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_price_with_retry(self, coin_id: str, currency: str = "usd", max_retries: int = 3) -> Optional[Dict[str, Any]]:
        """Fetch with retries.

        Args:
            coin_id: Coin ID.
            currency: Target currency.
            max_retries: Retry count.

        Returns:
            Data or None on failure.
        """
        for attempt in range(max_retries):
            try:
                return self.fetch_price(coin_id, currency)
            except requests.exceptions.RequestException:
                if attempt >= max_retries - 1:
                    return None
                time.sleep(1)
        return None


def process_prices(data: Dict[str, Any]) -> Dict[str, float]:
    """Process API data to extract prices.

    Args:
        data: Raw response data.

    Returns:
        Processed prices dict.
    """
    processed: Dict[str, float] = {}
    for coin, info in data.items():
        if isinstance(info, dict):
            for price in info.values():
                if isinstance(price, (int, float)):
                    processed[coin] = float(price)
                    break
    return processed