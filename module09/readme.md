# Lesson 09: Functions in Python - Decorators

In data engineering, code efficiency, reusability, and reliability are crucial. That's why we work with decorators.

**Using LOG**

When we want to understand more about our application, we have two alternatives.

- Use Print
- Use the Debugger

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

This example shows how to do basic logging with Loguru

```python
from loguru import logger

logger.info("This is an informational message")

# The output will be displayed in the console
```

#### Example 2: Log File Configuration

Here we configure Loguru to save log messages to a file, including file rotation based on size.

```python
from loguru import logger

# Configuring the log file with 5MB rotation
logger.add("my_app.log", rotation="5 MB")

logger.info("This message will be saved in the file")
```

In the example above, `logger.add()` is used to add a "sink" (destination) which, in this case, is a file. The `rotation` option determines that a new file will be created whenever the current one reaches 5MB.

#### Example 3: Capturing and saving

Here is an example of how to configure `loguru` to save logs both to a file and display them to standard output (`stderr`):

```python
from loguru import logger
from sys import stderr

# Logger configuration to display logs on stderr and save to file, with specific filtering and formatting
logger.add(
    sink=stderr,
    format="{time} <r>{level}</r> <g>{message}</g> {file}",
    level="INFO"
)

logger.add(
    "my_logs_file.log", # File where the logs will be saved
    format="{time} {level} {message} {file}",
    level="INFO"
)

# Example of using the logger
logger.info("This is an information log.")
logger.error("This is an error log.")
```

In this code, two "sinks" are added to the `logger`:

1. `stderr`, to display the logs, with specific formatting that includes time, log level, message and source file.

2. `"my_logs_file.log"`, to save the logs in a file with a format that also includes time, level, message and source file.

Log levels in Python (and many logging systems in other programming languages) are used to indicate the severity or importance of messages logged by the application. They help differentiate between types of information being logged, allowing for more effective filtering and analysis of log data. Here are the most common log levels, listed in order of increasing severity:

### DEBUG

* **Description**: The DEBUG level is used for detailed information, typically of interest only when diagnosing problems.
* **Use**: Developers use this level to obtain detailed information about application flow, state variables, and to understand how the code is operating during development and debugging.

### INFO

* **Description**: The INFO level is used to confirm that things are working as expected.
* **Use**: This level is generally the default in production for recording normal system events, such as startup processes, successfully completed operations, or other routine transactions.

### WARNING

* **Description**: The WARNING level indicates that something unexpected happened, or indicates a problem in the near future (e.g., 'disk almost full'). The software is working as expected.
* **Use**: This level is used to alert about situations that may require attention but do not prevent the system from functioning. For example, using an obsolete function or performance issues that do not require immediate action.

### ERROR

* **Description**: The ERROR level indicates that due to a more serious problem, the execution of some function or operation failed.
* **Use**: This level is used to log error events that affect the operation of a part of the system or functionality, but not necessarily the system as a whole. Errors that are caught and managed can still be logged at this level.

### CRITICAL

* **Description**: The CRITICAL level indicates a serious error that prevents the program from continuing to execute.
* **Use**: It is used for errors that require immediate attention, such as a critical system failure that can result in a complete stop of the service or application. This level should be reserved for the most serious problems.

### How to Use

Selecting the appropriate log level for different messages allows developers and system administrators to configure logs to capture only the information they need. For example, in a development environment, you may want to view all logs, from DEBUG to CRITICAL, to fully understand the application's behavior. In contrast, in a production environment, you can configure it to log only WARNING, ERROR, and CRITICAL, to reduce the volume of data generated and focus on issues that need attention.

#### Example 4: Catching Exceptions with Log

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

#### Example 5: Catching Exceptions with Log

Now, let's go to the decorator code:

```python
from loguru import logger
from sys import stderr
from functools import wraps

logger.remove()

logger.add(
                sink=stderr,
                format="{time} <r>{level}</r> <g>{message}</g> {file}",
                level="INFO"
            )

logger.add(
                "my_logs_file.log",
                format="{time} {level} {message} {file}",
                level="INFO"
            )

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Calling function '{func.__name__}' with args {args} and kwargs {kwargs}")
        try:
            result = func(*args, **kwargs)
            logger.info(f"Function '{func.__name__}' returned {result}")
            return result
        except Exception as e:
            logger.exception(f"Exception caught in '{func.__name__}': {e}")
            raise # Re-throw the exception so as not to change the behavior of the decorated function
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