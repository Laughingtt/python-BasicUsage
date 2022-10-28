#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""

# 使用委托（组合）代替继承

"""
All too often inheritance is used in the wrong scenarios. 
Inheritance should only be used in logical circumstances but it is often used for convenience purposes. 
I’ve seen this many times and it leads to complex inheritance hierarchies that don’t make sense. 
Take the following code:
"""


# 继承的误用十分普遍。它只能用于逻辑环境，但却经常用于简化，这导致复杂的没有意义的继承层次。
# 看下面的代码:

class Sanitation:
    @staticmethod
    def wash_hands(): return 'cleaned'


class Child(Sanitation): pass


"""
In this instance, a Child is not a “Sanitation” and therefore doesn’t make sense as an inheritance hierarchy. 
We can refactor by initializing an instance of Sanitation in the Child constructor and delegating 
the call to the class rather than via inheritance. 
If you were using Dependency Injection, you would pass in the Sanitation instance via the constructor, 
although then you would need to register your model in your IoC container which is a smell IMO, 
you get the idea though. Inheritance should ONLY be used for scenarios where inheritance is warranted. 
Not instances where it makes it quicker to throw down code.
"""


# 在该例中，Child 并不是 Sanitation，因此这样的继承层次是毫无意义的。
# 我们可以这样重构：在 Child 的构造函数里实现一个 Sanitation 实例，并将方法的调用委托给这个实例。
# 如果你使用依赖注入，可以通过构造函数传递 Sanitation 实例，尽管在我看来还要向 IoC 容器注册模型是一种坏味道，但领会精神就可以了。
# 继承只能用于严格的继承场景，并不是用来快速编写代码的工具。

class Sanitation:
    @staticmethod
    def wash_hands(): return 'cleaned'


class Child:
    def __init__(self, sanitation):
        self.sanitation = sanitation

    def wash_hands(self):
        return self.sanitation.wash_hands()
