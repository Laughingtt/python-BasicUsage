#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： tian
# datetime： 2022/11/20 9:03 PM 
# ide： PyCharm
"""
开发一个坐标计算工具， A表示向左移动，D表示向右移动，W表示向上移动，S表示向下移动。从（0,0）点开始移动，从输入字符串里面读取一些坐标，并将最终输入结果输出到输出文件里面。

输入：

合法坐标为A(或者D或者W或者S) + 数字（两位以内）

坐标之间以;分隔。

非法坐标点需要进行丢弃。如AA10;  A1A;  $%$;  YAD; 等。

下面是一个简单的例子 如：

A10;S20;W10;D30;X;A1A;B10A11;;A10;

处理过程：

起点（0,0）

+   A10   =  （-10,0）

+   S20   =  (-10,-20)

+   W10  =  (-10,-10)

+   D30  =  (20,-10)

+   x    =  无效

+   A1A   =  无效

+   B10A11   =  无效

+  一个空 不影响

+   A10  =  (10,-10)

结果 （10， -10）

数据范围：每组输入的字符串长度满足 1\le n \le 10000 \1≤n≤10000  ，坐标保证满足 -2^{31} \le x,y \le 2^{31}-1 \−2
31
 ≤x,y≤2
31
 −1  ，且数字部分仅含正数
"""

import sys

for line in sys.stdin:
    cmd = line.split(";")
    point = [0, 0]
    for _cmd in cmd:
        cc = list(_cmd.strip())
        if len(cc) > 3 or len(cc) < 2:
            continue
        first = cc[0]
        if first not in ["A", "D", "W", "S"]:
            continue
        sec = "".join(cc[1:])
        if not sec.isdigit():
            continue

        sec = int(sec)
        if first == "A":
            point[0] = point[0] - sec
        elif first == "S":
            point[1] = point[1] - sec
        elif first == "D":
            point[0] = point[0] + sec
        elif first == "W":
            point[1] = point[1] + sec

    print("{},{}".format(point[0], point[1]))



