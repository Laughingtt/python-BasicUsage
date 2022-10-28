# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Django -> 求两个字符串之间的最大公共字符串
@IDE    ：PyCharm
@Author ：爱跳水的温文尔雅的laughing
@Date   ：2020/4/2 21:48
@Desc   ：
=================================================='''


def func():
    m, n = map(str, input().strip().split())
    lis = []
    for i in range(len(m)):
        for j in range(len(n)):
            if m[j:i + j] in n:
                lis.append(len(m[j:j + i]))
    print(max(lis))

if __name__ == '__main__':
    func()