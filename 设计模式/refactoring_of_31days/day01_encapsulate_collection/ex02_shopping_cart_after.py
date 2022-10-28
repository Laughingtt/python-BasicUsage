#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_shopping_cart_after.py"""


class OrderLine:
    """订单明细"""

    def __init__(self, name, price, count):
        """
        初始化函数
        :param name: 商品名称
        :param price: 商品单价
        :param count: 商品数量
        """
        self.__name = name
        self.__price = price
        self.__count = count
        self.__subtotal = self.__price * self.__count  # 价格小计

    def print_orderline(self):
        """
        打印订单明细
        :return:
        """
        print(f'{self.__name}: {self.__price} * {self.__count} = {self.__subtotal}')

    @property
    def subtotal(self):
        """
        只读属性
        :return: 订单明细价格小计
        """
        return self.__subtotal


class Order:
    """订单"""

    def __init__(self):
        self.__orderlines = []  # 订单明细列表
        self.__grandtotal = 0  # 订单合计

    @property
    def orderlines(self):
        """
        只读属性：订单明细列表只允许通过元组访问
        :return:
        """
        return tuple(self.__orderlines)

    @property
    def grandtotal(self):
        """
        只读属性：订单价格合计
        :return:
        """
        return self.__grandtotal

    def add_orderline(self, orderline):
        """
        添加订单明细
        :param orderline: 订单明细
        :return: 订单
        """
        self.__orderlines.append(orderline)
        self.__grandtotal += orderline.subtotal
        return self

    def remove_orderline(self, orderline):
        """
        移除订单明细
        :param orderline: 订单明细
        :return: 订单
        """
        if orderline in self.__orderlines:
            self.__orderlines.remove(orderline)
            self.__grandtotal -= orderline.subtotal
        return self

    def print_orderlines(self):
        """
        批量打印订单明细
        :return:
        """
        for orderline in self.__orderlines:
            orderline.print_orderline()  # 调用订单明细的打印函数
        print(f'商品总数：{len(self.__orderlines)}，订单合计：{self.__grandtotal}')
        print()  # 分隔行


if __name__ == '__main__':
    order = Order()
    order.add_orderline(OrderLine('苹果', 10, 5))
    order.add_orderline(OrderLine('香蕉', 5, 4))
    order.add_orderline(OrderLine('橘子', 15, 10))
    order.print_orderlines()
    # 重构
    try:
        order.__orderlines.append(OrderLine('西瓜', 20, 5))  # 抛出异常：元组不允许修改
    except Exception as ex:
        print(ex)
    order.print_orderlines()
    # 重构
    order.__grandtotal = 0  # 修改无效
    order.print_orderlines()
