#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""

# 提取父类

"""
Today’s refactoring is from Martin Fowler’s refactoring catalog. You can find the original description here

This refactoring is used quite often when you have a number of methods that you want to “pull up” into a base class 
to allow other classes in the same hierarchy to use. 
Here is a class that uses two methods that we want to extract and make available to other classes.
"""


# 今天的重构来自于 Martin Fowler 的重构目录，其原始介绍在此。
# 当一个类有很多方法希望将它们提拔到基类以供同层次的其他类使用时，会经常使用该重构。
# 下面的类包含两个方法，我们希望提取这两个方法并允许其他类使用。

class Dog:
    def eat_food(self): pass

    def groom(self): pass


"""
After applying the refactoring we just move the required methods into a new base class. 
This is very similar to the [pull up refactoring], 
except that you would apply this refactoring when a base class doesn’t already exist.
"""


# 重构之后，我们仅仅将需要的方法转移到了一个新的基类中。
# 这很类似“Pull Up”重构，只是在重构之前， 并不存在基类。

class Animal:
    def eat_food(self): pass

    def groom(self): pass


class Dog(Animal): pass
