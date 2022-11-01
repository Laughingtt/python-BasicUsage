# !/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@company:UDAI
@author:tianjian
@file:传递对象.py
@time:2022/10/18

如上所示，Ray 将任务和参与者调用结果存储在其分布式对象存储中，返回可以稍后检索的对象引用。
对象引用也可以通过显式创建ray.put，并且对象引用可以作为参数值的替代物传递给任务：
"""
import ray
import numpy as np

ray.init()


# Define a task that sums the values in a matrix.
@ray.remote
def sum_matrix(matrix):
    return np.sum(matrix)


# Call the task with a literal argument value.
print(ray.get(sum_matrix.remote(np.ones((100, 100)))))
# -> 10000.0

# Put a large array into the object store.
matrix_ref = ray.put(np.ones((1000, 1000)))

# Call the task with the object reference as an argument.
print(ray.get(sum_matrix.remote(matrix_ref)))
# -> 1000000.0

ray.put()