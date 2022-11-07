import ray
import numpy as np

ray.init()


@ray.remote
def f(arr):
    # arr = arr.copy()  # Adding a copy will fix the error.
    arr[0] = 1


ray.get(f.remote(np.zeros(100)))
# ray.exceptions.RayTaskError(ValueError): ray::f()
#   File "test.py", line 6, in f
#     arr[0] = 1
# ValueError: assignment destination is read-only


"""
为避免此问题，如果需要对其进行变异，您可以在目标位置手动复制数组 ( )。请注意，这实际上类似于禁用 Ray 提供的零拷贝反序列化功能。arr = arr.copy()
"""
