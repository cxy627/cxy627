#coding:utf-8
#不是很理解web网站地址和web域名的区别，写的是匹配IP地址的
def check(inword):
    import re
    findword = re.search(r"[12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d\.[12]?\d?\d",inword)
    if findword:
        print(findword.group())
    else:
        print("未找到")
    
if __name__=="__main__":
    check("1.1.1.1")
    check("300.300.300.300")
    check("192.168.1.2")
