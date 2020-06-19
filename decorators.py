'''
This File will work with a jupyter notebook for decorator demo
https://realpython.com/primer-on-python-decorators/#simple-decorators
'''

# Simple examples

def do_twice(func): # decorator functions takes func, just remember it
    def wrapper_do_twice():
        func()
        func()
    return wrapper_do_twice


def do_twice2(func):
    def wrapper_do_twice(*args, **kwargs): #make sure you add the *argrs and **kwargs to take in arguments
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice

############################################################################3
# More Advanced examples
# Starting from here, we will just put the decorator definition here
import functools
import time
import math

def decorator(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator


def timer(func):
    """Print the runtime of the decorated function"""
    @functools.wraps(func) # using this to aviod setting aside another file
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs") # this is interesting, the print out
        # looks like this:
        # Finished 'waste_some_time' in 0.0021 secs
        return value
    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])

def debug(func):
    """Print the function signature and return value"""
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {value!r}")
        return value
    return wrapper_debug


@debug
def make_greeting(name, age=None):
    if age is None:
        return f"Howdy {name}"
    else:
        return f"Whoa {name}! {age} already, you are growing up!"

# We can also ally a decorator to a standard library function
math.factorial = debug(math.factorial)

def approximate_e(terms=18):
    return sum(1 / math.factorial(n) for n in range(terms))



if __name__ == "__main__":
    waste_some_time(1)
    print('-' * 20)
    make_greeting("Ben", age=26)
    print('-' * 20)
    approximate_e(5)
