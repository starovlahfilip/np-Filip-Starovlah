
from functools import wraps
from time import perf_counter


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = perf_counter()

        try:
            return func(*args, **kwargs)
        finally:
            elapsed = perf_counter() - start
            print(f"[TIME] Vrijeme izvršavanja: {elapsed:.4f} sekundi")

    return wrapper
