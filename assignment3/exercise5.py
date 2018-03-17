# coding:utf-8
'''
共输出三个文件,分别对应过程式编程，函数，生成器
'''


# 过程式编程
fwlist1 = []
fw = open("ip_output1.txt", "w", encoding="utf-8")
for line1 in open("ip.txt", "r", encoding="utf-8"):
    fwlist1.append(line1[0:line1.find('"')].strip())
fwlist1 = list(set(fwlist1))
for newip1 in fwlist1[0:len(fwlist1)-1]:
    fw.write(newip1+"\n")
fw.write(fwlist1[len(fwlist1)-1])
fw.close


# 函数
def outip2(fw2r):
    fwlist2 = []
    line2 = fw2r.readline()
    while True:
        if not line2:
            break
        nowip = line2[0:line2.find('"')].strip()
        if nowip not in fwlist2:
            fwlist2.append(nowip)
        line2 = fw2r.readline()
    return(fwlist2)


if __name__ == "__main__":
    fw2r = open("ip.txt", "r", encoding="utf-8")
    fw2w = open("ip_output2.txt", "w", encoding="utf-8")
    fwlist2 = outip2(fw2r)
    for newip2 in fwlist2[0:len(fwlist2)-1]:
        fw2w.write(newip2+"\n")
    fw2r.close
    fw2w.write(fwlist2[len(fwlist2)-1])
    fw2w.close



# 生成器
def outip3(fw3r):
    line3 = fw3r.readline()
    while True:
        if not line3:
            return None
        yield line3[0:line3.find('"')].strip()
        line3 = fw3r.readline()


def main():
    fw3r = open("ip.txt", "r", encoding="utf-8")
    fw3w = open("ip_output3.txt", "w", encoding="utf-8")
    fwlist3 = []
    for newip3 in outip3(fw3r):
        if newip3 not in fwlist3:
            fwlist3.append(newip3)
    for newip3 in fwlist3[0:len(fwlist3)-1]:
        fw3w.write(newip3+"\n")
    fw3r.close
    fw3w.write(fwlist3[len(fwlist3)-1])
    fw3w.close


if __name__ == "__main__":
    main()
