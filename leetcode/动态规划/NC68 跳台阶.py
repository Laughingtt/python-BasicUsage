#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： tian
# datetime： 2022/11/20 8:24 PM 
# ide： PyCharm


# 递归
def jump_step(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return jump_step(n - 1) + jump_step(n - 2)


# 动态规划
def jump_step2(n):
    step_list = [0, 1, 2]
    if n < 3:
        return step_list[n]
    for i in range(3, n + 1):
        step_sum = step_list[i - 1] + step_list[i - 2]
        step_list.append(step_sum)
    return step_list[n]


res = jump_step2(7)
print(res)
