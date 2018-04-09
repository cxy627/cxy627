#coding:utf-8

def check(inword):
    import re
    findword = re.search(r"\d+\s[A-Z].+ *",inword)
    if findword:
        print(findword.group())
    else:
        print("未找到")
    
if __name__=="__main__":
    check("2 r s")
    check("1180 Bordeaux Drive")
    check("3120 De la Cruz Boulevard")
