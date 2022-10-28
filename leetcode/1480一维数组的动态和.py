lis = [1,2,3,4]

b =[sum(lis[:i+1]) for i in range(len(lis))]
print(b)