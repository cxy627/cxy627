#coding:utf-8

'''
'''

print("enter a number:", end='')
num_str = input()
num_num = int(num_str)
fac_list = list(range(1, num_num+1))
print("Before:%s" % fac_list)
i = 0
while i < len(fac_list):
    # print(fac_list[i],end='')
    # print(num_num % fac_list[i])
    if num_num % fac_list[i] == 0:
        # del fac_list[i]
        del fac_list[i] 
        i -= 1
    i += 1
print("after:%s" % fac_list)                                  
