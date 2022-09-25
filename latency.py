import time
from typing import Callable


def time_func(function: Callable):
    def run_func(*args, **kwargs):
        start_time = time.time()
        value = function(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)
        return value

    return run_func()


        