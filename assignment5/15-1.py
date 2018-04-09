#coding:utf-8
def check(inword):
    import re
    if re.search(r"[bh][aiu]t",inword):
        return True
    return False

if __name__ == "__main__":
    print(check("hat"))
    print(check("haa"))
