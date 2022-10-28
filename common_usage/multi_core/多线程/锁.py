import threading
import time

lock=threading.Lock() #实例化一把锁

def seq(x):
    global num
    lock.acquire()   #获得锁
    num+=x
    time.sleep(0.1)
    num-=x
    lock.release()  #释放锁

num=0
i_obj=[]
for i in range(100):
    t=threading.Thread(target=seq,args=(i,))  #声明线程数
    t.start()   #开始线程
    i_obj.append(t)

for t in i_obj:  #加入阻塞
    t.join()

print("finished",num)