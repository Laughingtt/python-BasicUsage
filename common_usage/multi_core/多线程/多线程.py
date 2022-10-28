import threading
import multiprocessing
import time


class Test:
    name = "tian"
    def count_number(self,i):
        print("start",i)
        time.sleep(1)
        print("end",i)

    def for_number(self):
        for i in range(10):
            self.count_number(i)

    def forever_loop(self):
        while True:
            self.for_number()
            print(self.name)

    def create_thread(self):
        t = threading.Thread(target=self.forever_loop, args=())
        t.start()


test=Test()
# t = threading.Thread(target=test.forever_loop,args=())
# t2 = multiprocessing.Process(target=test.forever_loop,args=())
test.create_thread()
print("===")
# t.start()
# t2.start()
print("===")