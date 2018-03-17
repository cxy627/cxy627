#coding:utf-8
'''
'''
def sort_num():
    while True:
        num_str = input("请输入多个数字,并以','进行分隔:")
        num_list = num_str.split(',')
        right = True
        for a in range(0,len(num_list)):
            if num_list[a].isdigit():
                num_list[a] = int(num_list[a])
            else:
                right = False
        if right:
            break
        else:
            print("输入有误,请重新输入")
    num_len = len(num_list)
    for num_counter in range(1,num_len):
        key = num_list[num_counter]
        j = num_counter - 1
        while j > -1 and key < num_list[j]:
            num_list[j+1] = num_list[j]
            j -= 1
        num_list[j+1] = key
    print("排序结果:%s" % num_list)

def sort_str():
    import string
    key_dict = string.ascii_letters + string.digits +string.punctuation +string.whitespace
    sort_str = input("请输入字符串:")
    sort = list()
    for i in sort_str:
        sort.append(i)
    length = len(sort)
    for list_counter in range(0, length - 1):
        flag = True
        int_sorter = 0
        while int_sorter <= length - 2:
            if int_sorter >= length - list_counter - 1:
                break
            if key_dict.find(sort[int_sorter]) > key_dict.find(sort[int_sorter + 1]):
                sort[int_sorter], sort[int_sorter + 1] = sort[int_sorter + 1], sort[int_sorter]
                flag = False
            int_sorter += 1
        if flag is True:
            break
    contect = ''
    print("排序结果:", end='')
    print(contect.join(sort))


if __name__ == "__main__":
    print("习题1：输入数字列并从小到大排序")
    sort_num()
    print("习题2:输入字符串并按a-z字典序排列")
    sort_str()
        