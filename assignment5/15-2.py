#coding:utf-8

def check(inword):
    import re
    findword = re.search(r"\w+\s+\w+",inword)
    if findword:
        print(findword.group())
    else:
        print("未找到")
    
if __name__=="__main__":
    check("2 r s")
    check("o t")
    check("ot")
