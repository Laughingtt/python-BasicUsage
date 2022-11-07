# !/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@company:UDAI
@author:tianjian
@file:ray_data.py
@time:2022/10/26

"""

import ray
import pandas as pd

# create data
# ds = ray.data.range(10000)
# ds = ds.repartition(10)
# print("take ", ds.take(5))


# read csv
ds = ray.data.read_csv("/Users/tian/Projects/python-BasicUsage/算法/data/my_data_guest.csv")

# 将数据拆分为10个partition
ds = ds.repartition(10)


def pandas_transform(df: pd.DataFrame) -> pd.DataFrame:
    # Filter rows.
    print("df is ", df.count())
    return df


# 设置batch_size ,会根据100一批并行的运行
ds.map_batches(pandas_transform, batch_size=100)
