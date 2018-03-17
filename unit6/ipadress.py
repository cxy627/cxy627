#coding:utf-8
'''
'''
ipadress = ''
i = 1

while i <= 4:
    print("请输入第%s段IP字段:" % i, end='')
    iptext = input()
    if iptext.isdigit() and 0<int(iptext)<=255:
        iptext = iptext.rjust(3, "0")
        ipadress += (iptext+'.')
        i += 1
    else:
        print("输入有误,请重新输入第%s段IP地址" % i)

ipadress = ipadress[0:-1]
print("IP地址为%s" % ipadress)

for a in range(1,5):
    print("第%s段IP字段为%s" % (a,ipadress[((a-1)*4):((a-1)*4)+3]))
