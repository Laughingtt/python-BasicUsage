"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true

示例 2:

输入: "()[]{}"
输出: true
"""

s = "()"
s = "()[]{}"
s = "([)]"
s = "([)]"
s = "{[]}"
s = "}"
s = "(])"

def solution(s):
    braces_dict = {"(":")","{":"}","[":"]"}
    stick_list = []
    for i in s:
        if i in braces_dict.keys():
            stick_list.append(i)
            continue
        if i in braces_dict.values() and len(stick_list)>0:
            if braces_dict[stick_list[-1]]==i:
                stick_list.pop()
            else:
                return False
        else:
            return False
    if len(stick_list)==0:
        print("已清空列表")
        return True
    else:
        print("列表还剩下:{}".format(stick_list))
        return False

solution(s)