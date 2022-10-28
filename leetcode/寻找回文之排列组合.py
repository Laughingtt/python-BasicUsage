# !/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@company:UDAI
@author:tianjian
@file:1.py
@time:2022/04/28

"""

import copy


def is_huiwen(s):
    a = len(s)
    i = 0
    count = 1
    while i <= (a / 2):
        if s[i] == s[a - i - 1]:
            count = 1
            i += 1
        else:
            return False
    return True


def replace_str(ss):
    ss = list(ss)
    c = ss.count("?")
    letter = "abcdefz"
    for i in letter:
        s = copy.deepcopy(ss)
        for j in range(c):
            ss_index = s.index("?")
            s[ss_index] = i
            str_s = "".join(s)
        if is_huiwen(str_s):
            return True
    return False


if __name__ == '__main__':
    print(replace_str("?a?"))
