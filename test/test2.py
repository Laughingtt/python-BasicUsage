#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： tian
# datetime： 2022/11/26 10:59 AM 
# ide： PyCharm

import numpy as np


def cal_sum(lis, left, right):
    min_value = min(lis[left], lis[right])
    arr = np.array(lis[left + 1:right])
    arr = min_value - arr
    arr = arr[arr > 0]
    sum_value = arr.sum()

    return sum_value


if __name__ == '__main__':
    # print(cal_sum(lis=[1, 9, 6, 2, 5, 4, 9, 3, 7], left=1, right=6))
    print(cal_sum(lis=[1, 8, 6, 2, 5, 4, 8, 3, 7], left=1, right=8))
