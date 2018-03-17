#coding:utf-8
'''

'''
import random
rand_num = []
for i in range(100):
    rand_num.append(random.randint(0,2**31-1))
rand_num.sort(reverse=False)
print(rand_num)