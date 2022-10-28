"""
28. 实现 strStr()
实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

示例 1:

输入: haystack = "hello", needle = "ll"
输出: 2
示例 2:

输入: haystack = "aaaaa", needle = "bba"
输出: -1
"""


class Solution:
    def str_Str(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            # print(haystack.index(needle))
            for i in range(len(haystack)-len(needle)+1):
                if haystack[i:i+len(needle)]==needle:
                    print(i)
                    return i
        else:
            print(-1)
            return -1


solution = Solution()
solution.str_Str("hl2ello", "ll")
