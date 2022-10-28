# -*- coding: UTF-8 -*-
""""=================================================
@Project -> File   ：Django -> 二叉树之有序列表
@IDE    ：PyCharm
@Author ：爱跳水的温文尔雅的laughing
@Date   ：2020/4/2 21:56
@Desc   ：
=================================================="""

import redis

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.Redis(connection_pool=pool)
r.set('food', 'mutton', ex=3)    # key是"food" value是"mutton" 将键值对存入redis缓存
print(r.get('food'))  # mutton 取出键food对应的值