#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： tian
# datetime： 2022/11/17 9:48 PM 
# ide： PyCharm

"""
F(n) = F(n-1) + F(n-2)
1 1 2 3 5 8 ....n
"""

"""
重复计算导致慢
f(5) = f(4) + f(3)
f(4) = f(3) + f(2)
"""


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


# 动态规划思想DP
# 1. 最优子结构
# 2. 重复子问题
def no_recurision_fib(n):
    if n <= 2:
        return 1
    lis = [0, 1, 1]
    for i in range(n - 2):
        num = lis[-1] + lis[-2]
        lis.append(num)

    return lis[-1]


if __name__ == '__main__':
    print(fib(6))
    print(no_recurision_fib(6))
