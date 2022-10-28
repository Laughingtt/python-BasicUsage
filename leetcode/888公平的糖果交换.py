"""
888. 公平的糖果交换
爱丽丝和鲍勃有不同大小的糖果棒：A[i] 是爱丽丝拥有的第 i 块糖的大小，B[j] 是鲍勃拥有的第 j 块糖的大小。

因为他们是朋友，所以他们想交换一个糖果棒，这样交换后，他们都有相同的糖果总量。（一个人拥有的糖果总量是他们拥有的糖果棒大小的总和。）

返回一个整数数组 ans，其中 ans[0] 是爱丽丝必须交换的糖果棒的大小，ans[1] 是 Bob 必须交换的糖果棒的大小。

如果有多个答案，你可以返回其中任何一个。保证答案存在。



示例 1：

输入：A = [1,1], B = [2,2]
输出：[1,2]
示例 2：

输入：A = [1,2], B = [2,3]
输出：[1,2]

"""
import copy

A = [1, 1]
B = [2, 2]


def func(A, B):
    """
    超出时间限制
    """
    for a in range(len(A)):
        for b in range(len(B)):
            new_a = copy.deepcopy(A)
            new_b = copy.deepcopy(B)
            new_a[a] = B[b]
            new_b[b] = A[a]
            if sum(new_a) == sum(new_b):
                return [A[a], B[b]]



class Solution:
    def fairCandySwap(self, A, B):
        sa, sb = sum(A), sum(B)
        diff = (sa - sb) / 2
        A.sort()
        B.sort()
        i, j = 0, 0
        while A[i] - B[j] != diff:
            if A[i] - B[j] > diff:
                j += 1
            else:
                i += 1
        return [A[i], B[j]]
