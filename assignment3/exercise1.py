# coding:utf-8
'''
创造一个随机数序列，并返回中位数
'''
from random import uniform, randint
from math import floor


def createlist():
    randlist = []
    for i in range(0, randint(2, 10)):
        randlist.append(uniform(0, 1000))
    print("本次寻找的随机列表为%s" % str(randlist))
    return randlist


def findmid(findlist):
    findlist.sort
    if len(findlist) % 2:
        # 长度为奇数
        midnum = findlist[floor(len(findlist)/2)]
    else:
        # 长度为偶数
        midnum = 0.5 * (findlist[len(findlist)//2-1] +
                        findlist[len(findlist)//2])
    print("本列表的中位数为:%s" % midnum)
    return None


def main():
    findmid(createlist())


if __name__ == '__main__':
    main()
