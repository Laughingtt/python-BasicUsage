import handout
doc = handout.Handout('handout_output/ex00_original_after', 'ex00_original_after')
"""
# 封装集合-代码原型-重构后
---
"""

class Foo:
    def __init__(self):
        """将列表属性私有，保证用户无法从外部进行访问"""
        self.__items = []
    def add(self, item):
        """
        类内部的 add() 函数依然可以使用私有属性 __items
        :param item: 要添加的元素
        :return:
        """
        self.__items.append(item)
    @property
    def items(self):
        """
        只读属性，不允许用户从外部修改列表元素
        :return: 列表属性
        """
        return tuple(self.__items)

# 客户端
foo = Foo()
foo.add('a')  # 希望客户端的操作方式
print(foo.items)  # 输出列表中所有的元素

# foo.items.append('b')  # 有安全隐患的操作方式，绕过自定义的 add() 函数
print(foo.items)  # 输出列表中所有的元素

"""
---
domkn @ 2019-08-12
"""

doc.show()
