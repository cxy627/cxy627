#coding:utf-8
'''
'''

sort_list = [1,23,23,5,34,7456,43,12,458,67,97,765342,23,14,4324]
sort_len = len(sort_list)

for sort_counter in range(1,sort_len):
    key = sort_list[sort_counter]
    j = sort_counter - 1
    while j > -1 and key < sort_list[j]:
        sort_list[j+1] = sort_list[j]
        j -= 1
    sort_list[j+1] = key
print(sort_list)