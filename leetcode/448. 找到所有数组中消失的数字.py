# !/usr/bin/python
# -*- coding: UTF-8 -*-

"""
@company:UDAI
@author:tianjian
@file:448. 找到所有数组中消失的数字.py
@time:2021/08/15

"""

"""
给你一个含 n 个整数的数组 nums ，其中 nums[i] 在区间 [1, n] 内。请你找出所有在 [1, n] 范围内但没有出现在 nums 中的数字，并以数组的形式返回结果。

 

示例 1：

输入：nums = [4,3,2,7,8,2,3,1]
输出：[5,6]
示例 2：

输入：nums = [1,1]
输出：[2]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def findDisappearedNumbers(self, nums):
        n = len(nums)
        for num in nums:
            # 题目中nums内从1到n全存在，遍历的话，存在的值应该都在nums内，不在的直接可以找出来
            x = (num - 1) % n
            nums[x] += n

        ret = [i + 1 for i, num in enumerate(nums) if num <= n]
        return ret


s = Solution()
s.findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1])
