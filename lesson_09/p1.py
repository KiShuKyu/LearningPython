# Timing Function Execution
# Write a decorator that measures the time a function takes to execute.

import time


def timer(fn):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = fn(*args, **kwargs)
        end = time.time()
        print(f"{fn.__name__} ran in {end-start} time")
        return result
    return wrapper  # for decorator


@timer
def example_fn(n):
    time.sleep(n)


example_fn(2)
