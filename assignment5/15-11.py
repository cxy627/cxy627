#coding:utf-8

def check(inword):
    import re
    findword = re.findall(r"\w+@\w+\.com|\w+@\w+\.cn",inword)
    if findword:
        print(findword)
    else:
        print("未找到")
    
if __name__=="__main__":
    check("www.baidu.com")
    check("357663823@qq.com")
    check("357663823@qq.cn")
