# Class 08: Functions in Python - ETL with Pandas, JSON and Parquet

To perform a simple ETL (Extract, Transform, Load) using Python and the Pandas library, we will follow the following steps:

Extract: Read data from a JSON file.

Transform: Concatenate the extracted data into a single DataFrame and apply a transformation. The specific transformation will depend on the data, but let's assume a simple operation as an example.

Load: Save the resulting DataFrame to a CSV or PARQUET file. 

**Using LOG**

## Content

Loguru is a logging library for Python that aims to bring a simpler and more powerful user experience than Python's standard logging module. With a simple API, Loguru offers several useful features, such as file rotation, JSON serialization, sending messages to multiple destinations, and much more, all without the need for complicated initial configuration.

### What is Logging?

Logging is the process of recording messages that document events that occur during the execution of software. These messages may indicate execution progress, failures, errors, or other useful information. Logging is crucial for software development and maintenance, as it allows developers and system administrators to understand what the application is doing, diagnose problems, and monitor performance in production.

### How to Use Loguru

To start using Loguru, you first need to install it. This can be done easily via pip:

```bash
poetry add loguru
```

Now, let's look at examples of how to use Loguru in your Python code.

#### Example 1: Basic Logging

This example shows how to do basic logging with Loguru, including messages of different severity levels.

```python
from loguru import logger

# Log messages of different levels
logger.debug("This is a debug message")
logger.info("This is an informational message")
logger.warning("This is a warning")
logger.error("This is an error")
logger.critical("This is critical")

# The output will be displayed in the console
```

In this example, we use the `logger` imported from Loguru to log messages of different severity levels. Loguru takes care of formatting and displaying these messages in the console, by default.

#### Example 2: Log File Configuration

Here we configure Loguru to save log messages to a file, including file rotation based on size.

```python
from loguru import logger

# Configuring the log file with 5MB rotation
logger.add("my_app.log", rotation="5 MB")

logger.info("This message will be saved in the file")
```

In the example above, `logger.add()` is used to add a "sink" (destination) which, in this case, is a file. The `rotation` option determines that a new file will be created whenever the current one reaches 5MB.

#### Example 3: Catching Exceptions with Log

Loguru also makes exception logging easier by automatically capturing traceback information.

```python
from loguru import logger

def my_function():
    raise ValueError("An error occurred!")

try:
    my_function()
exceptException:
    logger.exception("An exception was caught")
```

Using `logger.exception()`, Loguru automatically captures and logs the exception traceback, which is extremely useful for error diagnosis.

Let's create a decorator using Loguru to automatically add logs to any Python function. This allows us to automatically record when a function is called and when it terminates, along with any relevant information such as function arguments and the result returned (or exception thrown).

Now, let's go to the decorator code:

```python
from loguru import logger

def log_decorator(func):
    def wrapper(*args, **kwargs):
        logger.info(f"Calling '{func.__name__}' with {args} and {kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"'{func.__name__}' returned {result}")
            return result
        except Exception as e:
            logger.exception(f"'{func.__name__}' threw an exception: {e}")
            raise
    return wrapper
```

In this decorator, `log_decorator`, we use `logger.info` to log when the decorated function is called and what it returns. If an exception is thrown, we use `logger.exception` to log the exception, including traceback.

### How to Use the Decorator

Now, see how to apply `log_decorator` to a function:

```python
@log_decorator
def sum(a, b):
    return a + b

@log_decorator
def failure():
    raise ValueError("An intentional error")

# Testing the decorated functions
sum(5, 3) # This will log the call and return
try:
    failure() # This will log the call and the exception
except ValueError:
    pass # Ignore the exception for demonstration purposes
```

By decorating the `sum` and `fail` functions with `@log_decorator`, we automatically log the input and output (or exception) of these functions without changing their body. This is especially useful for debugging, monitoring application performance, or simply keeping track of which functions are being called and with what arguments.

### Benefits of Using Decorators with Loguru

Using decorators in conjunction with Loguru provides an elegant and powerful approach to adding logs to Python applications. Without needing to modify the function body, we can easily add logging functionality, which makes the code cleaner, maintains separation of concerns, and makes maintenance and debugging easier.

Furthermore, by centralizing logging logic in the decorator, we promote code reuse and ensure a consistent way of logging information across different parts of an application.

### Conclusion

Loguru offers a modern and convenient approach to logging in Python, simplifying many aspects that require detailed manual configuration with Python's standard logging module. Whether for development, debugging, or production, adding logging to your application with Loguru can significantly improve the visibility and diagnostics of your code.

### Challenge