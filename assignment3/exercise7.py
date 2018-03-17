# coding:utf-8
'''
习题11-3
'''


def max2(*innum, **innum1):
    maxlist = []
    for inmaxnum in innum:
        try:
            maxlist.append(int(inmaxnum))
        except ValueError:
            print("所输入的%s非数字,已忽略" % inmaxnum)
    for inmaxnum in innum1.values():
        try:
            maxlist.append(int(inmaxnum))
        except ValueError:
            print("所输入的%s非数字,已忽略" % inmaxnum)
    maxlist.sort
    return maxlist.pop()


def min2(*innum, **innum1):
    minlist = []
    for inminnum in innum:
        try:
            minlist.append(int(inminnum))
        except ValueError:
            print("所输入的%s非数字,已忽略" % inminnum)
    for inminnum in innum1.values():
        try:
            minlist.append(int(inminnum))
        except ValueError:
            print("所输入的%s非数字,已忽略" % inminnum)
    minlist.sort
    return minlist.pop(0)


print(max2(1, 23, 4, "efw", jir=56,), end='\n\n')
print(min2(1, 23, 4, "efw", jir=56,))
