import threading
import time

def run(n):
   semaphore.acquire()  # 获取信号，信号可以有多把锁
   time.sleep(3)  # 等待一秒钟
   print("run the thread: %s\n" % n)
   semaphore.release()  # 释放信号
t_objs = []
if __name__ == '__main__':
   semaphore = threading.BoundedSemaphore(5)  # 声明一个信号量，最多允许5个线程同时运行
   for i in range(20):  # 运行20个线程
       t = threading.Thread(target=run, args=(i,))  # 创建线程
       t.start()  # 启动线程
       t_objs.append(t)
for t in t_objs:
   t.join()
print('>>>>>>>>>>>>>')