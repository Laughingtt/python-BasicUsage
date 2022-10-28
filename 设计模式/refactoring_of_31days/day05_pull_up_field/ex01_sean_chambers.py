#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""

# 提升字段

"""
Today we look at a refactoring that is similar to the Pull Up method. 
Instead of a method, it is obviously done with a field instead!
"""


# 今天我们来看看一个和提升方法十分类似的重构。我们处理的不是方法，而是字段。

class Account: pass


class CheckingAccount(Account):
    def __init__(self):
        self.__minimum_checking_balance = 5.0


class SavingsAccount(Account):
    def __init__(self):
        self.__minimum_checking_balance = 5.0


"""
In this example, we have a constant value that is duplicated between two derived classes. 
To promote reuse we can pull up the field into the base class and rename it for brevity.
"""


# 在这个例子中，两个子类中包含重复的常量。为了提高复用性我们将字段上移到基类中，并简化其名称。

class Account:
    def __init__(self):
        self.__minimum_balance = 5.0


class CheckingAccount(Account): pass


class SavingsAccount(Account): pass
