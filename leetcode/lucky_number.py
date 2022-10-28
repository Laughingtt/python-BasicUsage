# n,x,y,z = map(int,input().strip().split())

def func(n,x,y,z):
    count=0
    for i in range(1,n+1):
        if i%x==0 or i%y==0 or i%z==0:
            count+=1
    print(count)

def func2(n,x,y,z):
    count=0
    count+=n//x
    count+=n//y
    count+=n//z
    import math
    x_y=x*y//math.gcd(x,y)
    x_z=x*z//math.gcd(x,z)
    z_y=z*y//math.gcd(z,y)
    x_y_z=x_y*x_z//math.gcd(x_y,x_z)
    count-=n//x_y
    count-=n//x_z
    count-=n//z_y
    count+=n//x_y_z
    print(count)
n,x,y,z = map(int,input().strip().split())
func2(n,x,y,z)