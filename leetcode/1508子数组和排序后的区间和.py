nums = [1,2,3,4]
n = 4
left = 1
right = 5

lis = []
for i in range(n):
    for j in range(i,n):
        res = sum(nums[i:j+1])
        lis.append(res)
print(sum(sorted(lis)[left-1:right]))
