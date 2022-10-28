#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""
from abc import ABCMeta, abstractmethod

# 分解依赖

"""
Today’s refactoring is useful if you are trying to introduce unit tests into your code base as testing “seams” 
are needed to properly mock/isolate areas you don’t wish to test. 
In this example we have client code that is using a static class to accomplish some work. 
The problem with this when it comes to unit testing because there is no way to mock the static class from our unit test. 
To work around this you can apply a wrapper interface around the static to create a seam and break the dependency on the static.
"""


# 有些单元测试需要恰当的测试缝隙(test seam)来模拟/隔离一些不想被测试的部分。
# 如果你正想在代码中引入这种单元测试，那么今天介绍的重构就十分有用。
# 在这个例子中，我们的客户端代码使用一个静态类来实现功能。
# 但当需要单元测试时，问题就来了。我们无法在单元测试中模拟静态类。
# 解决的方法是使用一个接口将静态类包装起来，形成一个缝隙来切断与静态类之间的依赖。


class Feeder:
    @staticmethod
    def replenish_food(): pass


class AnimalFeedingService:
    def __init__(self, foodbowlempty):
        self.foodbowlempty = foodbowlempty

    def feed(self):
        if self.foodbowlempty:
            Feeder.replenish_food()


"""
All we did to apply this refactoring was introduce an interface and class that simply calls the underlying static class. 
So the behavior is still the same, just the manner in which it is invoked has changed. 
This is good to get a starting point to begin refactoring from and an easy way to add unit tests to your code base.
"""


# 重构时我们所要做的就是引入一个接口和简单调用上面那个静态类的类。
# 因此行为还是一样的，只是调用的方式产生了变化。
# 这是一个不错的重构起始点，也是向代码添加单元测试的简单方式。

class Feeder:
    @staticmethod
    def replenish_food(): pass


class IFeederService(metaclass=ABCMeta):
    @abstractmethod
    def replenish_food(self):
        raise NotImplementedError()


class FeederService(IFeederService):
    def replenish_food(self):
        Feeder.replenish_food()


class AnimalFeedingService:
    def __init__(self, foodbowlempty, i_feeder_service):
        self.foodbowlempty = foodbowlempty
        self.i_feeder_service = i_feeder_service

    def feed(self):
        if self.foodbowlempty:
            self.i_feeder_service.replenish_food()


"""
We can now mock IFeederService during our unit test via the AnimalFeedingService constructor by passing in a mock of IFeederService. 
Later we can move the code in the static into FeederService and delete the static class completely once we have some tests in place.
"""
# 现在，我们可以在单元测试中将模拟的 IFeederService 传入 AnimalFeedingService 构造函数。
# 测试成功后， 我们可以将静态方法中的代码移植到 FeederService 类中，并删除静态类。
