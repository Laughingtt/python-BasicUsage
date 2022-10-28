#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""

# 降低字段

"""
Opposite of the Pull Up Field refactoring is push down field. 
Again, this is a pretty straight forward refactoring without much description needed
"""


# 与提升字段相反的重构是下移字段。同样，这也是一个无需多言的简单重构

class Task:
    def __init__(self):
        self._resolution = None


class BugTask(Task): pass


class FeatureTask(Task): pass


"""
In this example, we have a string field that is only used by one derived class, 
and thus can be pushed down as no other classes are using it. 
It’s important to do this refactoring at the moment the base field is no longer used by other derived classes. 
The longer it sits the more prone it is for someone to simply not touch the field and leave it be.
"""


# 在这个例子中，基类中的一个字符串字段只被一个子类使用，因此可以进行下移。
# 只要没有其他子类使用基类的字段时，就应该立即执行该重构。
# 保留的时间越长，就越有可能不去重构而保持原样。

class Task: pass


class BugTask(Task):
    def __init__(self):
        self._resolution = None


class FeatureTask(Task): pass
