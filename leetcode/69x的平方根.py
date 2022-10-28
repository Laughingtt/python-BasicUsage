"""
实现 int sqrt(int x) 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

示例 1:

输入: 4
输出: 2
示例 2:

输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sqrtx
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def mySrt(num):
    """
    二分法
    """
    if num == 0:
        return 0
    left = 1
    right = num // 2
    while left < right:
        # 注意：这里一定取右中位数，如果取左中位数，代码可能会进入死循环
        # mid = left + (right - left + 1) // 2
        mid = (left + right + 1) >> 1  # 取右中位数
        print("mid", mid)
        square = mid * mid
        if square > num:
            right -= 1
        else:
            left = mid
        print("left", left)
    return left


mySrt(8)

class Solution(object):
    def mySqrt(self, x):
        """
        已知牛顿法递推公式：Xn+1 = Xn - f(Xn)/f'(Xn).
        带入f'(x) = -2x.
        得：
        Xn+1 = Xn +(num - Xn ^ 2)/2Xn
        = (num + Xn ^ 2) / 2Xn
        = (num / Xn + Xn) / 2.

        用代码表示则为num = (num + x / num) / 2.

        """
        num = x
        while num * num > x:
            num = (num + x // num) // 2
        return num
