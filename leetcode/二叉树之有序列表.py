# -*- coding: UTF-8 -*-
""""=================================================
@Project -> File   ：Django -> 二叉树之有序列表
@IDE    ：PyCharm
@Author ：爱跳水的温文尔雅的laughing
@Date   ：2020/4/2 21:56
@Desc   ：
=================================================="""


import bisect

lis=[1,3,5,8,11,15]

#获取index的位置，如果x存在则返回x之后index的位置，不存在则返回最近的index
print(bisect.bisect(lis,7))
print(bisect.bisect(lis,8))

#插入合适的位置
bisect.insort(lis,7)

print(bisect.bisect_left(lis,7))  #等同于bisect
print(bisect.bisect_right(lis,3))  #最近index+1
print(lis)

"""
3
4
3
2
[1, 3, 5, 7, 8, 11, 15]
"""