#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""

# 提取方法

"""
Today we look at the Extract Method refactoring. This is an extremely easy refactoring with several benefits. 
First, it helps to make code more readable by placing logic behind descriptive method names. 
This reduces the amount of investigation the next developer needs to do as a method name can describe what a portion of code is doing. 
This in turn reduces bugs in the code because less assumptions need to be made. 
Here’s some code before we apply the refactoring:
"""


# 这个重构极其简单但却大有裨益。
# 首先，将逻辑置于命名良好的方法内有助于提高代码的可读性。
# 当方法的名称可以很好地描述这部分代码的功能时，可以有效地减少其他开发者的研究时间。
# 假设越少，代码中的 bug 也就越少。重构之前的代码如下:

class Receipt:
    def __init__(self, discounts, itemtotals):
        self.discounts = discounts
        self.itemtotals = itemtotals

    def calculate_grandtotal(self):
        subtotal = 0
        for itemtotal in self.itemtotals:
            subtotal += itemtotal
        if len(self.discounts):
            for discount in self.discounts:
                subtotal -= discount
        tax = subtotal * 0.065
        subtotal += tax
        return subtotal


"""
You can see that the CalculateGrandTotal method is actually doing three different things here. 
It’s calculating the subtotal, applying any discounts and then calculating the tax for the receipt. 
Instead of making a developer look through that whole method to determine what each thing is doing, 
it would save time and readability to seperate those distinct tasks into their own methods like so
"""


# 你会发现 CalculateGrandTotal 方法一共做了 3 件不同的事情：计算总额、折扣 和 发票税额。
# 开发者为了搞清楚每个功能如何处理而不得不将代码从头看到尾。
# 相比于此，向下面的代码那样将每个任务分解成单独的方法则要节省更多时间，也更具可读性

class Receipt:
    def __init__(self, discounts, itemtotals):
        self.discounts = discounts
        self.itemtotals = itemtotals

    def calculate_grandtotal(self):
        subtotal = self.calculate_subtotal()
        subtotal = self.calculate_discount(subtotal)
        subtotal = self.calculate_tax(subtotal)
        return subtotal

    def calculate_tax(self, subtotal):
        tax = subtotal * 0.065
        subtotal += tax
        return subtotal

    def calculate_discount(self, subtotal):
        if len(self.discounts):
            for discount in self.discounts:
                subtotal -= discount
        return subtotal

    def calculate_subtotal(self):
        subtotal = 0
        for itemtotal in self.itemtotals:
            subtotal += itemtotal
        return subtotal
