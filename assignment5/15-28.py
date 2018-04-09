#coding:utf-8

def check(inword):
    import re
    findword = re.match(r"(\d{3}-)?\d{3}-\d{4}",inword)
    if findword:
        print(findword.group())
    else:
        print("未找到")
    
if __name__=="__main__":
    check("400-500-2456")
    check("555-8491")
    check("5419-546-4484")
