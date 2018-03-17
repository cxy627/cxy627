#coding:utf-8
'''
'''
import string

lower = string.ascii_lowercase*2
upper = string.ascii_uppercase*2
done_str = str()

change_str = input("请输入需要加密/解密的字符串:")

while True:
    choice_in = input("输入1加密，2解密:")
    if choice_in == "1":
        choice = 13
        break
    elif choice_in == "2":
        choice = -13
        break
    else:
        print("请输入正确数字")
for i in change_str:
    index_i = lower.find(i)
    if index_i >= 0:
        done_str += lower[index_i + choice]
    else:
        index_i = upper.find(i)
        if index_i >= 0:
            done_str += upper[index_i + choice]
        else:
            done_str += i 
    index_i = -1
print(done_str)