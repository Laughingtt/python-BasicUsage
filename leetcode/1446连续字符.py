"""
1446. 连续字符
给你一个字符串 s ，字符串的「能量」定义为：只包含一种字符的最长非空子字符串的长度。

请你返回字符串的能量。



示例 1：

输入：s = "leetcode"
输出：2
解释：子字符串 "ee" 长度为 2 ，只包含字符 'e' 。
"""


class Solution:
    def maxPower(self, s: str) -> int:
        lis = []
        number = 1
        for i in range(1,len(s)):
            if s[i] != s[i-1]:
                number = 1
            else:
                number +=1
                lis.append(number)
        return max(lis) if len(lis)>0 else 1

solution = Solution()
print(solution.maxPower("tourist"))
