# Debugginf Function calls
# create a decorator to print the function name and the values of its arguments every time the function is called.

def debug(fn):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())
        print(
            f"calling: {fn.__name__} with args {args_value} and kwargs {kwargs_value}")
        return fn(*args, **kwargs)
    return wrapper


@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")


greet("chai", greeting="yolo")
