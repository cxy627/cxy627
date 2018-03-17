#coding:utf-8
'''
'''

dict_one = {1:"one",2:"two",3:"three",4:"four",5:"five"
,6:"six",7:"seven",8:"eight",9:"nine",10:"ten",11:"eleven",
12:"twelve",13:"thirteen",14:"fourteen",15:"fifteen",
16:"sixteen",17:"seventeen",18:"eighteen",19:"nineteen"}
dict_ten = {2:"twenty",3:"thirty",4:"forty",5:"fifty",
6:"sixty",7:"seventy",8:"eighty",9:"ninty"}


done = False
while not done:
    number = input("请输入要转换的数字:")
    try:
        number = int(number)
        if 0 >= number > 10000:
            print("请输入0-9999数字")
        else:
            done =True
    except (TypeError,ValueError):
        print("请输入正确数字")

print_list = list()
if number ==0:
    print("zero")
    quit()
if number >= 1000:
    print_list.append("%s thousand" % dict_one[(number//1000)%10])
if number >= 100:
    print_list.append("%s hundred" % dict_one[(number//100)%10])
if (number//10)%10 >= 2:
    print_list.append("%s" % dict_ten[(number//10)%10])
    print_list.append("%s" % dict_one[(number//1)%10])
elif(number/10)%10 > 1:
    print_list.append("%s" % dict_one[(number//10)%10*10 + ((number//1)%10)])
else:
    print_list.append("%s" % dict_one[((number//1)%10)])
print('-'.join(print_list))

