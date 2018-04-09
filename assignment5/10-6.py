#coding:utf-8

def capopen(file=None,mode="r",encoding="utf-8"):
    f=None
    try:
        f=open(file,mode,encoding)
    except Exception:
        pass
    return f

print(capopen("123.txt","r"))
