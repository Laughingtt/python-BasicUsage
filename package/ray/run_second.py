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

count = 10000
# Define the square task.
@ray.remote
def hash1():
    for i in range(count):
        hashlib.sha256(str(i).encode("utf-8"))
    return


def hash2():
    for i in range(count):
        hashlib.sha256(str(i).encode("utf-8"))
    return


t0 = time.time()
# Retrieve results.
print(hash2())
print("python ",time.time() - t0)
# Launch four parallel square tasks.
t0 = time.time()
# Retrieve results.
print(ray.get(hash1.remote()))
print("ray ",time.time() - t0)
