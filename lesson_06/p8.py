# Functions with **kwargs
def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_kwargs(name="Vishal", hobby="Sleeping")
print_kwargs(name="Krishna")
print_kwargs(name="Jeet", hobby="LooksMaxing", enemy="Isshin")
