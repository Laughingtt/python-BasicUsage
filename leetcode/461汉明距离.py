"""
输入: x = 1, y = 4

输出: 2

解释:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑

上面的箭头指出了对应二进制位不同的位置。

"""
x = bin(1)[2:]
y = bin(4)[2:]
if len(x) > len(y):
    y = y.rjust(len(x),'0')
else:
    x = x.rjust(len(y),'0')
print(x,y)
count=0
for i,j in zip(x,y):
    if i!=j:
        count+=1

print(count)