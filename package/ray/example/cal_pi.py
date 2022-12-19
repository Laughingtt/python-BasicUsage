import ray
import math
import time
import random

# ray.init(address="10.10.10.241:9937")
ray.init(address="127.0.0.1:9937")


@ray.remote
class ProgressActor:
    def __init__(self, total_num_samples: int):
        self.total_num_samples = total_num_samples
        self.num_samples_completed_per_task = {}

    def report_progress(self, task_id: int, num_samples_completed: int) -> None:
        self.num_samples_completed_per_task[task_id] = num_samples_completed

    def get_progress(self) -> float:
        return (
                sum(self.num_samples_completed_per_task.values()) / self.total_num_samples
        )


@ray.remote
def sampling_task(num_samples: int, task_id: int,
                  progress_actor: ray.actor.ActorHandle) -> int:
    num_inside = 0
    for i in range(num_samples):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        if math.hypot(x, y) <= 1:
            num_inside += 1

        # Report progress every 1 million samples.
        if (i + 1) % 1_000_000 == 0:
            # This is async.
            progress_actor.report_progress.remote(task_id, i + 1)

    # Report the final progress.
    progress_actor.report_progress.remote(task_id, num_samples)
    return num_inside


# Change this to match your cluster scale.
NUM_SAMPLING_TASKS = 24
NUM_SAMPLES_PER_TASK = 10_000_000
TOTAL_NUM_SAMPLES = NUM_SAMPLING_TASKS * NUM_SAMPLES_PER_TASK

# Create the progress actor.
progress_actor = ProgressActor.options(resources={"alice": 1}).remote(TOTAL_NUM_SAMPLES)

results = [
    # sampling_task.remote(NUM_SAMPLES_PER_TASK, i, progress_actor)
    sampling_task.options(resources={"bob": 1}).remote(NUM_SAMPLES_PER_TASK, i, progress_actor)
    for i in range(NUM_SAMPLING_TASKS)
]

# Query progress periodically.
while True:
    progress = ray.get(progress_actor.get_progress.remote())
    print(f"Progress: {int(progress * 100)}%")

    if progress == 1:
        break

    time.sleep(1)

# Get all the sampling tasks results.
"""
Monte Carlo 方法估计 π 的值，该方法 通过在 2x2 正方形内随机采样点来工作。
我们可以使用以原点为中心的单位圆内包含的点的比例来估计圆的面积与正方形面积的比值
。鉴于我们知道真实比率为 π/4，我们可以将估计的比率乘以 4 来近似 π 的值。我们为计算该近似值而采样的点越多，该值应该越接近 π 的真实值。
"""
total_num_inside = sum(ray.get(results))
pi = (total_num_inside * 4) / TOTAL_NUM_SAMPLES
print(f"Estimated value of π is: {pi}")
