#coding:utf-8
'''
'''
import string

lower = string.ascii_lowercase
upper = string.ascii_uppercase
done_str = str()

change_str = input("请输入字符串:")
for i in change_str:
    index_i = lower.find(i)
    if index_i >= 0:
        done_str += upper[index_i]
    else:
        index_i = upper.find(i)
        if index_i >= 0:
            done_str += lower[index_i]
        else:
            done_str += i 
    index_i = -1
print(done_str)