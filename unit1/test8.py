#coding:utf-8

'''
首先输入值改为5，完成正向三角后，步骤相反的操作一遍即可
'''
input_num = 5
row = 1
while row <= input_num:
    a1 = input_num-row
    while a1 > 0:
        print(' ', end=' ')
        a1 -= 1
    a2 = row
    while a2 > 0:
        print('*', end=' ')
        a2 -= 1
    a3 = 2
    while a3 <= row:
        print('*', end=' ')
        a3 += 1
    print('\n')
    row += 1
    
row -= 2
while row > 0:
    a1 = input_num-row
    while a1 > 0:
        print(' ', end=' ')
        a1 -= 1
    a2 = row
    while a2 > 0:
        print('*', end=' ')
        a2 -= 1
    a3 = 2
    while a3 <= row:
        print('*', end=' ')
        a3 += 1
    print('\n')
    row -= 1
