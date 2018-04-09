#coding:utf-8

def check(inword):
    import re
    findword = re.findall(r"0?\d{15,16}|\d{4}-\d{6}-\d{5}|\d{4}-\d{4}-\d{4}-\d{4}",inword)
    if findword:
        print(findword)
    else:
        print("未找到")
    
if __name__=="__main__":
    check("4000-4000-8749-9282")
    check("3928-234237-92832")
    check("312-8283-29283-2238")
    check("1928738262922839")

#验证有效性什么意思。。。
