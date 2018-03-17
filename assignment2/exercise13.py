# coding:utf-8
'''
涉及一个代码，可以判断字符串长度，如果长度为1额外提示，并且能检测该
字符串是不是关键字
'''
import keyword

text = input("请输入字符串:")
print("该字符串长度为%s" % len(text))
print("该字符串%s系统关键字" % {True: "是", False: "不是"}[keyword.iskeyword(text)])
