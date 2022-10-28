#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex01_sean_chambers.py"""

# 去除中间人对象

"""
Today’s refactoring comes from Fowler’s refactoring catalog and can be found here.

Sometimes in code you may have a set of “Phantom” or “Ghost” classes. Fowler calls these “Middle Men”. 
Middle Men classes simply take calls and forward them on to other components without doing any work. 
This is an unneeded layer and can be removed completely with minimal effort.
"""


# 今天的重构来自于 Fowler 的重构目录，见这里。
# 有时你的代码里可能会存在一些“Phantom”或“Ghost”类，Fowler称之为“中间人(Middle Man)”。
# 这些中间人类仅仅简单地将调用委托给其他组件，除此之外没有任何功能。
# 这一层是完全没有必要的，我们可以不费吹灰之力将其完全移除。

class Customer:
    def __init__(self, account_manager):
        self.account_manager = account_manager

    def get(self, account_id):
        account = self.account_manager.get_account(id)
        return account


class AccountManager:
    def __init__(self, data_provider):
        self.data_provider = data_provider

    def get_account(self, account_id):
        return self.data_provider.get_account(account_id)


class AccountDataProvider:
    def get_account(self, account_id): pass


"""
The end result is straightforward enough. We just remove the middle man object and point the original call to 
the intended receiver.
"""


# 最终结果已经足够简单了。我们只需要移除中间人对象，将原始调用指向实际的接收者。


class Customer:
    def __init__(self, account_data_provider):
        self.account_data_provider = account_data_provider

    def get(self, account_id):
        account = self.account_data_provider.get_account(id)
        return account


class AccountDataProvider:
    def get_account(self, account_id): pass
