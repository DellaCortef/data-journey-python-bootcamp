from utils_log import log_decorator
from timer_decorator import time_measure_decorator

@log_decorator
@time_measure_decorator
def sum(x, y):
    print(f"Sum function called with {x} and {y}")  # Debugging print
    return x + y

sum(2, 3)
sum(2, 7)