import asyncio
import time

async def seq(url):
    print("正在下载 ",url)
    await asyncio.sleep(2)  #遇到阻塞必须手动挂起
    print("下载完成 ",url)

async def meq(url):
    print("正在下载 ",url)
    await asyncio.sleep(2)  #遇到阻塞必须手动挂起
    print("下载完成 ",url)

c=seq(1)
b=meq(2)
lis=[c,b]

# for i in range(5):
#     c=seq(i)
#     lis.append(c)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(lis))