import asyncio

#async修饰函数，调用之后的一个协程对象
async def request(url):   
    print("正在请求的url",url)
    print("请求成功",url)
    return url
c=request("www.baidu.com")

#创建事件循环对象
# loop = asyncio.get_event_loop()

#将协程对象注册到loop中然后启动
# loop.run_until_complete(c)

#task使用  #显示状态
# loop = asyncio.get_event_loop() 
# task = loop.create_task(c)   #用定义的时间循环loop
# print(task)
# loop.run_until_complete(task)
# print(task)

#future
# loop = asyncio.get_event_loop()
# task = asyncio.ensure_future(c)  #直接用asyncio里方法
# print(task)
# loop.run_until_complete(task)
# print(task)

#绑定回调
def callback_func(task):
    #result返回的是任务对象中封装的函数的返回值
    print("result :",task.result())

loop = asyncio.get_event_loop()
task = asyncio.ensure_future(c)
#将回调函数绑定到任务对象中
task.add_done_callback(callback_func)  
loop.run_until_complete(task)