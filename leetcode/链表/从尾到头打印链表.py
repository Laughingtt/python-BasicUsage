#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： tian
# datetime： 2022/11/22 5:50 PM 
# ide： PyCharm

"""
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。



示例 1：

输入：head = [1,3,2]
输出：[2,3,1]
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reversePrint(self, head: ListNode):
        lis = []
        while head is not None:
            lis.append(head.val)
            head = head.next
        lis.reverse()
        return lis


class Solution2:
    def reversePrint(self, head: ListNode):
        return self.reversePrint(head.next) + [head.val] if head else []
