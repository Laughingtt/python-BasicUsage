#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： tian
# datetime： 2022/11/23 4:20 PM 
# ide： PyCharm
from gevent import monkey;

monkey.patch_all()
from urllib import request
import gevent


def test(url):
    print('Get: %s' % url)
    response = request.urlopen(url)
    content = response.read().decode('utf8')
    print('%d bytes received from %s.' % (len(content), url))


if __name__ == '__main__':
    gevent.joinall([
        gevent.spawn(test, 'http://httpbin.org/ip'),
        gevent.spawn(test, 'http://httpbin.org/uuid'),
        gevent.spawn(test, 'http://httpbin.org/user-agent')
    ])

"""
从结果看，3个网络操作是并发执行的，而且结束顺序不同，但只有一个线程。

"""
