import pandas as pd
from timeit import timeit

ans = input('输入答案:')
code = 'ABCD'


def zc(n):
    c = 0
    while n > 0:
        n //= 4
        c += 1
    return c


def df(n, h):
    s = ''
    k = 4 ** (h - 1)
    for i in range(h):
        s = s + str(n // k)
        n = n % k
        k = k // 4
    return s


def pz(n):
    ret = []
    for i in range(4 ** n):
        for h in range(zc(i), 5):
            s = df(i, h)
            res = ''
            for j in s:
                res += code[int(j)]
            ret.append(res)
    return ret


def test():
    key = pz(5)[1:]
    a = len(key)
    b = len(ans)
    dic = {}
    for k in range(a):
        c = 0
        d = len(key[k])
        for i in range(b):
            m = ans[i]
            n = key[k][i % d]
            if m == n:
                c += 1
        res = round(c / b * 100, 3)
        dic[key[k]] = res
        print('全选:' + str(key[k]) + '准确率为:' + str(res) + "%")


#
# se = pd.Series(dic)
# se = se.sort_values(ascending=False)
# se = se.astype(str) + '%'
# se.name = '正确率'
# print(se)
# se.to_excel('dda.xlsx')


print(f"with:{timeit(test, number=10000)}")
