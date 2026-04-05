# memoize:To store result of computation so that it can be retrvied without repeating the computation.

from functools import lru_cache
import time

@lru_cache(maxsize=None)
def fn(x):
    time.sleep(5)
    return x*2

print(fn(5))
print("done for 5")
print(fn(2))
print("done for 2")


#while executing this does not compute again,instaed retrive value from already calculated.
print(fn(5))
print("done for 5")
print(fn(2))
print("done for 2")

print(fn(3))
print("done for 3")