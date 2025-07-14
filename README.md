# Python Logging Module

A custom Python logging module with colored console output and clean file logging.

## Features

- **Colored Console Output**: Different colors for different log levels (warnings in yellow, errors/critical in red)
- **Clean File Logging**: Plain text logs without color codes for better readability and compatibility
- **Logger Name Tracking**: Includes logger name in output for better identification
- **Configurable**: Easy to configure log directory and file names through environment variables
- **Custom Logger Class**: Extends Python's built-in logging with automatic setup

## File Structure

```
├── config.py      # Configuration settings
├── logs.py        # Main logging module
└── README.md      # This file
```

## Installation

No external dependencies required. Uses only Python standard library.

## Configuration

The module uses configuration from `config.py`:

```python
import os

LOG_DIR = os.getenv("LOG_DIR", "./logs")  # Default: ./logs directory
LOG_FILE = os.path.join(LOG_DIR, "script.log")  # Log file path
```

You can override the log directory by setting the `LOG_DIR` environment variable:

```bash
export LOG_DIR="/path/to/your/logs"
```

## Usage

### Basic Usage

```python
from logs import CustomLogger
import logging

# Create a logger instance
logger = CustomLogger("my_app", level=logging.DEBUG)

# Log messages at different levels
logger.debug("Debug message")
logger.info("Info message") 
logger.warning("Warning message")  # Yellow in console
logger.error("Error message")      # Red in console
logger.critical("Critical message") # Red in console
```

### Running the Demo

```bash
python logs.py
```

This will demonstrate all log levels with their respective colors in the console and create clean log entries in the file.

## Output Examples

### Console Output (with colors)
```
14-07-2025 16:37 : example_logger : DEBUG : This is a debug message.
14-07-2025 16:37 : example_logger : INFO : This is an info message.
14-07-2025 16:37 : example_logger : WARNING : This is a warning message.    # Yellow text
14-07-2025 16:37 : example_logger : ERROR : This is an error message.       # Red text
14-07-2025 16:37 : example_logger : CRITICAL : This is a critical message.  # Red text
```

### File Output (clean text)
```
14-07-2025 16:37 : example_logger : DEBUG : This is a debug message.
14-07-2025 16:37 : example_logger : INFO : This is an info message.
14-07-2025 16:37 : example_logger : WARNING : This is a warning message.
14-07-2025 16:37 : example_logger : ERROR : This is an error message.
14-07-2025 16:37 : example_logger : CRITICAL : This is a critical message.
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
- Includes logger name in all output for better tracking

## Multiple Loggers Example

When using multiple loggers, the name parameter helps distinguish between them:

```python
# Create different loggers for different modules
auth_logger = CustomLogger("auth_module", level=logging.INFO)
db_logger = CustomLogger("database", level=logging.DEBUG)
api_logger = CustomLogger("api_handler", level=logging.WARNING)

auth_logger.info("User logged in")
db_logger.debug("Database query executed")
api_logger.warning("API rate limit approaching")
```

Output:
```
14-07-2025 16:37 : auth_module : INFO : User logged in
14-07-2025 16:37 : database : DEBUG : Database query executed
14-07-2025 16:37 : api_handler : WARNING : API rate limit approaching
```

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
