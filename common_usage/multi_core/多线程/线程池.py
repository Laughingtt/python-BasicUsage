import time
from multiprocessing import Pool
t1 = time.time()

def seq(string):
    print(string, "star :%.f s" % (time.time()))
    time.sleep(2)
    print(string, "end :%.f s" % (time.time()))
    t1 = time.time()
    return string,string


lis = ["A", "B", "C", "D"]
pool = Pool(4)
ret = pool.map(seq, lis)
print("all finished :%.f s" % (time.time() - t1))
print(ret)