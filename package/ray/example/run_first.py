# !/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@company:UDAI
@author:tianjian
@file:first_run.py
@time:2022/10/18

"""
import ray

ray.init()


# Define the square task.
@ray.remote
def square(x):
    return x * x


# Launch four parallel square tasks.
futures = [square.remote(i) for i in range(400)]

# Retrieve results.
print(ray.get(futures))
# -> [0, 1, 4, 9]
