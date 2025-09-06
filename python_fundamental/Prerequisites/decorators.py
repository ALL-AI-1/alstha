import time
from functools import wraps

def logging_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling function '{func.__name__}' with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] Function '{func.__name__}' returned {result}")
        return result
    return wrapper

def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        print(f"[TIMER] Starting '{func.__name__}'...")
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed = end_time - start_time
        print(f"[TIMER] Function '{func.__name__}' executed in {elapsed:.6f} seconds")
        return result
    return wrapper

# Example usage:
@logging_decorator
@timing_decorator
def example_function(x, y):
    time.sleep(0.5)
    return x + y

# Uncomment to test:
example_function(5, 7)
