"""A small decorator that measures how long a function takes to run."""

from functools import wraps
from time import perf_counter


def measure_time(function):
    """Print elapsed time while preserving the wrapped function's metadata."""

    @wraps(function)
    def wrapper(*args, **kwargs):
        started = perf_counter()
        try:
            return function(*args, **kwargs)
        finally:
            elapsed = perf_counter() - started
            print(f"{function.__name__} took {elapsed:.6f} seconds")

    return wrapper


@measure_time
def calculate_sum(limit):
    return sum(range(limit))


if __name__ == "__main__":
    print("Result:", calculate_sum(1_000_000))
