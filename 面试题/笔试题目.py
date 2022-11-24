# !/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@company:UDAI
"""

"""
1. 存在以下列表，先对成绩排序正序，再对年龄排序倒序,可以写出多种解法: 
        student_tuples = [
        ('john', 'A', 15),
        ('jane', 'B', 12),
        ('helen', 'C', 14),
        ('bob', 'C', 13),
        ('dave', 'B', 10),]
"""


class Test1:
    @staticmethod
    def main():
        pass


"""
2. 一只青蛙要跳上n层高的台阶，一次能跳一级，也可以跳两级，请问这只青蛙有多少种跳上这个n层台阶的方法？(如果有多种解法可以写出来)
"""


class Test2:
    @staticmethod
    def main():
        pass


"""
3. 将一个五千万的数据，通过索引分区的方式，分别存入到8个文件当中, hash_code函数返回值为某个分区的区域id,比如传入"123"返回3,代表
"123"这个字符串应该存入区域3中，可通过并发的方式实现并写出测试速度。

"""
import pickle

Partitions = 8


class Test3:

    @staticmethod
    def id_create(count1=int(1e7)):
        import numpy as np
        import datatable as dt
        dt.Frame({"id": np.arange(count1)}).to_csv("id_{}.csv".format(count1))

    @staticmethod
    def hash_code(s):
        s = pickle.dumps(s)
        seed = 31
        h = len(s)
        for c in s:
            if c > 127:
                c = -256 + c
            h = h * seed
            if h > 2147483647 or h < -2147483648:
                h = (h & (2 ** 31 - 1)) - (h & 2 ** 31)
            h = h + c
            if h > 2147483647 or h < -2147483648:
                h = (h & (2 ** 31 - 1)) - (h & 2 ** 31)
        if h == 0 or h == -2147483648:
            h = 1
        return (h if h >= 0 else abs(h)) % Partitions

    @staticmethod
    def main():
        # Test3.id_create()
        print(Test3.hash_code("123"))


"""
4. Alice拥有2千万用户的数据，Bob拥有1千万用户数据，假设两方的数据id为自然数，对Alice和Bob方的数据求交集
   可使用并发对数据进行高效处理，要求在本机电脑可以正常执行。
"""


class Test4:

    @staticmethod
    def id_create(count1=int(2e7), count2=int(1e7)):
        import numpy as np
        import datatable as dt
        dt.Frame({"id": np.arange(count1)}).to_csv("id_{}.csv".format(count1))
        dt.Frame({"id": np.arange(count2)}).to_csv("id_{}.csv".format(count2))

    @staticmethod
    def main():
        # 可用于造数据
        # Test4.id_create()
        pass


if __name__ == '__main__':
    Test1.main()
    Test2.main()
    Test3.main()
    Test4.main()
