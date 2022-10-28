import threading
def print_hello(n):
    import time
    time.sleep(1)
    print(n)

print("start")
lis=[]
for i in range(10):
    p = threading.Thread(target=print_hello,args=(i,))
    p.start()
    lis.append(p)

for t in lis:
    t.join()

print("finished")