import logging
import os
import sys
from config import LOG_DIR

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
        
        # Create a separate log file for each logger instance
        log_filename = f"{name}.log"
        log_filepath = os.path.join(LOG_DIR, log_filename)
        file_handler = logging.FileHandler(log_filepath, mode="a", encoding="utf-8")
        
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
    """Main function to demonstrate logging with multiple loggers"""
    # Create different loggers for different modules
    app_logger = CustomLogger("app_main", level=logging.DEBUG)
    auth_logger = CustomLogger("auth_module", level=logging.INFO)
    db_logger = CustomLogger("database", level=logging.DEBUG)
    
    # Demonstrate logging with different loggers
    app_logger.info("Application started")
    app_logger.debug("Debug information from main app")
    
    auth_logger.info("User authentication attempt")
    auth_logger.warning("Invalid login attempt detected")
    auth_logger.error("Authentication failed - too many attempts")
    
    db_logger.debug("Database connection established")
    db_logger.info("Database query executed successfully")
    db_logger.critical("Database connection lost!")
    
    app_logger.info("Application shutdown")
    
    print("\nLog files created:")
    print(f"- {LOG_DIR}/app_main.log")
    print(f"- {LOG_DIR}/auth_module.log") 
    print(f"- {LOG_DIR}/database.log")

if __name__ == "__main__":
    main()
