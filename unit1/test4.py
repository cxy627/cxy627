#coding:utf-8

'''
for循环打印9*9乘法表，要求输出格式如下
思路：
问题分为 表头的打印以及表体的打印
首先根据输入数字建立一个list，num = list[1:input_num]，输入数字最大为99
（此处用一个无穷循环结构实现）
第一层用for使行数row遍历list
第二层用for使计数器i遍历list
里面有三个if语句，嵌套结构
外层判断i是否等于row，如果是i打印0i|0i(如果i>=10直接打印)
内层判断i*i是否小于10，如果小于+0输出，否则直接输出
'''



input_num = 9


'''
创建列表并打印表头
'''
b = 0
num = [0]*input_num
print('    ', end='')
for a in range(0,input_num):
    num[a] = a+1
    if int(num[a]) < 10:
        print('0'+str(num[a]), end=' ')
        b += 2
    else:
        print(str(num[a]), end=' ')
        b += 1
print('\n   '+(len(num)+b)*'-')

'''
生成乘法表
'''
for row in num:
    if row < 10:
        print('0'+str(row)+'|', end=' ')
    else:
        print(str(row)+'|', end=' ')
    for i in num:
        if i*row < 10:
            print('0'+str(i*row), end=' ')
        else:
            print(str(i*row), end=' ')
    print('\n')
