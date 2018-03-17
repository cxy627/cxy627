# coding:utf-8
'''
习题11-11
'''


def map1(fwr):
    linelist = []
    for line in fwr:
        linelist.append(line.strip())
    return linelist


def menu():
    while True:
        choice = input("请选择：1.覆盖原文件2.另存为文件")
        try:
            choice = int(choice)
        except (TypeError, ValueError):
            print("请输入数字1或2")
            continue
        if choice == 1:
            fwwname = "kongge.txt"
            break
        elif choice == 2:
            fwwname = input("请输入文件名")+".txt"
            break
        else:
            print("请输入数字1或2")
            continue
    return fwwname


def main():
    linelist = map1(open("kongge.txt", "r", encoding="utf-8"))
    fww = open(menu(), "w", encoding="utf-8")
    fww.write("\n".join(linelist))
    print("完成")


if __name__ == "__main__":
    main()
