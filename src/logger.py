import logging
from logging.handlers import RotatingFileHandler

def setup_logger():
    logger = logging.getLogger('OptionsInterestApp')
    logger.setLevel(logging.DEBUG)
    
    # Create a file handler for logging to a file
    file_handler = RotatingFileHandler('logs/app.log', maxBytes=2000, backupCount=5)
    file_handler.setLevel(logging.DEBUG)
    
    # Create a console handler for logging to the console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    
    # Create a formatter and set it for both handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    
    # Add both handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger

logger = setup_logger()
