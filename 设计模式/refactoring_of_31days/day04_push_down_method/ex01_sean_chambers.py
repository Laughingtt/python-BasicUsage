#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""
from abc import ABCMeta

# 降低方法

"""
Yesterday we looked at the pull up refactoring to move a method to a base class so mutiple derived classes can use a method. 
Today we look at the opposite. Here is the code before the refactoring:
"""


# 和提升方法相反，我们先来看一下重构之前的代码


class Animal:
    def bark(self): pass


class Dog(Animal): pass


class Cat(Animal): pass


"""
So here we have some code with a base class that has a Bark method. 
Perhaps at one time our cat could bark, 
but now we no longer need that functionality on the Cat class. 
So we “Push Down” the Bark method into the Dog class as it is no longer needed on the base class 
but perhaps it is still needed when dealing explicitly with a Dog. 
At this time, it’s worthwhile to evaluate if there is any behavior still located on the Animal base class. 
If not, it is a good opportunity to turn the Animal abstract class into an interface 
instead as no code is required on the contract and can be treated as a marker interface.
"""


# 这里的基类有一个 Bark 方法。
# 或许我们的猫咪们一时半会也没法学会汪汪叫(bark)，因此 Cat 类中不再需要这个功能了。
# 尽管基类不需要这个方法，但在显式处理 Dog 类时也许还需要，因此我们将 Bark 方法下移到 Dog 类中。
# 这时，有必要评估 Animal 基类中是否还有其他行为。
# 如果没有，则是一个将 Animal 抽象类转换成接口的好时机。
# 因为契约中不需要任何代码，可以认为是一个标记接口。

# 重构后的代码如下

class Animal(metaclass=ABCMeta): pass


class Dog(Animal):
    def bark(self): pass


class Cat(Animal): pass
