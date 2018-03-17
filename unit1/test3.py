#coding:utf-8

'''
循环嵌套的方式计算连续整数之和，要求输出样式如下
如果输入数字6输出连续6个数字之和
1=1
1+ 2=3
1+ 2+ 3=6
1+ 2+ 3+ 4=10
1+ 2+ 3+ 4+ 5=15 
1+ 2+ 3+ 4+ 5+ 6=21
思路:
将问题拆分为两块，输出前面的算式以及后面的答案
最外层为for循环,由1至输入数字
次外层为for循环，由1至行数
内部为一个个判断语句
当计数器i小于行数，输出i+'+ '
否则当计数器i等于行数，输出i+'='+累加器sum
'''
print('请输入数字:', end='')
num = int(input())

for row in range(1, (num+1)):
    sum = 0
    for i in range(1, (row+1)):
        sum += i
        if i < row:
            print(str(i)+'+ ', end='')
        else:
            print(str(i)+'='+str(sum))
