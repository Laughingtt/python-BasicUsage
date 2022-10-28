#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""
from abc import ABCMeta, abstractmethod
from enum import Enum

# 使用策略类

"""
Todays refactoring doesn’t come from any one source, 
rather I’ve used different versions over the years and I’m sure other have different variations of the same aim.

This refactoring is used when you have a larger switch statement that continually changes because of new conditions being added. 
In these cases it’s often better to introduce the strategy pattern and encapsulate each condition in it’s own class. 
The strategy refactoring I’m showing here is refactoring towards a dictionary strategy. 
There is several ways to implement the strategy pattern, 
the benefit of using this method is that consumers needn’t change after applying this refactoring.
"""


# 今天的重构没有固定的形式，多年来我使用过不同的版本，并且我敢打赌不同的人也会有不同的版本。
# 该重构适用于这样的场景：switch 语句块很大，并且会随时引入新的判断条件。
# 这时，最好使用策略模式将每个条件封装到单独的类中。
# 实现策略模式的方式是很多的。
# 我在这里介绍的策略重构使用的是字典策略， 这么做的好处是调用者不必修改原来的代码。


class State(Enum):
    Alaska = 1
    NewYork = 2
    Florida = 3


class ShippingInfo:
    def calculate_shipping_amount(self, state):
        if state == State.Alaska:
            return self.get_alaska_shipping_amount()
        if state == State.NewYork:
            return self.get_newyork_shipping_amount()
        else:
            return self.get_florida_shipping_amount()

    @staticmethod
    def get_alaska_shipping_amount():
        return 15.0

    @staticmethod
    def get_newyork_shipping_amount():
        return 10.0

    @staticmethod
    def get_florida_shipping_amount():
        return 3.0


class ClientCode:
    @staticmethod
    def calculate_shipping():
        shipping_info = ShippingInfo()
        return shipping_info.calculate_shipping_amount(State.Alaska)


"""
To apply this refactoring take the condition that is being tested and place it in it’s own class that adheres to a common interface. 
Then by passing the enum as the dictionary key, we can select the proper implementation and execute the code at hand. 
In the future when you want to add another condition, add another implementation and add the implementation to the ShippingCalculations dictionary. 
As I stated before, this is not the only option to implement the strategy pattern. 
I bold that because I know someone will bring this up in the comments :)  Use what works for you. 
The benefit of doing this refactoring in this manner is that none of your client code will need to change. 
All of the modifications exist within the ShippingInfo class.

Jayme Davis pointed out that doing this refactoring really only ceates more classes because the binding still needs to be done via the ctor, 
but would be more beneficial if the binding of your IShippingCalculation strategies can be placed into IoC and 
that allows you to wire up strategies more easily.
"""


# 要应用该重构，需将每个测试条件至于单独的类中，这些类实现了一个共同的接口。
# 然后将枚举作为字典的键，这样就可以获取正确的实现，并执行其代码了。
# 以后如果希望添加新的条件，只需添加新的实现类， 并将其添加至 ShippingCalculations 字典中。
# 正如前面说过的，这不是实现策略模式的唯一方式。
# 我在这里将字体加粗显示，是因为肯定会有人在评论里指出这点，用你觉得好用的方法。
# 我用这种方式实现重构的好处是，不用修改客户端代码。
# 所有的修改都在 ShippingInfo 类内部。
# Jayme Davis 指出这种重构由于仍然需要在构造函数中进行绑定，所以只不过是增加了一些类而已，
# 但如果绑定 IShippingCalculation 的策略可以置于 IoC 中，带来的好处还是很多的，它可以使你更灵活地捆绑策略。

class State(Enum):
    Alaska = 1
    NewYork = 2
    Florida = 3


class ShippingInfo:
    def __init__(self):
        self.shipping_calculations = {
            State.Alaska: AlaskShippingCalculation(),
            State.NewYork: NewYorkShippingCalculation(),
            State.Florida: FloridaShippingCalculation(),
        }

    def calculate_shipping_amount(self, state):
        return self.shipping_calculations[state].calculate()


class IShippingCalculation(metaclass=ABCMeta):
    @abstractmethod
    def calculate(self): raise NotImplementedError()


class AlaskShippingCalculation(IShippingCalculation):
    def calculate(self): return 15.0


class NewYorkShippingCalculation(IShippingCalculation):
    def calculate(self): return 10.0


class FloridaShippingCalculation(IShippingCalculation):
    def calculate(self): return 5.0


class ClientCode:
    @staticmethod
    def calculate_shipping():
        shipping_info = ShippingInfo()
        return shipping_info.calculate_shipping_amount(State.Alaska)


"""
To take this sample full circle, 
Here is how you would wire up your bindings if you were using Ninject as your IoC container in the ShippingInfo constructor. 
Quite a few things changed here, 
mainly the enum for the state now lives in the strategy and ninject gives us a IEnumerable of all bindings to the constructor of IShippingInfo. 
We then create a dictionary using the state property on the strategy to populate our dictionary and the rest is the same.
 (thanks to Nate Kohari and Jayme Davis)
"""


# 为了使这个示例圆满，我们来看看在 ShippingInfo 构造函数中使用 Ninject 为 IoC 容器时如何进行绑定。
# 需要更改的地方很多，主要是将 state 的枚举放在策略内部，以及 Ninject 向构造函数传递一个 IShippingInfo 的 IEnumerable 泛型。
# 接下来我们使用策略类中的 state 属性创建字典，其余部分保持不变。

class State(Enum):
    Alaska = 1
    NewYork = 2
    Florida = 3


class IShippingInfo(metaclass=ABCMeta):
    @abstractmethod
    def calculate_shipping_amount(self, state): raise NotImplementedError()


class ShippingInfo(IShippingInfo):
    def __init__(self):
        self.shipping_calculations = {
            State.Alaska: AlaskShippingCalculation(),
            State.NewYork: NewYorkShippingCalculation(),
            State.Florida: FloridaShippingCalculation(),
        }

    def calculate_shipping_amount(self, state):
        return self.shipping_calculations[state].calculate()


class IShippingCalculation(metaclass=ABCMeta):
    @abstractmethod
    def calculate(self): raise NotImplementedError()


class AlaskShippingCalculation(IShippingCalculation):
    def calculate(self): return 15.0


class NewYorkShippingCalculation(IShippingCalculation):
    def calculate(self): return 10.0


class FloridaShippingCalculation(IShippingCalculation):
    def calculate(self): return 5.0


class ClientCode:
    def __init__(self, i_shippint_info):
        self.shipping_info = i_shippint_info

    def calculate_shipping(self, state):
        return self.shipping_info.calculate_shipping_amount(state)


if __name__ == '__main__':
    print(ClientCode(ShippingInfo()).calculate_shipping(State.Alaska))
    print(ClientCode(ShippingInfo()).calculate_shipping(State.NewYork))
    print(ClientCode(ShippingInfo()).calculate_shipping(State.Florida))
