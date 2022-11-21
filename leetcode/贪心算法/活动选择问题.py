#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： tian
# datetime： 2022/11/17 9:25 PM 
# ide： PyCharm

# 在此场地可举办的活动有以下这么多场，问最多举办的活动有多少场
# 解: 最早结束的活动，为当前最优解，也就是说，活动结束的越早后面预留的时间越多，活动也可能越多
# (活动开始时间，活动结束时间)
active = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]


def find_max_times(active):
    current_time = 0
    max_time = max([i[1] for i in active])
    while current_time < max_time:
        min_active_time = 99
        for start, end in active:
            if start >= current_time and end <= min_active_time:
                min_active_time = end
        current_time = min_active_time
        print("current_time is {}".format(current_time))


if __name__ == '__main__':
    find_max_times(active)
