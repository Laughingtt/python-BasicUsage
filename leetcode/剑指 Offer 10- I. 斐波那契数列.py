#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@company:UDAI
@author:tianjian
@file:剑指 Offer 10- I. 斐波那契数列.py
@time:2020/11/22

"""
"""

写一个函数，输入 n ，求斐波那契（Fibonacci）数列的第 n 项。斐波那契数列的定义如下：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
斐波那契数列由 0 和 1 开始，之后的斐波那契数就是由之前的两数相加而得出。
"""


class Solution:
    def fib(self, n: int) -> int:
        ####标准递归解法：
        # if n==0:return 0
        # if n==1:return 1
        # return (self.fib(n-1)+self.fib(n-2))%1000000007

        ####带备忘录的递归解法
        # records = [-1 for i in range(n+1)] # 记录计算的值
        # if n == 0:return 0
        # if n == 1:return 1
        # if records[n] == -1: # 表明这个值没有算过
        #     records[n] = self.fib(n-1) +self.fib(n-2)
        # return records[n]
        # 递归输出超时,用记忆化递归规划，时间上优越很多。

        ###DP方法：解决记忆化递归费内存的问题
        dp = {}
        dp[0] = 0
        dp[1] = 1
        if n >= 2:
            for i in range(2, n + 1):
                dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n] % 1000000007

        ###最优化DP方法：
        # a, b = 0, 1
        # for _ in range(n):
        #     a, b = b, a + b
        # return a % 1000000007


if __name__ == '__main__':
    solution = Solution()
    res = solution.fib(37)
    print(res)
