#!/usr/bin/evn python
# -*- coding:utf-8 -*-
"""ex02_shopping_cart_before.py"""


class OrderLine:
    """订单明细"""

    def __init__(self, name, price, count):
        """
        初始化函数
        :param name: 商品名称
        :param price: 商品单价
        :param count: 商品数量
        """
        self.name = name
        self.price = price
        self.count = count
        self.subtotal = self.price * self.count  # 价格小计

    def print_orderline(self):
        """
        打印订单明细
        :return:
        """
        print(f'{self.name}: {self.price} * {self.count} = {self.subtotal}')


class Order:
    """订单"""

    def __init__(self):
        self.orderlines = []  # 订单明细
        self.grandtotal = 0  # 订单合计

    def add_orderline(self, orderline):
        """
        添加订单明细
        :param orderline: 订单明细
        :return: 订单
        """
        self.orderlines.append(orderline)
        self.grandtotal += orderline.subtotal  # 累加订单合计
        return self

    def remove_orderline(self, orderline):
        """
        移除订单明细
        :param orderline: 订单明细
        :return: 订单
        """
        if orderline in self.orderlines:
            self.orderlines.remove(orderline)
            self.grandtotal -= orderline.subtotal  # 扣除订单合计
        return self

    def print_orderlines(self):
        """
        批量打印订单明细
        :return:
        """
        for orderline in self.orderlines:
            orderline.print_orderline()  # 调用订单明细的打印函数
        print(f'商品总数：{len(self.orderlines)}，订单合计：{self.grandtotal}')
        print()  # 分隔行


if __name__ == '__main__':
    order = Order()  # 创建订单
    order.add_orderline(OrderLine('苹果', 10, 5))  # 添加订单明细
    order.add_orderline(OrderLine('香蕉', 5, 4))  # 添加订单明细
    order.add_orderline(OrderLine('橘子', 15, 10))  # 添加订单明细
    order.print_orderlines()  # 批量打印订单明细
    # 问题
    order.orderlines.append(OrderLine('西瓜', 20, 5))  # 通过订单的列表属性添加订单明细
    order.print_orderlines()  # 批量打印订单明细
    # 问题
    order.grandtotal = 0  # 手动设置订单总价
    order.print_orderlines()  # 批量打印订单明细
