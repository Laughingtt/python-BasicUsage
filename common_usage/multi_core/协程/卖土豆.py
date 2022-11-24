#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： tian
# datetime： 2022/11/23 4:27 PM 
# ide： PyCharm
import time


class Potato:
    @classmethod
    def make(cls, num, *args, **kws):
        potatos = []
        for i in range(num):
            potatos.append(cls.__new__(cls, *args, **kws))
        return potatos


def take_potatos(num):
    count = 0
    while True:
        if len(all_potatos) == 0:
            time.sleep(0.1)
        else:
            potato = all_potatos.pop()
            yield potato
            count += 1
            if count == num:
                break


def buy_potatos():
    bucket = []
    for p in take_potatos(50):
        bucket.append(p)
        print(bucket)


"""
异步
"""
import asyncio
import random


async def take_potatos2(num):
    count = 0
    while True:
        if len(all_potatos) == 0:
            await ask_for_potato()
        potato = all_potatos.pop()
        yield potato
        count += 1
        if count == num:
            break


async def ask_for_potato():
    await asyncio.sleep(random.random())
    all_potatos.extend(Potato.make(random.randint(1, 10)))


async def buy_potatos2():
    bucket = []
    async for p in take_potatos2(50):
        bucket.append(p)
        print(f'Got potato {id(p)}...')


"""
对应到代码中，就是迭代一个生成器的模型，显然，当货架上的土豆不够的时候，这时只能够死等，而且在上面例子中等多长时间都不会有结果（因为一切都是同步的）
"""


def test1():
    buy_potatos()


def test2():
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(buy_potatos2())
    loop.close()


if __name__ == '__main__':
    all_potatos = Potato.make(5)
    test2()
