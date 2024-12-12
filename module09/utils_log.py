# Importing libs
from sys import stderr
from loguru import logger
from functools import wraps

# Remove the default logger configuration
logger.remove()
logger.add(stderr, format="{time} {level} {message}", level="INFO")
logger.add("logs_file_info.log", format="{time} {level} {message} {file}", level="INFO")
logger.add("logs_file_critical.log", format="{time} {level} {message} {file}", level="ERROR")

# Add a logger configuration to write general logs to "logs_file_info.log"
logger.add(
    "logs_file_info.log",               # File to save logs
    format="{time} {level} {message} {file}",  # Format of the log entry
    level="INFO"                   # Minimum logging level to record
)

# Add another logger configuration to write critical/error logs to "logs_file_critical.log"
logger.add(
    "logs_file_critical.log",     # File to save critical logs
    format="{time} {level} {message} {file}",  # Format of the log entry
    level="ERROR"                  # Minimum logging level to record
)

# Define a decorator to add logging to functions
def log_decorator(func):
    """
    A decorator to add logging for function calls and exceptions.

    Logs:
    - Function name, arguments, and keyword arguments when the function is called.
    - Return value when the function successfully completes.
    - Exceptions raised by the function, with detailed traceback.
    """
    @wraps(func)  # Preserve the metadata (e.g., function name) of the decorated function
    def wrapper(*args, **kwargs):
        # Log the function call with its arguments and keyword arguments
        logger.info(f"Calling function '{func.__name__}' with args {args} and kwargs {kwargs}")
        try:
            # Call the actual function and log its return value
            result = func(*args, **kwargs)
            logger.info(f"Function '{func.__name__}' returns {result}")
            return result
        except Exception as e:
            # Log any exception that occurs during the function execution
            logger.exception(f"Exception caught in '{func.__name__}': {e}")
            raise  # Re-throw the exception so the behavior of the function isn't altered
    return wrapper  # Return the decorated function
