# Python Logging Module

A custom Python logging module with colored console output and clean file logging.

## Features

- **Colored Console Output**: Different colors for different log levels (warnings in yellow, errors/critical in red)
- **Clean File Logging**: Plain text logs without color codes for better readability and compatibility
- **Separate Log Files**: Each logger instance creates its own log file based on the logger name
- **Logger Name Tracking**: Includes logger name in output for better identification
- **Configurable**: Easy to configure log directory through environment variables
- **Custom Logger Class**: Extends Python's built-in logging with automatic setup

## File Structure

```
├── config.py      # Configuration settings (LOG_DIR)
├── logs.py        # Main logging module
├── README.md      # This file
└── logs/          # Log directory (created automatically)
    ├── app_main.log      # Example log file for "app_main" logger
    ├── auth_module.log   # Example log file for "auth_module" logger
    └── database.log      # Example log file for "database" logger
```

## Installation

No external dependencies required. Uses only Python standard library.

## Configuration

The module uses configuration from `config.py`:

```python
import os

LOG_DIR = os.getenv("LOG_DIR", "./logs")  # Default: ./logs directory
```

**Log File Naming**: Each logger automatically creates its own log file based on the logger name:
- Logger named "app_main" → `logs/app_main.log`
- Logger named "database" → `logs/database.log`
- Logger named "auth_module" → `logs/auth_module.log`

You can override the log directory by setting the `LOG_DIR` environment variable:

```bash
export LOG_DIR="/path/to/your/logs"
```

## Usage

### Basic Usage

```python
from logs import CustomLogger
import logging

# Create logger instances - each gets its own log file
app_logger = CustomLogger("app_main", level=logging.DEBUG)        # → logs/app_main.log
auth_logger = CustomLogger("auth_module", level=logging.INFO)     # → logs/auth_module.log
db_logger = CustomLogger("database", level=logging.DEBUG)         # → logs/database.log

# Log messages at different levels
app_logger.debug("Debug message")
app_logger.info("Info message") 
app_logger.warning("Warning message")  # Yellow in console
app_logger.error("Error message")      # Red in console
app_logger.critical("Critical message") # Red in console
```

### Running the Demo

```bash
python logs.py
```

This will demonstrate all log levels with their respective colors in the console and create separate log files for each logger:
- `logs/app_main.log`
- `logs/auth_module.log`
- `logs/database.log`

## Output Examples

### Console Output (with colors)
All loggers output to the same console with colors:
```
14-07-2025 18:17 : app_main : INFO : Application started
14-07-2025 18:17 : app_main : DEBUG : Debug information from main app
14-07-2025 18:17 : auth_module : INFO : User authentication attempt
14-07-2025 18:17 : auth_module : WARNING : Invalid login attempt detected      # Yellow text
14-07-2025 18:17 : auth_module : ERROR : Authentication failed - too many attempts  # Red text
14-07-2025 18:17 : database : DEBUG : Database connection established
14-07-2025 18:17 : database : INFO : Database query executed successfully
14-07-2025 18:17 : database : CRITICAL : Database connection lost!              # Red text
```

### File Output (clean text, separate files)

**logs/app_main.log:**
```
14-07-2025 18:17 : app_main : INFO : Application started
14-07-2025 18:17 : app_main : DEBUG : Debug information from main app
14-07-2025 18:17 : app_main : INFO : Application shutdown
```

**logs/auth_module.log:**
```
14-07-2025 18:17 : auth_module : INFO : User authentication attempt
14-07-2025 18:17 : auth_module : WARNING : Invalid login attempt detected
14-07-2025 18:17 : auth_module : ERROR : Authentication failed - too many attempts
```

**logs/database.log:**
```
14-07-2025 18:17 : database : DEBUG : Database connection established
14-07-2025 18:17 : database : INFO : Database query executed successfully
14-07-2025 18:17 : database : CRITICAL : Database connection lost!
```

## Log Format

The current log format is: `{asctime} : {name} : {levelname} : {message}`

Where:
- `{asctime}`: Timestamp in DD-MM-YYYY HH:MM format
- `{name}`: Logger name (helps identify different loggers in multi-module applications)
- `{levelname}`: Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- `{message}`: The actual log message

## Color Scheme

| Log Level | Console Color | ANSI Code |
|-----------|---------------|-----------|
| DEBUG     | Default       | -         |
| INFO      | Default       | -         |
| WARNING   | Yellow        | `\x1b[33;21m` |
| ERROR     | Red           | `\x1b[31;21m` |
| CRITICAL  | Red           | `\x1b[31;21m` |

## Customization

### Adding More Colors

To add colors for other log levels, modify the `COLORS` dictionary in the `ColoredFormatter` class:

```python
COLORS = {
    'DEBUG': "\x1b[36;21m",    # Cyan
    'INFO': "\x1b[32;21m",     # Green
    'WARNING': YELLOW,
    'ERROR': RED,
    'CRITICAL': RED,
}
```

### Common ANSI Color Codes

- Black: `\x1b[30;21m`
- Red: `\x1b[31;21m`
- Green: `\x1b[32;21m`
- Yellow: `\x1b[33;21m`
- Blue: `\x1b[34;21m`
- Magenta: `\x1b[35;21m`
- Cyan: `\x1b[36;21m`
- White: `\x1b[37;21m`

### Changing Log Format

Modify the format string in the `CustomLogger` class:

```python
# Current format
colored_formatter = ColoredFormatter("{asctime} : {name} : {levelname} : {message}",
                                   style="{",
                                   datefmt="%d-%m-%Y %H:%M")

# Example: Add more details
colored_formatter = ColoredFormatter("{asctime} : {name} : {levelname} : {funcName}:{lineno} : {message}",
                                   style="{",
                                   datefmt="%d-%m-%Y %H:%M:%S")
```

## Classes

### `ColoredFormatter`
- Extends `logging.Formatter`
- Adds ANSI color codes to specified log levels
- Automatically resets colors after each message
- Maintains clean formatting for file output

### `CustomLogger`
- Extends `logging.Logger`
- Automatically sets up console and file handlers
- Uses colored formatter for console, plain formatter for file
- Creates log directory if it doesn't exist
- **Creates separate log file for each logger instance** (based on logger name)
- Includes logger name in all output for better tracking

## Multiple Loggers Example

When using multiple loggers, each creates its own log file while sharing the console output:

```python
# Create different loggers for different modules
auth_logger = CustomLogger("auth_module", level=logging.INFO)      # → logs/auth_module.log
db_logger = CustomLogger("database", level=logging.DEBUG)          # → logs/database.log
api_logger = CustomLogger("api_handler", level=logging.WARNING)    # → logs/api_handler.log

auth_logger.info("User logged in")           # Goes to console + auth_module.log
db_logger.debug("Database query executed")  # Goes to console + database.log
api_logger.warning("API rate limit approaching")  # Goes to console + api_handler.log
```

**Benefits of separate log files:**
- Easy to analyze logs from specific modules
- Reduced file size for each component
- Better organization for debugging
- Can set different log levels for different components

## Best Practices

1. **Use descriptive logger names**: Use meaningful names like "database", "auth", "api" instead of generic names
2. **Use appropriate log levels**: DEBUG for development, INFO for general information, WARNING for potential issues, ERROR for errors, CRITICAL for serious problems
3. **Don't log sensitive information**: Avoid logging passwords, API keys, or personal data
4. **Use structured logging**: Include relevant context in your log messages
5. **Rotate log files**: Consider implementing log rotation for production environments

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `LOG_DIR` | Directory for log files | `./logs` |

## License

This module is provided as-is for educational and development purposes.
