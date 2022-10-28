#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""

# 重命名布尔方法

"""
Today’s refactoring doesn’t necessarily come from Fowlers refactoring catalog. 
If anyone knows where this “refactoring” actually comes from, please let me know.

Granted, this could be viewed as not being a refactoring as the methods are actually changing, 
but this is a gray area and open to debate. Methods with a large number of boolean parameters can quickly 
get out of hand and can produce unexpected behavior. 
Depending on the number of parameters will determine how many methods need to be broken out. 
Let’s take a look at where this refactoring starts:
"""


# 今天的重构不是来自于 Fowler 的重构目录。
# 如果谁知道这项重构的确切出处，请告诉我。
# 当然，你也可以说这并不是一个真正的重构，因为方法实际上改变了，但这是一个灰色地带，可以开放讨论。
# 一个拥有大量布尔类型参数的方法将很快变得无法控制，产生难以预期的行为。
# 参数的数量将决定分解的方法的数量。来看看该重构是如何开始的

class BankAccount:
    def create_account(self, customer, with_checking, with_saving, with_stocks): pass


"""
We can make this work a little better simple by exposing the boolean parameters via well named methods and 
in turn make the original method private to prevent anyone from calling it going forward. 
Obviously you could have a large number of permutations here and perhaps it makes more sense to refactor to a 
Parameter object instead.
"""


# 要想使这样的代码运行得更好，我们可以通过命名良好的方法暴露布尔参数，并将原始方法更改为 private 以阻止外部调用。
# 显然，你可能需要进行大量的代码转移，也许重构为一个 Parameter Object 会更有意义。

class BankAccount:
    def create_account_with_checking(self, customer):
        self.__create_account(customer, True, False)

    def create_account_with_checking_and_saving(self, customer):
        self.__create_account(customer, True, True)

    def __create_account(self, customer, with_checking, with_saving): pass
