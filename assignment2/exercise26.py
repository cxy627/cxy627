#coding:utf-8
import random

def newrand():
    rand_set=set()
    for i in range(0,random.randrange(10) + 1):
        rand_set.add(random.randint(0,9))
    return(rand_set)

set_a = newrand()
set_b = newrand()
answer1 = set_a | set_b
answer2 = set_a & set_b
if len(answer2) == 0:
    answer2 = "NULL"
print("集合A为%s,集合B为%s,A|B结果为%s,A&B结果为%s" % (set_a,set_b,answer1,answer2))