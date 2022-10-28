#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""

"""迁移方法

The refactoring today is pretty straightforward,
今天的重构同样非常简单

although often overlooked and ignored as being a worthwhile refactoring. 
以至于人们并不认为这是一个有价值的重构

Move method does exactly what it sounds like, move a method to a better location.
迁移方法，顾名思义就是将方法迁移到合适的位置
 
Let’s look at the following code before our refactoring
在开始重构前，我们先看一下代码
"""


class BankAccount:
    """银行账户"""

    def __init__(self, account_age, credit_score, account_interest):
        """
        初始化函数
        :param account_age: 户龄
        :param credit_score: 信用积分
        :param account_interest: 账户利率
        """
        self.__account_age = account_age
        self.__credit_score = credit_score
        self.__account_interest = account_interest

    def calculate_interest_rate(self):
        """
        计算贷款利率
        :return: 贷款利率
        """
        if self.__credit_score > 800: return 0.02  # 信用积分大于800时还款利率0.02
        if self.__account_age > 10: return 0.03  # 户龄超过10年时还款利率0.03
        return 0.05  # 标准还款利率0.05


class AccountInterest:
    """账户利率"""

    def __init__(self, bank_account):
        """
        初始化函数
        :param bank_account: 银行账户
        """
        self.__bank_account = bank_account

    @property
    def interest_rate(self):
        """
        只读属性：还款利率
        :return: 根据关联的账户计算还款利率
        """
        return self.__bank_account.calculate_interest_rate()

    @property
    def introductory_rate(self):
        """
        只读属性：引入率
        :return:
        """
        return self.__bank_account.calculate_interest_rate() < 0.05  # 判断引入率是否低于标准还款利率


"""
The point of interest here is the BankAccount.CalculateInterest method. 
这里指的注意的是 BankAccount.calculate_interest_rate 方法

A hint that you need the Move Method refactoring is when another class is using a method more often then the class in which it lives.
需要进行 move 方法重构的提示是，当另一个类比它所在的类更频繁地使用某个方法时
 
If this is the case it makes sense to move the method to the class where it is primarily used. 
如果是这种情况，那么将方法移动到主要使用它的类是有意义的

This doesn’t work in every instance because of dependencies, 
由于依赖关系，这并不是在每个实例中都有效

but it is overlooked often as a worthwhile change. 
但作为一个有价值的改变，它往往被忽视

In the end you would end up with something like this:
该重构最终的代码应该是这样的
"""


class BankAccount:
    def __init__(self, account_age, credit_score, account_interest):
        self.__account_age = account_age
        self.__credit_score = credit_score
        self.__account_interest = account_interest

    @property
    def account_age(self): return self.__account_age

    @property
    def credit_score(self): return self.credit_score


class AccountInterest:
    def __init__(self, bank_account):
        self.__bank_account = bank_account

    def calculate_interest_rate(self):
        if self.__bank_account.credit_score > 800: return 0.02
        if self.__bank_account.account_age > 10: return 0.03
        return 0.05

    @property
    def interest_rate(self):
        return self.calculate_interest_rate()

    @property
    def introductory_rate(self):
        return self.calculate_interest_rate() < 0.05
