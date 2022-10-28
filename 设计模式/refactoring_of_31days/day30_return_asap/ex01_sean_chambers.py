#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""

# 尽快返回

"""
This topic actually came up during the Remove Arrowhead Antipattern refactoring. 
The refactoring introduces this as a side effect to remove the arrowhead. 
To eliminate the arrowhead you return as soon as possible.
"""


# 该话题实际上是诞生于移除箭头反模式重构之中。
# 在移除箭头时，它被认为是重构产生的副作用。
# 为了消除箭头，你需要尽快地 return。

class Order:
    def __init__(self):
        self.__customer = None

    def calculate_order(self, customer, products, discount):
        self.__customer = customer
        order_total = 0
        if len(products):
            order_total = sum([p.price for p in products])
            if discount > 0:
                order_total -= discount
        return order_total


"""
The idea is that as soon as you know what needs to be done and you have all the required information, 
you should exit the method as soon as possible and not continue along.
"""


# 该重构的理念就是，当你知道应该处理什么并且拥有全部需要的信息之后，立即退出所在方法，不再继续执行。

class Order:
    def __init__(self):
        self.__customer = None

    def calculate_order(self, customer, products, discount):
        if len(products) == 0: return 0

        self.__customer = customer

        order_total = sum([p.price for p in products])

        if discount == 0: return order_total
        order_total -= discount
        return order_total
