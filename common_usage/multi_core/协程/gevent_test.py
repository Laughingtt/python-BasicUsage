#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： tian
# datetime： 2022/11/23 4:13 PM 
# ide： PyCharm
import gevent


def test(n):
    for i in range(n):
        print(gevent.getcurrent(), i)


g1 = gevent.spawn(test, 3)
g2 = gevent.spawn(test, 3)
g3 = gevent.spawn(test, 3)

g1.join()
g2.join()
g3.join()

