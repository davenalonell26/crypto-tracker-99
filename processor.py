import typing

class CryptoDataProcessor:
    """Processes raw cryptocurrency market data for analysis."""

    def __init__(self, decimal_places: int = 2):
        self.decimal_places = decimal_places

    def clean_price_data(self, raw_data: list[dict]) -> list[dict]:
        """Filters out invalid entries and formats price values."""
        cleaned = []
        for entry in raw_data:
            symbol = entry.get("symbol")
            price = entry.get("price")
            if symbol and price is not None:
                try:
                    cleaned.append({
                        "symbol": str(symbol).upper(),
                        "price": round(float(price), self.decimal_places),
                        "timestamp": entry.get("timestamp")
                    })
                except (ValueError, TypeError):
                    continue
        return cleaned

    def calculate_average_price(self, prices: list[dict], symbol: str) -> float:
        """Calculates the average price for a specific symbol."""
        matching_prices = [
            item["price"] for item in prices 
            if item["symbol"] == symbol.upper()
        ]
        if not matching_prices:
            return 0.0
        return round(sum(matching_prices) / len(matching_prices), self.decimal_places)