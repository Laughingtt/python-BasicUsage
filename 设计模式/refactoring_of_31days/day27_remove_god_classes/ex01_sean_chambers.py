#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""

# 移除上帝类

"""
Often with legacy code bases I will often come across classes that are clear SRP violations. 
Often these classes will be suffixed with either “Utils” or “Manager”. 
Sometimes they don’t have this indication and are just classes with multiple grouped pieces of functionality. 
Another good indicator of a God class is methods grouped together with using statements or comments into 
seperate roles that this one class is performing.

Over time, these classes become a dumping ground for a method that someone doesn’t have time/want to put in 
the proper class. The refactoring for situations like these is to break apart the methods into distinct classes 
that are responsible for specific roles.
"""


# 在传统的代码库中，我们常常会看到一些违反了 SRP 原则的类。
# 这些类通常以 Utils 或 Manager 结尾，有时也没有这么明显的特征而仅仅是普通的包含多个功能的类。这种 God 类还有一个特征，使用语句或注释将 代码分隔为多个不同角色的分组，而这些角色正是这一个类所扮演的。 久而久之，这些类成为了那些没有时间放置到恰当类中的方法的垃圾桶。这时的重构需要将方法分解成多 个负责单一职责的类。

class CustomerService:
    def calculate_order_discount(self, products, customer): pass

    def customer_isvalid(self, customer, order): pass

    def gather_order_errors(self, products, customer): pass

    def register(self, customer): pass

    def forgot_password(self, customer): pass


"""
The refactoring for this is very straight forward. 
Simply take the related methods and place them in specific classes that match their responsibility. 
This makes them much finer grained and defined in what they do and make future maintenance much easier. 
Here is the end result of splitting up the methods above into two distinct classes.
"""


# 使用该重构是非常简单明了的，只需把相关方法提取出来并放置到负责相应职责的类中即可。
# 这使得类的粒度更细、职责更分明、日后的维护更方便。上例的代码最终被分解为两个类


class CustomerOrderService:
    def calculate_order_discount(self, products, customer): pass

    def customer_isvalid(self, customer, order): pass

    def gather_order_errors(self, products, customer): pass


class CustomerRegistrationService:
    def register(self, customer): pass

    def forgot_password(self, customer): pass
