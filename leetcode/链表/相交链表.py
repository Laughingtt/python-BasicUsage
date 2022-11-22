#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： tian
# datetime： 2022/11/22 5:21 PM 
# ide： PyCharm
"""

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __repr__(self):
        print("val is {},next is {}".format(self.val, self.next))


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        A, B = headA, headB
        while A != B:
            A = A.next if A else headB
            B = B.next if B else headA
        return A