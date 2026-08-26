"""Custom exceptions for crypto-tracker-99.

This module centralizes exception definitions for better organization after cleanup.
"""

class CryptoTrackerError(Exception):
    """Base class for all crypto tracker exceptions."""
    pass


class APIError(CryptoTrackerError):
    """Exception raised for errors during API interactions."""

    def __init__(self, message, status_code=None):
        super().__init__(message)
        self.status_code = status_code

    def __str__(self):
        base = super().__str__()
        if self.status_code:
            return f"{base} (HTTP {self.status_code})"
        return base


class InvalidCoinError(CryptoTrackerError):
    """Exception raised for invalid cryptocurrency identifiers."""
    pass


class RateLimitError(APIError):
    """Exception raised when rate limit is hit."""
    pass


class AuthError(APIError):
    """Exception raised on authentication failure."""
    pass


class ParseError(CryptoTrackerError):
    """Exception raised on data parsing failure."""
    pass


class NetworkError(CryptoTrackerError):
    """Exception raised on network issues."""
    pass


def create_api_error(status_code, message="Request failed"):
    """Factory function to create appropriate API error."""
    if status_code == 429:
        return RateLimitError(message, status_code)
    if status_code in (401, 403):
        return AuthError(message, status_code)
    if 400 <= status_code < 500:
        return APIError(message, status_code)
    if 500 <= status_code < 600:
        return APIError(message, status_code)
    return APIError(message, status_code)