#coding:utf-8
'''
'''

sort = [1,24,3,4,5,6,8,10,2,3,24,21323,35,23,5435,2324,5436,87,768]
length = len(sort)
for list_counter in range(0, length - 1):
    flag = True
    int_sorter = 0
    while int_sorter <= length - 2:
        if int_sorter >= length - list_counter - 1:
            break
        if sort[int_sorter] > sort[int_sorter + 1]:
            sort[int_sorter], sort[int_sorter + 1] = sort[int_sorter + 1], sort[int_sorter]
            flag = False
        int_sorter += 1
    print("第%s轮完成,共排序 %s次" % (list_counter + 1, int_sorter))
    if flag is True:
        break
print(sort)
