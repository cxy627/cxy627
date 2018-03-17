#coding:utf-8

'''
编写程序生成以下算术列
1 *8+1=9
1 2 *8+2=98
1 2 3 *8+3=987
1 2 3 4 *8+4=9876
1 2 3 4 5 *8+5=98765
1 2 3 4 5 6 *8+6=987654
1 2 3 4 5 6 7 *8+7=9876543
1 2 3 4 5 6 7 8 *8+8=98765432
1 2 3 4 5 6 7 8 9 *8+9=987654321
思路：
大循环for循环i遍历1至行数row，然后使用for循环i遍历1至行数row，每次循环将i转换为字符串与number1（原本为''）相加，整形
化后乘8加行数赋值给sum，打印算术列即可
'''
#无空格
print('无空格')
input_num = 9
for row in range(1, input_num+1):
    number1 = ''
    for i in range(1, row+1):
        number1 += str(i)
    sum = int(number1)*8+input_num
    print(number1+'*8+'+str(input_num)+'='+str(sum))

#有空格
print('有空格')
input_num = 9
for row in range(1, input_num+1):
    number1 = echo1 = ''
    for i in range(1, row+1):
        number1 += str(i)
        echo1 += str(i)+' '
    sum = int(number1)*8+input_num
    print(echo1+'*8+'+str(input_num)+'='+str(sum))
    