#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： tian
# datetime： 2022/11/17 10:21 PM 
# ide： PyCharm

price_lis = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

"""
最优值 = max(p_n,r1+r_n-1....)
"""
import time


def cal_time(fn):
    def wapper(*args, **kwargs):
        t0 = time.time()
        res = fn(*args, **kwargs)
        t1 = time.time()
        print("function {},time is {}s".format(fn.__name__, t1 - t0))
        return res

    return wapper


# 找出n个长度的锯条，无论怎么切割都是最大的值


# 递推式
@cal_time
def find_max_price(price_lis, length_n):
    if length_n == 0:
        return 0
    else:
        # 最大价值 = max(p_n,r1+r_n-1....)
        # 不切割时的价值是多少
        max_res = price_lis[length_n]
        # 逐一来切的价值是多少
        for i in range(1, length_n):
            max_res = max(max_res, find_max_price(price_lis, i) + find_max_price(price_lis, length_n - i))
        return max_res


# 递推式2 切割点左边的值不动，右边查找，相当于少了一次递归
# 最大价值 = max(p_i+r_n-i)
@cal_time
def find_max_price2(price_lis, length_n):
    if length_n == 0:
        return 0
    else:
        max_res = 0
        for i in range(1, length_n + 1):
            max_res = max(max_res, price_lis[i] + find_max_price2(price_lis, length_n - i))
        return max_res


@cal_time
def find_max_price_dp(price_lis, length_n):
    res_lis = [0] * (length_n + 1)
    cut_lis = [0] * (length_n + 1)  # 切割次数，保存每一次切割时左边留下的长度
    for sub_n in range(1, length_n + 1):
        max_res = 0
        sub_left = 0
        for block_n in range(1, sub_n + 1):
            if price_lis[block_n] + res_lis[sub_n - block_n] > max_res:
                max_res = price_lis[block_n] + res_lis[sub_n - block_n]
                sub_left = block_n
        res_lis[sub_n] = max_res
        cut_lis[sub_n] = sub_left
    print("cut_lis ", cut_lis)
    return res_lis[length_n]


if __name__ == '__main__':
    # print(find_max_price(price_lis, 10))
    # print(find_max_price2(price_lis, 10))
    print(find_max_price_dp(price_lis, 10))
