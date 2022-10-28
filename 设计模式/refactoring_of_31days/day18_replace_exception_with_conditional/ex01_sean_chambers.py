#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""

# 使用条件判断代替异常

"""
Today’s refactoring doesn’t come from any place specifically, 
just something I’ve picked up over time that I find myself using often. 
Any variations/comments would be appreciated to this approach. 
I think there’s some other good refactorings around these type of problems.

A common code smell that I come across from time to time is using exceptions to control program flow. 
You may see something to this effect:
"""


# 今天的重构没有什么出处，是我平时经常使用而总结出来的。
# 欢迎您发表任何改进意见或建议。
# 我相信一定还有其他比较好的重构可以解决类似的问题。
# 我曾无数次面对的一个代码坏味道就是，使用异常来控制程序流程。
# 您可能会看到类似的代码:


class Microwave:
    def __init__(self, motor):
        self.motor = motor

    def start(self, food):
        food_cooked = False
        try:
            self.motor.cook(food)
            food_cooked = True
        except Exception:
            food_cooked = False
        return food_cooked


"""
Exceptions should only be there to do exactly what they are for, handle exceptional behavior. 
Most of the time you can replace this type of code with a proper conditional and handle it properly. 
This is called design by contract in the after example because we are ensuring a specific state of the Motor class 
before performing the necessary work instead of letting an exception handle it.
"""


# 异常应该仅仅完成自己的本职工作：处理异常行为。
# 大多数情况你都可以将这些代码用恰当的条件判断替换，并进行恰当的处理。
# 下面的代码可以称之为契约式设计，因为我们在执行具体工作之前明确了 Motor 类的状态，而不是通过异常来进行处理。

class Microwave:
    def __init__(self, motor):
        self.motor = motor

    def star(self, food):
        if self.motor.isinuse:
            return False
        self.motor.cook(food)
        return True
