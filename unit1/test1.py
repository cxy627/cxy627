#coding:utf-8

'''
第一-第四讲作业
写出以下逻辑表达式的值
附百度的运算符优先顺序表
Lambda  #运算优先级最低
逻辑运算符: or
逻辑运算符: and
逻辑运算符:not
成员测试: in, not in
同一性测试: is, is not
比较: <,<=,>,>=,!=,==
按位或: |
按位异或: ^
按位与: &
移位: << ,>>
加法与减法: + ,-
乘法、除法与取余: *, / ,%
正负号: +x,-x
'''

QUESTION1 = False and None#答案False
QUESTION2 = 0 and None or {} and []#答案{}
QUESTION3 = True and None or () and []#答案()
QUESTION4 = 0 or None and () or []#答案[]
QUESTION5 = True or None and () or []#答案True
QUESTION6 = 1 or None and 'a' or 'b'#答案1

print("第一题答案是", end='')
print(QUESTION1)
print("第二题答案是", end='')
print(QUESTION2)
print("第三题答案是", end='')
print(QUESTION3)
print("第四题答案是", end='')
print(QUESTION4)
print("第五题答案是", end='')
print(QUESTION5)
print("第六题答案是", end='')
print(QUESTION6)
