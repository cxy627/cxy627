def pick():
    import re
    f = open("redata.txt", "r", encoding="utf-8")
    row = 0
    while True:
        row += 1
        thisline = f.readline()
        if thisline:
            ss = re.sub("[a-z]+@[a-z]+\.[a-z]{3}","357663823@qq.com",thisline)
            if ss:
                print(ss)
            else:
                print("替换出错")
        else:
            f.close()
            break
if __name__=="__main__":
    pick()
