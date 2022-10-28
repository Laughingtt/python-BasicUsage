#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""

# 提取子类

"""
Todays refactoring comes from Martin Fowlers catalog of patterns. You can find this refactoring in his catalog here

This refactoring is useful when you have methods on a base class that are not shared amongst all classes and needs 
to be pushed down into it’s own class. The example I’m using here is pretty straightforward. 
We start out with a single class called Registration. 
This class handles all information related to a student registering for a course.
"""


# 今天的重构来自于 Martin Fowler 的模式目录。你可以在他的目录中找到该重构。
# 当一个类中的某些方法并不是面向所有的类时，可以使用该重构将其迁移到子类中。
# 我这里举的例子十分简单，它包含一个 Registration 类，该类处理与学生注册课程相关的所有信息。

class Registration:
    def __init__(self, non_registration_action, registration_total, notes, description, registration_date):
        self.non_registration_action = non_registration_action
        self.registration_total = registration_total
        self.notes = notes
        self.description = description
        self.registration_date = registration_date


"""
There is something that we’ve realized after working with this class. 
We are using it in two different contexts. 
The properties NonRegistrationAction and Notes are only ever used when dealing with a NonRegistration 
which is used to track a portion of the system that is slightly different than a normal registration. 
Noticing this, we can extract a subclass and move those properties down into the NonRegistration class 
where they more appropriately fit.
"""


# 当使用了该类之后，我们就会意识到问题所在——它应用于两个完全不同的场景。
# 属性 NonRegistrationAction 和 Notes 只有在处理与普通注册略有不同的 NonRegistration 时才会使用。
# 因此，我们可以提取一个子类， 并将这两个属性转移到 NonRegistration 类中，这样才更合适。

class Registration:
    def __init__(self, registration_total, description, registration_date):
        self.registration_total = registration_total
        self.description = description
        self.registration_date = registration_date


class NonRegistration(Registration):
    def __init__(self, non_registration_action, notes, registration_total, description, registration_date):
        super().__init__(registration_total, description, registration_date)
        self.non_registration_action = non_registration_action
        self.notes = notes
