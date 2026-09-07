"""Custom exception hierarchy for crypto-tracker-99."""

from typing import Optional


class CryptoTrackerError(Exception):
    """Base exception class for all errors raised by crypto-tracker-99."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message: str = message

    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] {self.message}"


class APIError(CryptoTrackerError):
    """Raised when an external cryptocurrency API request fails."""

    def __init__(self, message: str, endpoint: str, status_code: Optional[int] = None) -> None:
        super().__init__(message)
        self.endpoint: str = endpoint
        self.status_code: Optional[int] = status_code


class RateLimitExceededError(APIError):
    """Raised when API request limit is exceeded."""

    def __init__(self, endpoint: str, retry_after: int = 60) -> None:
        msg = f"Rate limit exceeded for endpoint '{endpoint}'. Retry after {retry_after}s."
        super().__init__(message=msg, endpoint=endpoint, status_code=429)
        self.retry_after: int = retry_after


class InvalidTickerError(CryptoTrackerError):
    """Raised when an unsupported or malformed ticker symbol is supplied."""

    def __init__(self, ticker: str) -> None:
        msg = f"Invalid or unknown crypto ticker symbol: '{ticker.upper()'}"
        super().__init__(message=msg)
        self.ticker: str = ticker.upper()


class ConfigurationError(CryptoTrackerError):
    """Raised when application configuration or API keys are invalid."""

    def __init__(self, setting_name: str, reason: str) -> None:
        msg = f"Configuration error for '{setting_name}': {reason}"
        super().__init__(message=msg)
        self.setting_name: str = setting_name
