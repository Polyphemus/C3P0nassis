'''Decorator tutorial from https://realpython.com/primer-on-python-decorators/'''

import functools
import time
import math
import random

def do_twice(func): #decorator is passed a function, returns modified function
    @functools.wraps(func) ##  uses functools.update_wrapper(),updates attributes (__name__, __doc__), used in introspection
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice

def say_whee():
    print("Whee!")

say_whee = do_twice(say_whee)

@do_twice
def greet(name):
    print(f"Hello {name}")

@do_twice
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"

say_whee()
print(say_whee.__name__)
greet('Jon')
print(return_greeting('bot'))


def timer(func):
    """Prints the runtime of the decorated function"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs") # !r flag calls repr() on value (normal behavior is to call __format__ method of value itself
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

waste_some_time(5)

def debug(func):
    """Print the function signature and return value. Function signature (or type signature, or method signature) defines
     input and output of functions or methods. A signature can include: parameters and their types. a return value and type"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]                      # Create a list of the positional arguments. Use repr() to get a nice string representing each argument
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # Create a list of the keyword arguments
        signature = ", ".join(args_repr + kwargs_repr)           # join above lists
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")           # return value is printed after the function is executed
        return value
    return wrapper_debug

# Apply a decorator to a standard library function
math.factorial = debug(math.factorial)

def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))  # generator expression

print(approximate_e(5))


'''Decorators can also simply register that a function exists and return it unwrapped.
This can be used, for instance, to create a light-weight plug-in architecture:'''

PLUGINS = dict()

def register(func):
    """Register a function as a plug-in"""
    PLUGINS[func.__name__] = func
    return func

@register
def say_hello(name):
    return f"Hello {name}"

@register
def be_awesome(name):
    return f"Yo {name}, together we are the awesomest!"

def randomly_greet(name):
    greeter, greeter_func = random.choice(list(PLUGINS.items()))
    print(f"Using {greeter!r}")
    return greeter_func(name)

print(randomly_greet('Jon'))
