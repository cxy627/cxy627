#coding:utf-8
'''
键盘输15以内的整数，输出这样的格式
          1
        2 1 2
      3 2 1 2 3
    4 3 2 1 2 3 4
  5 4 3 2 1 2 3 4 5
6 5 4 3 2 1 2 3 4 5 6
思路：
整体流程分为两大块:接收键盘输入数字并取整，输出图样
接收键盘数字后首先使用isdigit判断是否为纯数字，然后转换位整形，
并判断是否在1-15内
输出图样首先输出空格，数量为输入数字减行数，然后再输出数字金字塔的左半部分，
由行数逐渐递减直至1，最后输出右半部分，有2循环至行数。
'''

# 输入数字并检测
while True:
    print('请输入数字:', end='')
    input_num = input()
    if input_num.isdigit() == True:
        input_num = int(input_num)
        if input_num <= 15 and input_num >= 1:
            break
        else:
            print('请输入的数字在1-15之间')
            continue
    else:
        print('请输入纯数字')
        continue

# 输出表
row = 1
while row <= input_num:
    a1 = input_num-row
    while a1 > 0:
        print(' ', end=' ')
        a1 -= 1
    a2 = row
    while a2 > 0:
        print(a2, end=' ')
        a2 -= 1
    a3 = 2
    while a3 <= row:
        print(a3, end=' ')
        a3 += 1
    print('\n')
    row += 1
             