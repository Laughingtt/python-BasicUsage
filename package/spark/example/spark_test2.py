# !/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@company:UDAI
@author:tianjian
@file:test.py
@time:2021/12/10

"""
from pyspark import SparkContext, SparkConf


def create_sc():
    sc_conf = SparkConf()
    # sc_conf.setMaster('spark://192.168.2.102:7077')
    sc_conf.setAppName('my-app')
    # sc_conf.set('spark.executor.memory', '2g')  #executor memory是每个节点上占用的内存。每一个节点可使用内存
    # sc_conf.set("spark.executor.cores", '4') #spark.executor.cores：顾名思义这个参数是用来指定executor的cpu内核个数，分配更多的内核意味着executor并发能力越强，能够同时执行更多的task
    # sc_conf.set('spark.cores.max', 40)    #spark.cores.max：为一个application分配的最大cpu核心数，如果没有设置这个值默认为spark.deploy.defaultCores
    # sc_conf.set('spark.logConf', True)    #当SparkContext启动时，将有效的SparkConf记录为INFO。
    print(sc_conf.getAll())

    sc = SparkContext(conf=sc_conf)

    return sc


if __name__ == '__main__':
    sc = create_sc()
    data = sc.parallelize(enumerate(range(1000)), 10)
    data2 = data.map(lambda k: (k[0], k[1] * 2))
    print(data2.take(10))
