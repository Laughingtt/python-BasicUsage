nums = [1,2,3,1,1,3]
nums = [1,1,1,1]

count = 0
for idx,num in enumerate(nums):
    for number in nums[idx+1:]:
        if num ==number:
            count+=1

print(count)