# coding:utf-8
'''
习题11-4
'''


def changemin(min):
    try:
        min = int(min)
    except ValueError:
        print("请输入纯数字")
        return
    return (min//60, min % 60)


if __name__ == "__main__":
    inputmin = 125
    print("输入值为%s分,输出值为%s时%s分" % (inputmin, *changemin(inputmin)))
