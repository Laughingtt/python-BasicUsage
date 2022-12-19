#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： tian
# datetime： 2022/11/26 10:37 AM 
# ide： PyCharm
def fun():
    lis = ["7",
           "IN 1 1",
           "IN 1 2",
           "IN 1 3",
           "IN 2 1",
           "OUT 1",
           "OUT 2",
           "OUT 2"]
    for i in lis:
        yield i


thin = fun()

try:
    thing_num = int(next(thin))
    in_dict = {}
    out_list = []
    times = 1
    for _th in range(thing_num):
        th = next(thin).split(" ")
        if len(th) == 3:
            if th[1] not in in_dict:
                in_dict[th[1]] = [(int(th[2]), times)]
            else:
                in_dict[th[1]].append((int(th[2]), times))
            times += 1
        elif len(th) == 2:
            out_list.append(th[1])
    #         print(in_dict)
    #         print(out_list)
    for out in out_list:
        mechine = in_dict.get(out, None)
        if mechine is None:
            print("NULL")
            continue
        #             print("mechine",mechine)
        sort_lis = sorted(mechine, key=lambda x: (-x[0], x[1]))
        pop_num = sort_lis.pop(0)
        #             print("pop_num",pop_num)
        if len(sort_lis) > 0:
            in_dict[out] = sort_lis
        else:
            in_dict[out] = None
        print(pop_num[1])
    #             print("===")

except Exception as e:
    print(e)
