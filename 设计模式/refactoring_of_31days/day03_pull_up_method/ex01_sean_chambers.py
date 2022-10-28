#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""
from enum import Enum, unique

# 提升方法

"""
The Pull Up Method refactoring is the process of taking a method and “Pulling” it up in the inheritance chain. 
This is used when a method needs to be used by multiple implementers.
"""


# 提升方法是将方法向继承链上层迁移的过程。用于一个方法被多个实现者使用时。
# 例如下面的代码


class Vehicle: pass


class Car(Vehicle):
    def turn(self, direction):
        pass


class Motocycle(Vehicle): pass


@unique
class Direction(Enum):
    Left = 1
    Right = 2


"""
As you can see, our Turn method is currently only available to the car class, 
we also want to use it in the motorcycle class so we create a base class if one doesn’t already exist 
and “pull up” the method into the base class making it available to both. 
The only drawback is we have increased surface area of the base class adding to it’s complexity so use wisely. 
Only place methods that need to be used by more that one derived class. 
Once you start overusing inheritance it breaks down pretty quickly and you should start to lean towards composition over inheritance. 
Here is the code after the refactoring:
"""


# 如你所见，目前只有 Car 类中包含 Turn 方法，但我们也希望在 Motorcycle 类中使用。
# 因此，如果没有基类， 我们就创建一个基类并将该方法上移到基类中，这样两个类就都可以使用 Turn 方法了。
# 这样做唯一的缺点是扩充了基类的接口、增加了其复杂性，因此需谨慎使用。
# 只有当一个以上的子类需要使用该方法时才需要进行迁移。
# 如果滥用继承，系统将会很快崩溃。这时你应该使用组合代替继承。
# 重构之后的代码如下:

class Vehicle:
    def turn(self, direction):
        pass


class Car(Vehicle): pass


class Motocycle(Vehicle): pass


@unique
class Direction(Enum):
    Left = 1
    Right = 2
