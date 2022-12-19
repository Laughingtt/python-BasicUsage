import ray
import random
import time
import math
from fractions import Fraction

# Let's start Ray
ray.init(address='127.0.0.1:9937')


# 圆中点的个数/正方形点的个数 = math.pi / 4
# pi = 4 * 圆中点的个数/正方形点的个数
@ray.remote
def pi4_sample(sample_count):
    """pi4_sample runs sample_count experiments, and returns the
    fraction of time it was inside the circle.
    """
    in_count = 0
    for i in range(sample_count):
        x = random.random()
        y = random.random()
        if x * x + y * y <= 1:
            in_count += 1
    return Fraction(in_count, sample_count)


# 单核
SAMPLE_COUNT = 1000 * 1000
start = time.time()
# future = pi4_sample.remote(sample_count=SAMPLE_COUNT)
# pi4 = ray.get(future)
# print(float(pi4 * 4))

# 多核
FULL_SAMPLE_COUNT = 60 * 10 * 1000 * 1000  # 100 billion samples!
BATCHES = int(FULL_SAMPLE_COUNT / SAMPLE_COUNT)
print(f'Doing {BATCHES} batches')
results = []
for _ in range(BATCHES):
    # results.append(pi4_sample.remote(sample_count=SAMPLE_COUNT))
    results.append(pi4_sample.options(resources={"alice": 1}).remote(sample_count=SAMPLE_COUNT))
output = ray.get(results)

pi = sum(output) * 4 / len(output)
print(float(pi), " ", abs(pi - math.pi) / pi)

end = time.time()
dur = end - start
print(f'Running {SAMPLE_COUNT} tests took {dur} seconds')