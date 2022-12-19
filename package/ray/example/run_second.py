# !/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@company:UDAI
@author:tianjian
@file:first_run.py
@time:2022/10/18

"""
import ray
import time
import hashlib

ray.init()

count = 100000


# 直接指定循环，设定cpu 不会自动并行处理
@ray.remote(num_cpus=8)
def hash1():
    for i in range(count):
        hashlib.sha256(str(i).encode("utf-8"))


def hash2():
    for i in range(count):
        hashlib.sha256(str(i).encode("utf-8"))
    return


# 调用次数过多，时间会变的更慢
@ray.remote
def hash3(i):
    hashlib.sha256(str(i).encode("utf-8"))


t0 = time.time()
# Retrieve results.
print(hash2())
print("python ", time.time() - t0)
# Launch four parallel square tasks.
t0 = time.time()
# Retrieve results.
returns = ray.get(hash1.remote())
print("ray ", time.time() - t0)
