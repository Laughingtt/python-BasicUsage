#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： tian
# datetime： 2022/11/20 8:02 PM 
# ide： PyCharm

"""
输入：
3
2
2
1
复制
输出：
1
2
复制
说明：
输入解释：
第一个数字是3，也即这个小样例的N=3，说明用计算机生成了3个1到500之间的随机整数，接下来每行一个随机数字，共3行，也即这3个随机数字为：
2
2
1
所以样例的输出为：
1
2

"""
import sys


def random_sort():
    lis = []
    for line in sys.stdin:
        lis.append(int(line))
    uniq = set(lis[1:])
    for j in sorted(uniq):
        print(j)


random_sort()