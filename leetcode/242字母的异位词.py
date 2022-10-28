#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@company:UDAI
@author:tianjian
@file:242字母的异位词.py
@time:2020/11/22

"""

"""
242. 有效的字母异位词
给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

示例 1:

输入: s = "anagram", t = "nagaram"
输出: true
示例 2:

输入: s = "rat", t = "car"
输出: false

"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        for s_, t_ in zip(sorted(s), sorted(t)):
            if s_ != t_:
                return False
        else:
            return True


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    solution = Solution()
    res = solution.isAnagram(s, t)
    print(res)
