#coding:utf-8
'''
'''
list_sort = [1,23,45,21,214,3,25,5,788,53]
list_length = len(list_sort)
for list_counter in range(0, list_length - 1):
    small = list_counter
    for item_counter in range(list_counter + 1, list_length):
        if list_sort[small] > list_sort[item_counter]:
            small = item_counter
    list_sort[list_counter],list_sort[small] = list_sort[small],list_sort[list_counter]
    # print("第%s轮排序完成,共比较%s次" % (list_counter + 1, list_length - list_counter - 1))

print(list_sort)