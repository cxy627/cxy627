#coding:utf-8
'''


'''

import string
import keyword
alphas = string.ascii_letters + '_'
nums = string.digits

flag = 0

while flag == 0:
    print("请输入测试字符:",end="")
    myInput = input() 
    if myInput in keyword.kwlist:
        print("属于关键字")
        flag = 1
    else:
        if len(myInput) > 0:
            if myInput[0] not in alphas:
                print("首字母不合法")
                flag = 1
            else:
                for otherchar in myInput[1:]:
                    if otherchar not in alphas + nums:
                        print("除首字母后续应都为字母，数字，下划线")
                        flag = 1
                        break
                else:
                    print("通过")
                    flag = 1
