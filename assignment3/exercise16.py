# coding:utf-8
'''
习题11-12
'''
from time import clock


def timeit(func):

    def intimeit():
        clock()
        result = func()
        print("共耗时%s秒" % clock())
        return result
    return intimeit


@timeit
def por():
    i = 0
    while i <= 10010:
        i += 1
    return i


por()
