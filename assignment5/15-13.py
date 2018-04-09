#coding:utf-8

def check(inword):
    import re
    findword = re.search(r"class\s+(\'.+\')",str(inword.__class__))
    if findword:
        print(findword.group(1))
    else:
        print("未找到")
    
if __name__=="__main__":
    check("1.1.1.1")
    check(300)
    check(300.00)
