#coding=utf-8

'''
将上题方法1输出图形替换为*即可
'''

input_num = 6
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
    