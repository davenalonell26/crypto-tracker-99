from typing import Any, Dict, Optional

def validate_crypto_payload(data: Any) -> bool:
    """Ensures incoming crypto data contains required fields."""
    required_fields = {'symbol', 'price', 'timestamp'}
    
    if not isinstance(data, dict):
        return False
    
    return all(field in data for field in required_fields)

def sanitize_price(price: Any) -> Optional[float]:
    """Converts price to float and validates positive value."""
    try:
        value = float(price)
        return value if value >= 0 else None
    except (TypeError, ValueError):
        return None

def validate_ticker_format(symbol: str) -> bool:
    """Validates ticker symbols follow standard format."""
    if not isinstance(symbol, str) or len(symbol) < 2:
        return False
    return symbol.isalnum() and symbol.isupper()

def normalize_crypto_data(data: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Aggregates and cleans raw dictionary data."""
    if not validate_crypto_payload(data):
        return None
        
    clean_price = sanitize_price(data['price'])
    if clean_price is None or not validate_ticker_format(data['symbol']):
        return None
        
    return {
        'symbol': data['symbol'].upper(),
        'price': clean_price,
        'timestamp': data['timestamp']
    }