"""
优点：效率高
缺点：必须是有序列表
"""


def func(lis, n):
    low = 0
    high = len(lis) - 1
    while low <= high:
        mid = (low + high) // 2
        num = lis[mid]
        if num == n:
            return mid
        elif num > n:
            high = mid - 1
        elif num < n:
            low = mid + 1
    return None


lis = [i for i in range(100)]


def search(nums, target):
    if target not in nums:
        return -1
    length = len(nums)
    current_index = int(length / 2)
    while True:
        current_value = nums[current_index]
        if current_value == target:
            return current_index
        elif current_value < target:
            current_index = current_index + int((length - current_index) / 2)
        else:
            current_index = int(current_index / 2)


# lis = [-1, 0, 3, 5, 9, 12]
# res = search(lis, 3)
# print(res)

i = 0
while i < 1000:
    while True:
        if i == 4:
            print(123)
            break
        i += 1
        print(i)


