# coding:utf-8
'''
习题11-14
'''


def fbnq(N, lastnum=1, nownum=1, counter=2):
    if N <= 2:
        return 1
    lastnum, nownum = nownum, lastnum
    nownum += lastnum
    counter += 1
    if N == counter:
        return nownum
    else:
        return fbnq(N, lastnum, nownum, counter)


print(fbnq(9))
