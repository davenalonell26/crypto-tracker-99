from typing import Dict, Any, Optional

def format_crypto_amount(amount: float, symbol: str, decimals: int = 4) -> str:
    """Format cryptocurrency amount with appropriate decimal precision and symbol."""
    if amount is None:
        return f"0.0000 {symbol}"
    
    format_string = f"{{:.{decimals}f}}"
    formatted_number = format_string.format(amount)
    return f"{formatted_number} {symbol.upper()}"

def calculate_price_change(current_price: float, previous_price: float) -> Optional[Dict[str, Any]]:
    """Calculate absolute and percentage price change between two data points."""
    if not previous_price or previous_price == 0:
        return None
        
    price_difference = current_price - previous_price
    percentage_change = (price_difference / previous_price) * 100
    
    return {
        "absolute_change": round(price_difference, 8),
        "percentage_change": round(percentage_change, 2),
        "is_positive": price_difference >= 0
    }

def sanitize_ticker(ticker: str) -> str:
    """Clean and normalize cryptocurrency ticker symbols."""
    if not ticker:
        return ""
    return ticker.strip().upper().replace("/", "-")
