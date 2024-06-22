from .ib_api import IBAPI
from .logger import logger

def run_diagnostics():
    api = IBAPI()
    if not api.is_connected():
        logger.error("Diagnostic failed: Unable to connect to Interactive Brokers")
        return False
    logger.info("Connected to Interactive Brokers for diagnostics")
    test_symbol = "AAPL"
    metrics = api.get_options_interest(test_symbol)
    if metrics:
        logger.info(f"Retrieved options interest metrics for {test_symbol}")
        logger.info(metrics)
        api.disconnect()
        return True
    else:
        logger.error(f"Failed to retrieve options interest metrics for {test_symbol}")
        return False
