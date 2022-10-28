#!/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@company:UDAI
@author:tianjian
@file:Offer06从尾到头打印链表.py
@time:2020/11/22

"""
"""
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

 

示例 1：

输入：head = [1,3,2]
输出：[2,3,1]
"""


class NodeList(object):
    def __init__(self, x):
        self.val = x
        self.next: NodeList = None


class LinkList(object):
    def __init__(self, head):
        self.head = head

    def create_node_list(self):
        res = NodeList(self.head[0])
        n = res
        for i in self.head[1:]:
            n.next = NodeList(i)
            n = n.next
        return res


class Solution:
    def _reversePrint(self, head):
        """递归"""
        if not head:
            return []

        res_lis = []

        def fun(head):
            res_lis.append(head.val)
            if head.next:
                fun(head.next)

        fun(head)
        return list(reversed(res_lis))

    def reversePrint(self, head):
        """循环"""
        if not head:
            return []

        lis = []
        while head.next:
            lis.append(head.val)
            head = head.next

        lis.append(head.val)
        return list(reversed(lis))


if __name__ == '__main__':
    head = [2, 3, 1]
    link_list = LinkList(head)
    link = link_list.create_node_list()
    print(link.next.__dict__)

    solution = Solution()
    res = solution.reversePrint(link)
    print(res)
