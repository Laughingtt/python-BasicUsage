#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""

import datetime

# 封装条件

"""
Sometimes when doing a number of different checks within a conditional the intent of what you are testing for 
gets lost in the conditional. In these instances I like to extract the conditional into an easy to read property, 
or method depending if there is parameters to pass or not. Here is an example of what the code might look like before:
"""


# 当代码中充斥着若干条件判断时，代码的真正意图会迷失于这些条件判断之中。
# 这时我喜欢将条件判断提取到一个易于读取的属性或方法(如果有参数)中。
# 重构之前的代码如下:


class RemoteControl:
    def __init__(self, name, created_year):
        self.name = name
        self.created_year = created_year
        self.functions = []

    def perform_cool_function(self, button_pressed):
        if all([len(self.functions), self.name == 'RCA', self.created_year > (datetime.date.today().year - 2)]):
            return 'do something'


"""
After we apply the refactoring, you can see the code reads much easier and conveys intent:
"""


# 重构之后，代码的可读性更强，意图更明显


class RemoteControl:
    def __init__(self, name, created_year):
        self.name = name
        self.created_year = created_year
        self.functions = []

    @property
    def has_extra_functions(self):
        return len(self.functions) and self.name == 'RCA' and self.created_year > (datetime.date.today().year - 2)

    def perform_cool_function(self, button_pressed):
        if self.has_extra_functions:
            return 'do something'
