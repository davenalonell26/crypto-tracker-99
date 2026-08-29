import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

# Directory and file settings for crypto tracker logs
LOG_DIR = Path("logs")
LOG_FILE = LOG_DIR / "crypto_tracker.log"
MAX_LOG_SIZE_BYTES = 5 * 1024 * 1024  # 5 MB per file
BACKUP_COUNT = 3
DEFAULT_LOG_LEVEL = logging.INFO

def setup_logger(name: str = "crypto_tracker") -> logging.Logger:
    """Set up a logger with console and rotating file handlers."""
    # Create logs directory if it does not exist
    LOG_DIR.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(name)
    logger.setLevel(DEFAULT_LOG_LEVEL)

    # Remove any existing handlers to prevent duplicate logs
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    # Define log message format
    log_format = logging.Formatter(
        "%(asctime)s [%(levelname)s] %(name)s: %(message)s"
    )

    # Add console handler for real-time output
    console_handler = logging.StreamHandler()
    console_handler.setLevel(DEFAULT_LOG_LEVEL)
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)

    # Add rotating file handler for persistent logs with rotation
    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=MAX_LOG_SIZE_BYTES,
        backupCount=BACKUP_COUNT,
        encoding="utf-8"
    )
    file_handler.setLevel(DEFAULT_LOG_LEVEL)
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)

    return logger

# Initialize the main logger for the application
logger = setup_logger()