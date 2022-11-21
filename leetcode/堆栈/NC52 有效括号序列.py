#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： tian
# datetime： 2022/11/21 10:14 AM 
# ide： PyCharm

"""
给出一个仅包含字符'(',')','{','}','['和']',的字符串，判断给出的字符串是否是合法的括号序列
括号必须以正确的顺序关闭，"()"和"()[]{}"都是合法的括号序列，但"(]"和"([)]"不合法。

数据范围：字符串长度 0\le n \le 100000≤n≤10000
要求：空间复杂度 O(n)O(n)，时间复杂度 O(n)O(n)
示例1
输入：
"["
复制
返回值：
false
复制
示例2
输入：
"[]"
复制
返回值：
true
"""


class Solution:
    def isValid(self, s: str) -> bool:
        # write code here
        stack = []
        sybol_map = {"]": "[", "}": "{", ")": "("}
        for symbol in s:
            if symbol in ["(", "{", "["]:
                stack.append(symbol)
            elif symbol in [")", "}", "]"] and len(stack) >= 1:
                end = stack.pop()
                if end != sybol_map[symbol]:
                    return False
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    s = Solution()
    print(s.isValid("([])"))
