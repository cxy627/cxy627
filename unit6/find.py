#coding:utf-8
'''
'''

import string

largeStr = string.ascii_letters
print("请输入测试字符",end='')
test = input()

if largeStr.find(test) >= 0:
    print("包含")
else:
    print("不包含")

