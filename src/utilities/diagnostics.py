import time
import functools

def executionTime ():
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(f"{func.__name__}: {end - start}")
            return result
        return wrapper
    return decorator