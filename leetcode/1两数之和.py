nums = [2, 7, 11, 15]
target = 9
for i in range(len(nums)):
    lis = nums[i+1:]
    for j in range(len(lis)):
        if nums[i] + lis[j] == target:
            print(i,j+j+1)

