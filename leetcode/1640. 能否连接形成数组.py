#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@company:UDAI
@author:tianjian
@file:1640. 能否连接形成数组.py
@time:2021/04/10

"""
"""
给你一个整数数组 arr ，数组中的每个整数 互不相同 。另有一个由整数数组构成的数组 pieces，其中的整数也 互不相同 。请你以 任意顺序 连接 pieces 中的数组以形成 arr 。但是，不允许 对每个数组 pieces[i] 中的整数重新排序。

如果可以连接 pieces 中的数组形成 arr ，返回 true ；否则，返回 false 。

 

示例 1：

输入：arr = [85], pieces = [[85]]
输出：true
"""


class Solution:
    def canFormArray(self, arr, pieces) -> bool:
        new_arr = []
        for i in arr:
            for j in pieces:
                if i != j[0]:
                    continue
                new_arr.extend(j)
        return arr == new_arr


if __name__ == '__main__':
    s = Solution()
    arr = [85]
    arr = [91, 4, 64, 78]
    arr = [1, 3, 5, 7]
    pieces = [[85]]
    pieces = [[78], [4, 64], [91]]
    pieces = [[2, 4, 6, 8]]
    print(s.canFormArray(arr, pieces))
