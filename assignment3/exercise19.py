# coding:utf-8
'''
习题11-15
'''


def resstr(string):
    if len(string) == 1:
        print(string)
    else:
        print(string[-1], end='')
        resstr(string[:-1])


resstr("abcdef")


def qhstr(string):
    if len(string) <= 2:
        print(string)
    else:
        print(string[0]+string[-1], end='')
        qhstr(string[1:-1])


qhstr("1234567")
