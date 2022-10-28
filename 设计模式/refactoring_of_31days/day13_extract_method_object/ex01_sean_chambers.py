#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""

# 提取方法对象

"""
Today’s refactoring comes from Martin Fowlers list of refactorings. 
You can find his original article here with a brief description.

This is a more infrequent refactoring that I see myself using but it comes in handy at times. 
When trying to apply an Extract Method refactoring, and multiple methods are needing to be introduced, 
it is sometimes gets ugly because of multiple local variables that are being used within a method. 
Because of this reason, 
it is better to introduce an Extract Method Object refactoring and to segregate the logic required to perform the task.
"""


# 今天的重构来自于 Martin Fowler 的重构目录。
# 你可以在这里找到包含简介的原始文章。
# 在我看来，这是一个比较罕见的重构，但有时却终能派上用场。
# 当你尝试进行提取方法的重构时，需要引入大量的方法。
# 在一个方法中使用众多的本地变量有时会使代码变得丑陋。因此最好使用提取方法对象这个重构，将执行任务的逻辑分开。

class OrderLineItem:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self): return self.__price


class Order:
    def __init__(self, orderline_items, discounts, tax):
        self.orderline_items = orderline_items
        self.discounts = discounts
        self.tax = tax

    def calculate(self):
        subtotal = 0
        for orderline_item in self.orderline_items:
            subtotal += orderline_item.price
        for discount in self.discounts:
            subtotal -= discount
        tax = subtotal * self.tax
        grandtotal = subtotal + tax
        return grandtotal


"""
This entails passing a reference to the class that will be returning the computation to a new object 
that has the multiple methods via the constructor, 
or passing the individual parameters to the constructor of the method object. 
I will be showing the former here.
"""


# 我们通过构造函数，将返回计算结果的类的引用传递给包含多个计算方法的新建对象，或者向方法对象的构造函数中单独传递各个参数。
# 如下面的代码:


class OrderLineItem:
    def __init__(self, price):
        self.__price = price

    @property
    def price(self): return self.__price


class Order:
    def __init__(self, orderline_items, discounts, tax):
        self.orderline_items = orderline_items
        self.discounts = discounts
        self.tax = tax

    def calculate(self):
        return OrderCalculator(self).calculate()


class OrderCalculator:
    def __init__(self, order):
        self.subtotal = 0
        self.orderline_items = order.orderline_items
        self.discounts = order.discounts
        self.tax = order.tax

    def calculate(self):
        self.calculate_subtotal()
        self.calculate_discounts()
        self.calculate_tax()
        return self.subtotal

    def calculate_subtotal(self):
        for orderline_item in self.orderline_items:
            self.subtotal += orderline_item.price

    def calculate_discounts(self):
        for discount in self.discounts:
            self.subtotal -= discount

    def calculate_tax(self):
        self.subtotal += self.subtotal * self.tax
