import logging
from typing import Dict, Any, List

logger = logging.getLogger(__name__)

class CryptoDataProcessor:
    """Processes and validates incoming cryptocurrency tick data."""
    
    def __init__(self, allowed_symbols: List[str]):
        self.allowed_symbols = {sym.upper() for sym in allowed_symbols}

    def validate_payload(self, data: Dict[str, Any]) -> bool:
        """Validates the structure and values of the crypto data payload."""
        if not isinstance(data, dict):
            logger.error("Payload is not a dictionary.")
            return False
            
        required_fields = ["symbol", "price", "volume", "timestamp"]
        for field in required_fields:
            if field not in data:
                logger.error(f"Missing required field: {field}")
                return False

        symbol = data["symbol"]
        if not isinstance(symbol, str) or symbol.upper() not in self.allowed_symbols:
            logger.error(f"Invalid or unsupported symbol: {symbol}")
            return False

        try:
            price = float(data["price"])
            volume = float(data["volume"])
            if price <= 0 or volume < 0:
                logger.error(f"Invalid numeric values: price={price}, volume={volume}")
                return False
        except (ValueError, TypeError):
            logger.error("Price and volume must be numeric values.")
            return False

        return True

    def process_queue(self, queue: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Processes a queue of raw crypto payloads, filtering out invalid ones."""
        validated_data = []
        for index, payload in enumerate(queue):
            if self.validate_payload(payload):
                payload["symbol"] = payload["symbol"].upper()
                payload["price"] = float(payload["price"])
                payload["volume"] = float(payload["volume"])
                validated_data.append(payload)
            else:
                logger.warning(f"Discarding invalid payload at index {index}")
        return validated_data