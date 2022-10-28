#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@company:UDAI
@author:tianjian
@file:763划分字母.py
@time:2021/01/17

"""


def partitionLabels(S: str):
    """
    解题思路：先把字符串中的字母最后的Index记录起来，循环的去变量字符串，先暂定首字
    母的最大index为阈值，如果在这个阈值内，有超过范围内的往后移，并且当前区间内的字母遍历完时，
    此区间就定下来了
    """
    dic = {s: index for index, s in enumerate(S)}
    j = dic[S[0]]
    result = []
    num = 0
    for index, i in enumerate(S):
        num += 1
        if dic[i] < j:
            pass
        else:
            j = dic[i]
            if index == j:
                result.append(num)
                num = 0
    return result


if __name__ == '__main__':
    partitionLabels(S="ababcbacadefegdehijhklij")
