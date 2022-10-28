# -*- coding: UTF-8 -*-
""""=================================================
@Project -> File   ：Django -> 二叉树之有序列表
@IDE    ：PyCharm
@Author ：爱跳水的温文尔雅的laughing
@Date   ：2020/4/2 21:56
@Desc   ：
=================================================="""
import redis


class MyRedis(object):
    """
    ===================================================================
    =====================       MyRedis        ========================
    ===================================================================
    """
    def __init__(self):
        self.redis_conn = None
        self.redis_db = None

    def connect_to_redis(self, redis_host, redis_port=6379, db=0, password=None):
        """
        连接到Redis服务器
        """
        self.redis_db = db
        print('Executing : Connect To Redis | host={0}, port={1}, db={2}, password={3}'
                     .format(redis_host, redis_port, self.redis_db, password))
        try:
            self.redis_conn = redis.StrictRedis(
                host=redis_host, port=redis_port, db=self.redis_db, password=password)
        except Exception as ex:
            print(str(ex))
            raise Exception(str(ex))

    def redis_key_should_be_exist(self, name):
        """
        验证redis存在指定键
        """
        if not self.redis_conn.exists(name):
            print(("Redis of db%s doesn't exist in key [ %s ]." % (self.redis_db, name)))

    def redis_key_should_not_be_exist(self, name):
        """
        验证redis不存在指定键
        """
        if self.redis_conn.exists(name):
            print(("Redis of db%s exist in key [ %s ]." % (self.redis_db, name)))

    def getkeys_from_redis_bypattern(self, pattern, field=None):
        """
        获取redis所有键值
        """
        keys_list = list()
        print('Executing : Getall Key | %s' % pattern)
        if field is None:
            return self.redis_conn.keys(pattern)
        else:
            keys = self.redis_conn.keys(pattern)
            for key in keys:
                if not self.redis_conn.hget(key, field) is None:
                    keys_list.append(key)
            return keys_list

    # ==========================  String Type =============================
    def get_from_redis(self, name):
        """
        获取redis数据
        """
        print('Executing : Get Key | %s' % name)
        return self.redis_conn.get(name)

    def del_from_redis(self, name):
        """
        删除redis中的任意数据类型
        """
        return self.redis_conn.delete(name)

    def set_to_redis(self, name, data, expire_time=0):
        """
        设置redis执行key的值
        """
        return self.redis_conn.set(name, data, expire_time)

    def append_to_redis(self, name, value):
        """
        添加数据到redis
        """
        return self.redis_conn.append(name, value)

        # ==========================  Hash Type  ==========================
    def hgetall_from_redis(self, name):
        """
        获取redis hash所有数据
        """
        print('Executing : Hgetall Key | %s' % name)
        return self.redis_conn.hgetall(name)

    def hget_from_redis(self, name, key):
        """
        获取redis hash指定key数据
        """
        print('Executing : Hget Key | %s' % name)
        return self.redis_conn.hget(name, key)

    def hset_to_redis(self, name, key, data):
        """
        设置redis指定key的值
        """
        print(('Executing : Hset Redis | name={0}, key={1}, data={2}'
                     .format(name, key, data)))
        return self.redis_conn.hset(name, key, data)

    def hdel_to_redis(self, name, *keys):
        """
        删除redis指定key的值
        """
        print('Executing : Hdel Key | ', *keys)
        self.redis_conn.hdel(name, *keys)

    # =========================  ZSet Type  ================================
    def get_from_redis_zscore(self, name, values):
        """
        获取name对应有序集合中 value 对应的分数
        """
        try:
            return int(self.redis_conn.zscore(name, values))
        except:
            return self.redis_conn.zscore(name, values)

    def get_from_redis_zrange(self, name, start=0, end=10):
        """
        按照索引范围获取name对应的有序集合的元素
        """
        return self.redis_conn.zrange(name, start, end, desc=False, withscores=True, score_cast_func=int)

    def del_from_redis_zrem(self, name, values):
        """
        删除name对应的有序集合中值是values的成员
        """
        return self.redis_conn.zrem(name, values)

    def add_from_redis_zadd(self, name, value, score):
        """
        在name对应的有序集合中添加一条。若值存在，则修改对应分数。
        """
        return self.redis_conn.zadd(name, {value: score})

    def count_from_redis_zcard(self, name):
        """
        获取name对应的有序集合元素的数量
        """
        return self.redis_conn.zcard(name)


if __name__ == '__main__':
    print('This is test.')
    mr = MyRedis()