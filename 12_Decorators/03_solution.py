import time

def cache(func):
    cache_value = {}
    print(cache_value)
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        return result
    return wrapper




@cache
def number(a, b):
    time.sleep(4)
    return a + b

print(number(3, 4))
print(number(3, 4))
print(number(5, 6))
print(number(5, 6))

