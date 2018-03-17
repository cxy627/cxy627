#coding:utf-8
'''
'''
import random

while True:
    try:
        amount = int(input(
        "请输入需要生成的随机数列表的元素数量（不得大于100或小于1）："))
    except (ValueError, TypeError):
        print("请输入纯数字")
        continue
    if amount > 100 or amount < 1:
        print("请输入的数字在1至100之间")
        continue
    else:
        break

rand_list = [random.randint(0, 2**31-1) for i in range(0, amount)]
print("已生成随机数列表:%s" % rand_list)

while True:
    try:
        amount_sort = int(input(
            "请输入需要排序的随机数数量，数量不能超过%s个:" % amount))
    except (ValueError, TypeError):
        print("请输入纯数字")
        continue
    if amount > amount or amount < 1:
        print("请输入的数字在1至%s之间" % amount)
        continue
    else:
        break

sort_list = list()
for a in range(0,amount_sort):
    sort_list.append(random.choice(rand_list))

print(sorted(sort_list))
