import logging
import os
import sys
from config import LOG_DIR, LOG_FILE

# Configure the logging module

YELLOW = "\x1b[33;21m"
RED = "\x1b[31;21m"
RESET = "\x1b[0m"

class ColoredFormatter(logging.Formatter):
    """Custom formatter that adds colors to log levels"""
    
    COLORS = {
        'WARNING': YELLOW,
        'ERROR': RED,
        'CRITICAL': RED,
    }
    
    def format(self, record):
        # Get the original formatted message
        formatted = super().format(record)
        
        # Add color if this level has one defined
        if record.levelname in self.COLORS:
            color = self.COLORS[record.levelname]
            formatted = f"{color}{formatted}{RESET}"
        
        return formatted
    
class CustomLogger(logging.Logger):
    """Custom logger that uses ColoredFormatter"""
    
    def __init__(self, name, level=logging.NOTSET):
        super().__init__(name, level)
        self.setLevel(level)
        
        try:
            os.makedirs(LOG_DIR, exist_ok=True)
        except Exception as e:
            print(f"Failed to create log directory: {e}")
            sys.exit(1)
        
        # Create handlers
        console_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(LOG_FILE, mode="a", encoding="utf-8")
        
        # Create formatter and add it to the handlers
        colored_formatter = ColoredFormatter("{asctime} : {name} : {levelname} : {message}",
                                           style="{",
                                           datefmt="%d-%m-%Y %H:%M")
        plain_formatter = logging.Formatter("{asctime} : {name} : {levelname} : {message}",
                                          style="{",
                                          datefmt="%d-%m-%Y %H:%M")
        console_handler.setFormatter(colored_formatter)
        file_handler.setFormatter(plain_formatter)
        
        # Add handlers to the logger
        self.addHandler(console_handler)
        self.addHandler(file_handler)
        
def main():
    """Main function to demonstrate logging"""
    time_logging = CustomLogger("example_logger", level=logging.DEBUG)
    
    time_logging.debug("This is a debug message.")
    time_logging.info("This is an info message.")
    time_logging.warning("This is a warning message.")
    time_logging.error("This is an error message.")
    time_logging.critical("This is a critical message.")

if __name__ == "__main__":
    main()
