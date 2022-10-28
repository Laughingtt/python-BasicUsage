#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""

# 移除双重否定

"""
Today’s refactoring comes from Fowler’s refactoring catalog and can be found here.

This refactoring is pretty simple to implement although I find it in many codebases that severely 
hurts readability and almost always conveys incorrect intent. 
This type of code does the most damage because of the assumptions made on it. 
Assumptions lead to incorrect maintenance code written, which in turn leads to bugs. 
Take the following example:
"""


# 今天的重构来自于 Fowler 的重构目录，参见这里。
# 尽管我在很多代码中发现了这种严重降低可读性并往往传达错误意图的坏味道，但这种重构本身还是很容易实现的。
# 这种毁灭性的代码所基于的假设导致了错误的代码编写习惯，并最终导致 bug。
# 如下例所示:

class Order:
    def checkout(self, products, customer):
        if not customer.isnotflagged:
            # the customer account is flagged
            # log some errors and return
            return
        # normal order processing


class Customer:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self): return self.__balance

    @property
    def isnotflagged(self): return self.__balance < 30


"""
As you can see the double negative here is difficult to read because we have to figure out 
what is positive state of the two negatives. 
The fix is very easy. If we don’t have a positive test, 
add one that does the double negative assertion for you rather than make sure you get it correct.
"""


# 如你所见，这里的双重否定十分难以理解，我们不得不找出什么才是双重否定所要表达的肯定状态。
# 修改代码是很容易的。如果我们找不到肯定的判断，可以添加一个处理双重否定的假设，而不要在得到结果之后再去验证。

class Customer:
    def __init__(self, balance):
        self.__balance = balance

    @property
    def balance(self): return self.__balance

    @property
    def isflagged(self): return self.__balance >= 30


class Order:
    def checkout(self, products, customer):
        if customer.isflagged:
            return
