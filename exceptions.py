class CryptoTrackerError(Exception):
    """Base exception for all crypto-tracker-99 operations."""
    pass

class APIConnectionError(CryptoTrackerError):
    """Raised when external crypto API services are unreachable."""
    pass

class RateLimitExceeded(CryptoTrackerError):
    """Raised when API requests exceed threshold."""
    pass

class DataParsingError(CryptoTrackerError):
    """Raised when market data cannot be serialized or parsed."""
    pass

class InvalidTickerError(CryptoTrackerError):
    """Raised when an unsupported or malformed ticker is used."""
    pass

def handle_crypto_error(e: Exception) -> None:
    """Helper to format and re-raise custom exceptions."""
    if isinstance(e, CryptoTrackerError):
        print(f"[CryptoTracker-99 Error] {e.__class__.__name__}: {str(e)}")
    else:
        print(f"[Unexpected Error] {type(e).__name__}: {str(e)}")
    raise e