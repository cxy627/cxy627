#coding:utf-8

'''
限定while循环和print语句输出以下样式
样式1
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5 
1 2 3 4 5 6
样式2
1 2 3 4 5 6 
1 2 3 4 5 
1 2 3 4
1 2 3
1 2
1
样式3
          1
        2 1
      3 2 1
    4 3 2 1
  5 4 3 2 1
6 5 4 3 2 1
思路：前两种样式可使用列表，while循环行数 print输出[0:row]
后一种样式可使用列表while循环行数 print输出(6-row)*2空格，然后输出[row:0]

'''

# 创建列表
i = 1
num = [0]*6
while i <= 6:
    num[i-1] = str(i)+' '
    i += 1

 # 生成样式1
print('\n样式1:\n')
i = 1
row = 1
while row <= 6:
    while i <= row:
        print(num[i-1], end='')
        i += 1
    row += 1
    i = 1
    print('\r')

# 生成样式2
print('\n样式2:\n')
i = 1
row = 1
while row <= 6:
    while i+row <= 7:
        print(num[i-1], end='')
        i += 1
    row += 1
    i = 1
    print('\r')

# 生成样式3
print('\n样式3:\n')
i = 1
row = 1
while row <= 6:
    print('  '*(6-row), end='')
    while i <= row:
        print(num[row-i], end='')
        i += 1
    row += 1
    i = 1
    print('\r')
    