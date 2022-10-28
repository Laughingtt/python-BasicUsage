# !/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@company:UDAI
@author:tianjian
@file:循环遍历多层数组.py
@time:2021/10/09

"""


def map_histograms_add_n2(array):
    for value in array:
        if isinstance(value, list):
            map_histograms_add_n2(value)
        else:
            if isinstance(value, PaillierEncryptedNumber):
                value.set_n_square()


map_histograms_add_n2(after_map_list)
