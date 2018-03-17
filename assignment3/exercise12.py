# coding:utf-8
'''
'''


def leapyear1(sequence):
    return list(filter(lambda x: not bool(x % 4), sequence))


def leapyear2(sequence):
    return [item for item in sequence if not bool(item % 4)]


print(leapyear1([1953, 2000, 2005, 2008, 3008]))
print(leapyear2([1953, 2000, 2005, 2008, 3000]))
