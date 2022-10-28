# 0,1,1,2,3,5,8,13.......

from functools import lru_cache


@lru_cache
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)


print(fib(100))
