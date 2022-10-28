#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""

# 合并继承

"""
Todays refactoring comes from Martin Fowlers catalog of patterns. You can find this refactoring in his catalog here

Yesterday we looked at extracting a subclass for moving responsibilities down if they are not needed across the board. 
A Collapse Hierarchy refactoring would be applied when you realize you no longer need a subclass. 
When this happens it doesn’t really make sense to keep your subclass around if it’s properties can be 
merged into the base class and used strictly from there.
"""


# 今天的重构来自于 Martin Fowler 的模式目录。你可以在他的目录中找到该重构。
# 昨天，我们通过提取子类来下放职责。
# 而今天，当我们意识到不再需要某个子类时，可以使用 Collapse Hierarchy 重构。
# 如果某个子类的属性(以及其他成员)可以被合并到基类中，这时再保留这个子类已经没有任何意义了。

class Website:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.pages = []


class StudentWebsite(Website):
    def __init__(self, is_active, title, description):
        super().__init__(title, description)
        self.is_active = is_active


"""
Here we have a subclass that isn’t doing too much. 
It just has one property to denote if the site is active or not. 
At this point maybe we realize that determing if a site is active is something we can use across the board 
so we can collapse the hierarchy back into only a Website and eliminate the StudentWebsite type.
"""


# 这里的子类并没有过多的功能，只是表示站点是否激活。
# 这时我们会意识到判断站点是否激活的功能应该是通用的。
# 因此可以将子类的功能放回到 Website 中，并删除 StudentWebsite 类型。

class Website:
    def __init__(self, title, description, is_active):
        self.title = title
        self.description = description
        self.pages = []
        self.is_active = is_active
