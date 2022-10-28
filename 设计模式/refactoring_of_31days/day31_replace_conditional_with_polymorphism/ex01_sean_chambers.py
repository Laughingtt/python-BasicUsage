#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""

# 使用多态代替条件判断

"""
The last day of refactoring comes from Fowlers refactoring catalog and can be found here.

This shows one of the foundations of Object Oriented Programming which is Polymorphism. 
The concept here is that in instances where you are doing checks by type, 
and performing some type of operation, 
it’s a good idea to encapsulate that algorithm within the class and then use polymorphism to 
abstract the call to the code.
"""
# 最后一天的重构来自于 Fowler 的重构目录，参见这里。
# 多态(Polymorphism)是面向对象编程的基本概念之一。
# 在这里，是指在进行类型检查和执行某些类型操作时，最好将算法封装在类中，并且使用多态来对代码中的调用进行抽象。
from abc import abstractmethod, ABCMeta


class Customer: pass


class Employee(Customer): pass


class NonEmployee(Customer): pass


class OrderProcessor:
    def process_order(self, customer, products):
        order_total = sum([p.price for p in products])
        customer_type = type(customer)
        if customer_type is type(Employee):
            order_total -= order_total * 0.15
        elif customer_type is type(NonEmployee):
            order_total -= order_total * 0.05
        return order_total


"""
As you can see here, we’re not leaning on our inheritance hierarchy to put the calculation, 
or even the data needed to perform the calculation lest we have a SRP violation. So to refactor 
this we simply take the percentage rate and place that on the actual customer type that each class 
will then implement. I know this is really remedial but I wanted to cover this as well as I have seen it in code.
"""


# 如你所见，我们没有利用已有的继承层次进行计算，而是使用了违反 SRP 原则的执行方式。
# 要进行重构， 我们只需将百分率的计算置于实际的 customer 类型之中。
# 我知道这只是一项补救措施，但我还是会这么做， 就像在代码中那样。

class Customer(metaclass=ABCMeta):
    @abstractmethod
    def discount_percentage(self): pass


class Employee(Customer):
    def discount_percentage(self): return 0.15


class NonEmployee(Customer):
    def discount_percentage(self): return 0.05


class OrderProcessor:
    def process_order(self, customer, products):
        order_total = sum([p.price for p in products])
        order_total -= order_total * customer.discount_percentage()
        return order_total
