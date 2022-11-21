#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： tian
# datetime： 2022/11/17 9:06 PM 
# ide： PyCharm


"""
有n个非负整数，将其按照字符串方式拼接，如何拼接使得数字最大
"""


def find_max_number(numer_lis):
    numer_lis = list(map(str, numer_lis))

    # 冒泡排序
    for i in range(len(numer_lis)):
        for j in range(i + 1, len(numer_lis)):
            if numer_lis[i] + numer_lis[j] < numer_lis[j] + numer_lis[i]:
                temp = numer_lis[i]
                numer_lis[i] = numer_lis[j]
                numer_lis[j] = temp
    print(numer_lis)


if __name__ == '__main__':
    find_max_number([22, 442, 123, 534, 223])
