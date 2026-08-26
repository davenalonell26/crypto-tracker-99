from typing import List, Dict, Optional
from dataclasses import dataclass

@dataclass
class CryptoPrice:
    """Represents cryptocurrency price data."""
    symbol: str
    price: float
    timestamp: int

def process_price_changes(prices: List[CryptoPrice], min_change: float = 0.01) -> Dict[str, float]:
    """Calculate significant price changes per symbol.

    Args:
        prices: List of price records.
        min_change: Minimum change ratio to report.

    Returns:
        Symbol to change ratio dict.
    """
    if not prices:
        return {}

    grouped: Dict[str, List[CryptoPrice]] = {}
    for p in prices:
        grouped.setdefault(p.symbol, []).append(p)

    changes: Dict[str, float] = {}
    for symbol, lst in grouped.items():
        if len(lst) < 2:
            continue
        srt = sorted(lst, key=lambda x: x.timestamp)
        chg = (srt[-1].price - srt[0].price) / srt[0].price
        if abs(chg) >= min_change:
            changes[symbol] = round(chg, 4)
    return changes

def get_average(prices: List[CryptoPrice]) -> float:
    """Return average price or zero if none."""
    if not prices:
        return 0.0
    return sum(p.price for p in prices) / len(prices)

class CryptoProcessor:
    """Handles processing of crypto price lists."""
    def __init__(self, prices: Optional[List[CryptoPrice]] = None) -> None:
        """Set up with initial prices if provided."""
        self.prices: List[CryptoPrice] = prices or []

    def add_price(self, price: CryptoPrice) -> None:
        """Append a price to the internal list."""
        self.prices.append(price)

    def get_changes(self, threshold: float = 0.05) -> Dict[str, float]:
        """Return changes above the given threshold."""
        return process_price_changes(self.prices, threshold)

    def get_stats(self) -> Dict[str, float]:
        """Provide count, avg, min and max stats."""
        if not self.prices:
            return {"count": 0, "avg": 0.0, "min": 0.0, "max": 0.0}

        vals = [p.price for p in self.prices]
        avg = get_average(self.prices)
        return {
            "count": len(self.prices),
            "avg": round(avg, 2),
            "min": min(vals),
            "max": max(vals)
        }

if __name__ == "__main__":
    prices = [CryptoPrice("BTC", 50000.0, 100), CryptoPrice("BTC", 51000.0, 200)]
    cp = CryptoProcessor(prices)
    print(cp.get_stats())
    print(cp.get_changes(0.01))