import time

def timer(func):
    def wrapper (*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} ran in time {end-start}")
        return result
    return wrapper

@timer
def new_func(n):
    time.sleep(n)

new_func(2)


@timer
def func2(n):
    time.sleep(n)
    return "Hello"

func2(4)