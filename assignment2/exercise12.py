#coding:utf-8
'''
有两个,分别是string.find(),string.index()，
不同点在于fing找不到会返回-1，index则会抛出vlaueerror异常
'''

a = "abcd"
b = "a"
c = "e"

print(a.find(b))
print(a.find(c))
print(a.index(b))
try:
    print(a.index(c))
except ValueError:
    print("print(a.index(c))抛出ValueError异常")