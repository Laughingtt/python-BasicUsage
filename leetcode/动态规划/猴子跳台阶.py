
from functools import lru_cache
@lru_cache
def f(n):
    if n<3:
        return 1
    elif n==3:
        return 2
    elif n>3:
        return f(n-1)+f(n-3)

print(f(150))