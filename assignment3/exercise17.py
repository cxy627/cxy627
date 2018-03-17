# coding:utf-8
'''
习题11-13
'''
from functools import reduce
from time import time


def timeit(func):
    def intimeit(*arg):
        starttime = time()
        result = func(*arg)
        endtime = time()
        print("共耗时%s秒" % (endtime-starttime))
        return result
    return intimeit


def mult1(x, y):
    return x*y


@timeit
def mult2(endnum):
    return reduce(mult1, range(1, endnum+1))


@timeit
def mult3(endnum):
    return reduce(lambda x, y: x*y, range(1, endnum+1))


@timeit
def mult4(endnum):
    def mathnum(endnum, nownum=1, result=1):
        if nownum == 1:
            return mathnum(endnum, nownum+1, result)
        elif nownum != endnum:
            result *= nownum*(nownum-1)
            return mathnum(endnum, nownum+1, result)
        else:
            return result
    return mathnum(endnum)


print(mult1(1, 100))
print("任务1运算时长")
mult2(10000)
print("任务2运算时长")
mult3(10000)
print("任务3运算时长")
mult4(990)
