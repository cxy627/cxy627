#coding:utf-8

def check(inword):
    import re
    findword = re.findall(r"\d+",inword)
    if findword:
        print(findword)
    else:
        print("未找到")
    
if __name__=="__main__":
    check("www.baidu.com")
    check("1180 Bordeaux Drive 2280")
    check("3120 De la Cruz Boulevard")
