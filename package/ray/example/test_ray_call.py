# !/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@company:UDAI
@author:tianjian
@file:test_py.py
@time:2022/10/25

"""
import ray

ray.init()


class CallTest(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, fn):
        def wrapper(*args, **kwargs):
            return self._run.remote(fn, *args, **kwargs)

        return wrapper

    @staticmethod
    @ray.remote
    def _run(fn, *args, **kwargs):
        print(fn)
        print(args)
        print(kwargs)
        return fn(*args, **kwargs)


cal = CallTest("tian")


def print_h(*args, **kwargs):
    print("hello world {} == {}".format(args, kwargs))


cal(print_h)("233", "1223", abc=1)
