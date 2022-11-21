"""
给你一个整数 n ，返回 和为 n 的完全平方数的最少数量 。
完全平方数 是一个整数，其值等于另一个整数的平方；换句话说，其值等于一个整数自乘的积。
例如，1、4、9 和 16 都是完全平方数，而 3 和 11 不是。
 
示例 1：
输入：n = 12

输出：3

解释：12 = 4 + 4 + 4
示例 2：
输入：n = 13

输出：2

解释：13 = 4 + 9 

"""
import copy
from math import log2, sqrt


def is_log2(number):
    log2_num = sqrt(number)
    if log2_num == int(log2_num):
        return True
    else:
        return False


"""
贪心算法，寻找每一次最大的平方根数
"""


def greed(n):
    sum_number = 0
    sum_times = 0
    tem_number = copy.deepcopy(n)
    while sum_number != n:
        if is_log2(tem_number):
            sum_number += tem_number
            tem_number = n - sum_number
            sum_times += 1
        else:
            tem_number -= 1
    return sum_times


if __name__ == '__main__':
    print(greed(13))
