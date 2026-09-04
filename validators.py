from typing import Any, Dict, Optional

def validate_crypto_data(data: Any) -> bool:
    """verify crypto market data structure and types"""
    required_fields = ['symbol', 'price', 'volume']
    
    if not isinstance(data, dict):
        return False

    # ensure all fields exist and types are valid
    try:
        for field in required_fields:
            if field not in data:
                return False
        
        if not isinstance(data['symbol'], str):
            return False
        if not isinstance(data['price'], (int, float)) or data['price'] < 0:
            return False
        if not isinstance(data['volume'], (int, float)) or data['volume'] < 0:
            return False
            
        return True
    except (KeyError, TypeError):
        return False

def sanitize_symbol(symbol: str) -> Optional[str]:
    """normalize trading pair strings"""
    if not symbol or not isinstance(symbol, str):
        return None
        
    clean_symbol = symbol.strip().upper()
    if len(clean_symbol) < 2:
        return None
        
    return clean_symbol