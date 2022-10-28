#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""

# 引入参数对象

"""
This refactoring comes from Fowler’s refactoring catalog and can be found here

Sometimes when working with a method that needs several parameters it becomes difficult to read the method signature 
because of five or more parameters being passed to the method like so:
"""


# 该重构来自于 Fowler 的重构目录，参见这里。
# 有时当使用一个包含多个参数的方法时，由于参数过多会导致可读性严重下降，如:

def create(amount, student, courses, credits): pass


"""
In this instances it’s useful to create a class who’s only responsibility is to carry parameters into the method. 
This helps make the code more flexible because to add more parameters, 
you need only to add another field to the parameter object. 
Be careful to only use this refactoring when you find that you have a large number of parameters to pass to the method 
however as it does add several more classes to your codebase and should be kept to a minimum.
"""


# 这时有必要新建一个类，负责携带方法的参数。
# 如果要增加更多的参数，只需为对参数对象增加其他的字段就可以了，代码显得更加灵活。
# 要注意，仅仅在方法的参数确实过多时才使用该重构，否则会使类的数量暴增，而这本应该越少越好。

class RegistrationContext:
    def __init__(self, amount, student, courses, credits):
        self.amount = amount
        self.student = student
        self.courses = courses
        self.credits = credits


class Registration:
    def create(self, registration_context): pass
