from operator import add, sub, mul, truediv
from random import randint, choice

choicedict = {"+": add, "-": sub, "*": mul, "/": truediv}


def easymath():
    chance = 3
    ichance = 1
    thischoice = choice("+-*/")
    twonum = [randint(1, 100) for i in range(0, 2)]
    twonum.sort(reverse=True)
    answer = choicedict[thischoice](twonum[0], twonum[1])
    if type(answer) == float:
        twonum[0] = randint(0, 50)*twonum[1]
        answer = choicedict[thischoice](twonum[0], twonum[1])
    print("%d%s%d=" % (twonum[0], thischoice, twonum[1]), end='')
    while True:
        while True:
            usermath = input()
            try:
                usermath = int(usermath)
            except (TypeError, ValueError):
                print("重新输入")
                continue
            break
        if usermath == answer:
            print("正确")
            break
        elif chance == ichance:
            print("失败")
            break
        else:
            print("第%s次回答错误,再试一次" % ichance)
            ichance += 1


if __name__ == "__main__":
    easymath()
