

#1,1,2,3,5,8  斐波拉契数列
def fib(num):
    if num<=2:
        return 1
    else:
        return fib(num-1)+fib(num-2)


# print(fib(10))




