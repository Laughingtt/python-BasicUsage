"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

1,2,3
"""

#1
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n - 2) + self.climbStairs(n - 1)


#2
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=dp[i-2]+dp[i-1]
        return dp[n]

s = Solution()
print(s.climbStairs(4))

#3
class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:return n
        if n==2:return n
        a,b,res = 1,2,0
        for i in range(3,n+1):
            res = a+b
            a=b
            b=res
        return res

s = Solution()
print(s.climbStairs(4))