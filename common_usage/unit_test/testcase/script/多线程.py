import threading


# 判断值是否为偶数
def is_even(value):
    if value % 2 == 0:
        return True
    else:
        return False


class MyThread(threading.Thread):
    def __init__(self, func, args=()):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args

    def run(self):
        self.result = self.func(*self.args)  # 在执行函数的同时，把结果赋值给result,
        # 然后通过get_result函数获取返回的结果

    def get_result(self):
        try:
            return self.result
        except Exception as e:
            return None


result = []
threads = []
for i in range(10):
    t = MyThread(is_even, args=(i,))
    t.start()
    threads.append(t)
for t in threads:
    t.join()  # 一定执行join,等待子进程执行结束，主进程再往下执行
    result.append(t.get_result())
