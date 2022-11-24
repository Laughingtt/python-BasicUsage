#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author： tian
# datetime： 2022/11/23 4:10 PM 
# ide： PyCharm

import asyncio


async def test(i):
    print('test_1', i)
    await asyncio.sleep(1)
    print('test_2', i)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    tasks = [test(i) for i in range(3)]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
