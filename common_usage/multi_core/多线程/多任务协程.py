import asyncio
import time

async def request(url):
    print("正在下载 ",url)
    #在异步协程中如果出现了同步模块相关的代码，异步无法实现，如time.sleep()
    #time.sleep(2)
    #async中也有sleep方法，是基于异步的
    await asyncio.sleep(2)  #遇到阻塞必须手动挂起
    print("下载完成 ",url)

start_time=time.time()
urls=[
    "www.baidu.com",
    "www.sougou.com",
    "www.goubanjia.com"
]

#任务列表，存放多个任务对象
tasks = []
for url in urls:
    c = request(url)
    #task=asyncio.ensure_future(c)
    tasks.append(c)

loop = asyncio.get_event_loop()
#固定的语法格式，需要将任务列表封装到wait中
loop.run_until_complete(asyncio.wait(tasks))

print(time.time()-start_time)