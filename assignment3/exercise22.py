# coding:utf-8
'''
'''
from os import listdir
import datetime
strftime=datetime.datetime.now().strftime



def wifechange(str):
    f = open("wifemount.txt", "a", encoding="utf-8")
    f.write(str+"\n")
    print(str)
    f.close


def hubbychange(str):
    f = open("hubbymount.txt", "a", encoding="utf-8")
    f.write(str+"\n")
    print(str)
    f.close


def balance(name):
    try:
        flist = open(name+"mount.txt", "r", encoding="utf-8").readlines()
    except IOError:
        return 100
    return int(flist[-1][flist[-1].find("余额:")+3:])


def transfer():
    while True:
        try:
            trantype = input('1.妻子向丈夫转账\n2.丈夫向妻子转账\n\n请输入数字:')
            trantype = int(trantype)
            if trantype == 1 or trantype == 2:
                break
            else:
                print("请输入正确选项")
                continue
        except (ValueError, TypeError):
            print("请输入数字")
            continue
        
    while True:
        try:
            trannum = input("请输入转账金额，退出请输入q:")
            if trannum == "q":
                print("退出")
                quit()
            trannum = int(trannum)
            if trannum <= 0:
                print("请输入大于零的数字")
                continue
        except (ValueError, TypeError):
            print("请输入纯数字")
            continue
        break
    if trantype == 1:
        wifebalance = balance("wife")
        hubbybalance = balance("hubby")
        wifebalance -= trannum
        hubbybalance += trannum
        print("丈夫账户更新如下:")
        hubbychange("%s 转入:%s,余额:%s" % (strftime("%Y-%m-%d %H:%M:%S"),trannum, hubbybalance))
        print("妻子账户更新如下:")
        wifechange("%s 转出:%s,余额:%s" % (strftime("%Y-%m-%d %H:%M:%S"),trannum, wifebalance))
    if trantype == 2:
        wifebalance = balance("wife")
        hubbybalance = balance("hubby")
        wifebalance += trannum
        hubbybalance -= trannum
        print("丈夫账户更新如下:")
        hubbychange("%s 转出:%s,余额:%s" % (strftime("%Y-%m-%d %H:%M:%S"),trannum, hubbybalance))
        print("妻子账户更新如下:")
        wifechange("%s 转入:%s,余额:%s" % (strftime("%Y-%m-%d %H:%M:%S"),trannum, wifebalance))
transfer()