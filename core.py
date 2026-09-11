import requests
from typing import Optional

class CryptoFetchError(Exception):
    """Custom exception for cryptocurrency data retrieval errors."""
    pass

class CryptoTracker:
    def __init__(self, base_url: str = "https://api.coingecko.com/api/v3", timeout: int = 10):
        self.base_url = base_url
        self.timeout = timeout

    def fetch_price(self, coin_id: str, vs_currency: str = "usd") -> Optional[float]:
        """Fetch current price for a coin with robust edge case error handling."""
        if not coin_id or not isinstance(coin_id, str):
            raise ValueError("Invalid coin_id provided")

        clean_coin = coin_id.lower().strip()
        clean_currency = vs_currency.lower().strip()
        url = f"{self.base_url}/simple/price"
        params = {"ids": clean_coin, "vs_currencies": clean_currency}

        try:
            response = requests.get(url, params=params, timeout=self.timeout)
            response.raise_for_status()
            data = response.json()

            if not isinstance(data, dict) or clean_coin not in data:
                raise CryptoFetchError(f"Coin '{clean_coin}' not found in response")

            price_data = data[clean_coin]
            if clean_currency not in price_data:
                raise CryptoFetchError(f"Currency '{clean_currency}' not available for '{clean_coin}'")

            price = price_data[clean_currency]
            if not isinstance(price, (int, float)) or price < 0:
                raise CryptoFetchError(f"Invalid price value received: {price}")

            return float(price)

        except requests.exceptions.Timeout:
            raise CryptoFetchError(f"Request timed out while fetching price for {clean_coin}")
        except requests.exceptions.RequestException as e:
            raise CryptoFetchError(f"Network error occurred: {str(e)}")
        except (ValueError, KeyError) as e:
            raise CryptoFetchError(f"Failed to parse API response: {str(e)}")