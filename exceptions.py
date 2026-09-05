from typing import Optional

class CryptoTrackerError(Exception):
    """Base exception for the crypto-tracker-99 application."""
    def __init__(self, message: str, code: Optional[int] = None) -> None:
        super().__init__(message)
        self.code = code

class APIConnectionError(CryptoTrackerError):
    """Raised when the crypto exchange API is unreachable."""
    pass

class DataValidationError(CryptoTrackerError):
    """Raised when incoming market data fails schema validation."""
    pass

class RateLimitExceeded(CryptoTrackerError):
    """Raised when API request limits are reached."""
    def __init__(self, message: str = "API rate limit exceeded", retry_after: int = 60) -> None:
        super().__init__(message, code=429)
        self.retry_after = retry_after

class ConfigurationError(CryptoTrackerError):
    """Raised when environment or config settings are missing."""
    pass