"""

"""
import copy

"""
贪心，先拿单位最大
"""


def max_value(goods, weight):
    # 单位商品价值最高
    goods_sort = sorted(goods, key=lambda x: x[0] / x[1], reverse=True)

    _max_value = 0
    for indx, (value, sub_weight) in enumerate(goods_sort):
        if weight >= sub_weight:
            goods_num = weight // sub_weight
            _max_value += goods_num * value
            weight = weight - (goods_num * sub_weight)

    return _max_value


if __name__ == '__main__':
    goods = [(60, 10), (100, 20), (120, 30)]  # （价值，重量）
    weight = 50
    print(max_value(goods, weight))
