"""
找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class _Solution:
    def findRepeatNumber(self, nums) -> int:
        list_count = {}
        for i in nums:
            if i not in list_count:
                list_count[i]=1
            else:
                list_count[i]+=1
        res_list = [k for k,v in list_count.items() if v>=2]
        return res_list[0] if res_list else None


class Solution:
    def findRepeatNumber(self, nums) -> int:
        nums_set = set()
        for i in nums:
            if i not in nums_set:
                nums_set.add(i)
            else:
                return i





if __name__ == '__main__':
    s = Solution()
    print(s.findRepeatNumber([2, 3, 1, 0, 2, 5, 3]))