# coding:utf-8
'''
习题11-9
'''
from functools import reduce
from random import randint


def average(sequence):
    return(reduce(lambda x, y: x+y, sequence)/len(sequence))


inlist = [randint(0, 10) for i in range(0, 5)]
print('输入序列%s' % inlist)
print(average(inlist))
