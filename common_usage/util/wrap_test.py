from functools import wraps
import inspect
import time


def log_elapsed(func):
    func_name = func.__name__

    @wraps(func)
    def _fn(*args, **kwargs):
        t = time.time()
        name = f"{func_name}#{kwargs['func_tag']}" if 'func_tag' in kwargs else func_name
        rtn = func(*args, **kwargs)
        frame = inspect.getouterframes(inspect.currentframe(), 2)
        print(f"{frame[1].filename.split('/')[-1]}:{frame[1].lineno} call {name}, takes {time.time() - t}s")
        return rtn

    return _fn


@log_elapsed
def func(name):
    print("my name is {}".format(name))


func("tian")
