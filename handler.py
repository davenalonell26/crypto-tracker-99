import logging

def validate_ticker(ticker):
    """Checks if ticker is a valid string and not empty."""
    if not isinstance(ticker, str) or not ticker.isalnum() or len(ticker) > 5:
        raise ValueError(f"Invalid ticker format: {ticker}")
    return ticker.upper()

def validate_amount(amount):
    """Ensures amount is a positive numeric value."""
    try:
        val = float(amount)
        if val <= 0:
            raise ValueError
        return val
    except (TypeError, ValueError):
        raise ValueError(f"Invalid amount: {amount}")

def run_processing_loop(data_queue):
    """Main loop for processing crypto transactions."""
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger("crypto-tracker-99")

    while True:
        task = data_queue.get()
        if task is None:
            break
        
        try:
            # Input validation layer
            ticker = validate_ticker(task.get('ticker'))
            amount = validate_amount(task.get('amount'))
            
            # Processing logic
            logger.info(f"Processing {amount} units of {ticker}")
            
        except ValueError as e:
            logger.error(f"Validation failed: {e}")
        except Exception as e:
            logger.exception(f"Unexpected error: {e}")