"""
58. 最后一个单词的长度
给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。



示例:

输入: "Hello World"
输出: 5
"""

s = "HelloWorld "
s = "b   a    "
s = " "
def lengthLastWord(s):
    """
    将s按空格切分转化为列表，如果最后一位存在时返回最后一位的长度，最后一位是空格的话用列表生成式和三目取出大于0的字符串再取最后面的词
    """
    if " " in s:
        s_list = s.split(" ")
        last = s_list[-1]
        if len(last)>0:
            return len(s_list[-1])
        else:
            left_list = [i for i in s_list if len(i) > 0]  #列表生成式和三目表达式
            if len(left_list)>0:
                return len(left_list[-1])
            else:
                return 0
    else:
        return len(s)


if __name__ == '__main__':
    print(lengthLastWord(s))