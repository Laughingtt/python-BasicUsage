#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@company:UDAI
@author:tianjian
@file:子数列求个数.py
@time:2021/02/28

"""

count = 0
# A = [1, 2, 1, 2, 3]
# k = 2

# A = [1,2,1,3,4]
# k = 3

A = [1, 2]
k = 1

for idx in range(len(A)):
    for jdx in range(idx + 1, len(A) + 1):
        array = A[idx:jdx]
        print(array)
        if len(set(array)) == k:
            count += 1
        else:
            continue
print(count)
