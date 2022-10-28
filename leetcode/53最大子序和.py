"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

示例:

输入: [-2,1,-3,4,-1,2,1,-5,4]
输出: 6
解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

lis = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


def maxSubarray(lis):
    """
    暴力法求解，时间超时
    """
    if len(lis) == 1:
        return lis[0]
    max_current = lis[0]
    for l in range(1, len(lis) + 1):
        for i in range(len(lis) - l + 1):
            # print(lis[i:i + l])
            current = sum(lis[i:i + l])
            if current > max_current:
                max_current = current

    print(max_current)
    return max_current


def maxSubarray(nums):
    """
    贪心算法:若当前指针所指元素之和小于0，则丢弃当前元素所有的数列
    """
    pass


def maxSubarray(nums):
    """
    动态规划:若前一个元素大于0,将其加到当前元素上
    """
    pre = 0
    if len(nums) == 1:
        return nums[0]

    for i in range(len(nums)):
        if i == 0:
            pre = nums[i]
        else:
            if pre > 0:
                nums[i] = pre + nums[i]
            pre = nums[i]
    return max(nums)


if __name__ == '__main__':
    maxSubarray(lis)
