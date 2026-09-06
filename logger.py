import logging
import os
from logging.handlers import RotatingFileHandler

def setup_logger(name: str = 'crypto-tracker-99') -> logging.Logger:
    """Configures a rotating file logger for crypto tracking operations."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Ensure logs directory exists
    log_dir = 'logs'
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Rotation settings: 5MB per file, keep 3 backups
    log_file = os.path.join(log_dir, 'app.log')
    handler = RotatingFileHandler(
        log_file, 
        maxBytes=5*1024*1024, 
        backupCount=3
    )

    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    handler.setFormatter(formatter)

    if not logger.handlers:
        logger.addHandler(handler)
        # Also output to console for development visibility
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    return logger

# Instance for global application usage
tracker_logger = setup_logger()