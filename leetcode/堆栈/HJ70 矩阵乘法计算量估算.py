#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： tian
# datetime： 2022/11/21 9:33 AM 
# ide： PyCharm

"""
矩阵乘法的运算量与矩阵乘法的顺序强相关。
例如：

A是一个50×10的矩阵，B是10×20的矩阵，C是20×5的矩阵

计算A*B*C有两种顺序：((AB)C)或者(A(BC))，前者需要计算15000次乘法，后者只需要3500次。

编写程序计算不同的计算顺序需要进行的乘法次数。

数据范围：矩阵个数：1\le n\le 15 \1≤n≤15 ，行列数：1\le row_i,col_i\le 100\1≤row
i
​
 ,col
i
​
 ≤100 ，保证给出的字符串表示的计算顺序唯一。
进阶：时间复杂度：O(n)\O(n) ，空间复杂度：O(n)\O(n)

输入：
3
50 10
10 20
20 5
(A(BC))
复制
输出：
3500
"""


# 可以使用对栈的方式进行，对计算规则的计算，没有遇到右括号)时，压栈，遇到右括号后出栈
def check_mul_count():
    num_count = int(input())
    num_map = {}
    for i in range(num_count):
        k = chr(ord("A") + i)
        num_map[k] = list(map(int, input().split(" ")))

    rule = input()
    stack = []
    res = 0
    for r in rule:
        # print(stack)
        # 如果是字母就插入堆栈中
        if r.isalpha():
            stack.append(num_map[r])
        # 遇到右括号弹出并插入新的矩阵纬度
        elif r == ")" and len(stack) >= 2:
            b = stack.pop()
            a = stack.pop()
            res += a[0] * b[1] * a[1]
            stack.append([a[0], b[1]])
        print(res)

    while True:
        try:
            check_mul_count()

        except Exception as e:
            break
