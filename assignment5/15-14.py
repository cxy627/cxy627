#coding:utf-8

def check(inword):
    import re
    findword = re.findall(r"1[012]",inword)
    if findword:
        print(findword)
    else:
        print("未找到")
    
if __name__=="__main__":
    check("11")
    check("10")
    check("357663823@qq.cn")
