"""
田健 2022.11.15


g(i) = f(i-1) * f(n-i)
n =3 i=1
f(0) = 1
g(1) = f(0) * f(2) = 2

n =3 i =2
g(2) = f(1) * f(1) = 1

n =3 i=3
g(3) = f(2) * f(1) = 2

f(n) = g(1)+....g(i)+....+g(n)

"""

f_dict = {0: 1, 1: 1, 2: 2}


def compute_g(index_i, n):
    return compute_f(index_i - 1) * compute_f(n - index_i)


def compute_f(n):
    if n in f_dict:
        return f_dict.get(n)
    else:
        g_res = 0
        for index_i in range(1, n + 1):
            g_res += compute_g(index_i, n)
        if n not in f_dict:
            f_dict[n] = g_res
        return g_res


if __name__ == '__main__':
    n = 18
    r = compute_f(n)
    print(r)
    """
    n=4 r= 14
    n=5 r= 42
    n=18 r= 477638700
    """
