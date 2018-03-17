# coding:utf-8
'''
'''
import sys

fw = open("test_output.txt", "w", encoding="utf-8")


def infile():
    for line in open("test.txt", "r", encoding="utf-8"):
        if line.find("***编号**") != -1:
            fw.write(line)
        if line.find("公司行业：") != -1:
            placexz = line.find("公司性质：")
            placegm = line.find("公司规模：")
            hy = line[0:placexz].strip()
            xz = line[placexz:placegm].strip()
            gm = line[placegm:].strip()
            fw.write(hy+"\n"+xz+"\n"+gm+"\n\n")


fw.close
infile()
