# coding:utf-8
'''
补充题1
'''


def dereplication(lst):
    for x in range(0, len(lst)):
        if x == len(lst)-1:
            yield lst[x]
            continue
        if lst[x] == lst[x+1]:
            continue
        else:
            yield lst[x]


print(list(dereplication([1, 1, 1, 2, 3, 4, 5, 6, 6])))
