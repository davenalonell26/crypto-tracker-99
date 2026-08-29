import logging
from logging.handlers import RotatingFileHandler
import os
from typing import Optional

# Constants for logger configuration in crypto tracker
LOG_DIRECTORY = "logs"
DEFAULT_LOG_FILENAME = "crypto_tracker.log"
DEFAULT_LOG_PATH = os.path.join(LOG_DIRECTORY, DEFAULT_LOG_FILENAME)
MAX_BYTES = 5 * 1024 * 1024  # 5 megabytes per log file
BACKUP_COUNT = 3  # Keep 3 backup files
LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

def create_log_directory(log_path: str) -> None:
    """Create the directory for log files if it does not exist."""
    log_dir = os.path.dirname(log_path)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

def get_rotating_file_handler(log_file: str, level: int) -> RotatingFileHandler:
    """Return a configured rotating file handler."""
    handler = RotatingFileHandler(
        log_file,
        maxBytes=MAX_BYTES,
        backupCount=BACKUP_COUNT,
        encoding="utf-8"
    )
    handler.setLevel(level)
    formatter = logging.Formatter(LOG_FORMAT, DATE_FORMAT)
    handler.setFormatter(formatter)
    return handler

def get_console_handler(level: int) -> logging.StreamHandler:
    """Return a configured console handler."""
    handler = logging.StreamHandler()
    handler.setLevel(level)
    formatter = logging.Formatter("%(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    return handler

def setup_logger(
    name: str = "crypto_tracker",
    log_file: Optional[str] = None,
    level: int = logging.INFO,
    console_level: int = logging.WARNING
) -> logging.Logger:
    """Set up and return a logger with rotating file handler.
    Suitable for tracking crypto prices and transactions.
    """
    if log_file is None:
        log_file = DEFAULT_LOG_PATH
    logger = logging.getLogger(name)
    # Prevent adding handlers multiple times
    if logger.hasHandlers():
        logger.setLevel(level)
        return logger
    logger.setLevel(level)
    create_log_directory(log_file)
    # Add rotating file handler
    file_handler = get_rotating_file_handler(log_file, level)
    logger.addHandler(file_handler)
    # Add console handler for important messages
    console_handler = get_console_handler(console_level)
    logger.addHandler(console_handler)
    logger.info("Rotating logger setup complete for crypto-tracker-99")
    return logger