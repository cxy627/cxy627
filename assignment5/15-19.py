def pick():
    import re
    f = open("redata.txt", "r", encoding="utf-8")
    row = 0
    while True:
        row += 1
        thisline = f.readline()
        if thisline:
            ss = re.search(
                "\w{3}\s\w{3}\s+\d+\s\d{2}:\d{2}:\d{2}\s\d{4}::[a-z]+@[a-z]+\.[a-z]{3}::(\d+)-\d+-\d+", thisline)
            if ss:
                print("第%s行:%s" % (row, ss.group(1)))
            else:
                print("匹配出错")
        else:
            f.close()
            break
if __name__=="__main__":
    pick()
