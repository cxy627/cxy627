#coding=utf-8

'''
有多少个三位数（100-999）可以被17整除，将之输出
思路：
用for 遍历 100-999（xrange后一位需加一）
如果除后余数(%)为0,则输出
'''
sum = 0
for i in range(100, 1000):
    if i%17 == 0:
        sum += 1
print('总共有'+str(sum)+'个数字')
