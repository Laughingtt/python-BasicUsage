#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""

# 重命名

"""
This refactoring I use most often and is one of the most useful refactoring. 
All too often we do not name methods/classes/parameters properly that leads to a misunderstanding 
as to what the method/class/parameter’s function is. 
When this occurs, assumptions are made and bugs are introduced to the system. 
As simple of a refactoring this seems, it is one of the most important to leverage.
"""


# 这是我最常用也是最有用的重构之一。
# 我们对方法/类/参数的命名往往不那么合适，以至于误导阅读者对于方法/类/参数功能的理解。
# 这会造成阅读者的主观臆断，甚至引入 bug。
# 这个重构看起来简单，但却十分重要。

class Person:
    def __init__(self, fn):
        self.fn = fn

    def clchrlypr(self):
        """计算时薪的代码"""
        return .0


"""
As you can see here, we have a class/method/parameter that all have very non-descriptive, obscure names. 
They can be interpreted in a number of different ways. 
Applying this refactoring is as simple as renaming the items at hand to be more descriptive and convey what exactly they do. Simple enough.
"""


# 如你所见，我们的类/方法/参数的名称十分晦涩难懂，可以理解为不同的含义。
# 应用这个重构你只需随手将名称修改得更具描述性、更容易传达其含义即可。
# 见名知意

class Employee:
    def __init__(self, first_name):
        self.first_name = first_name

    def calculate_hourly_pay(self):
        """计算时薪的代码"""
        return .0
