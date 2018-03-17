# coding:utf-8
'''
'''

from random import randint


def rolldice():
    sumdice = 0
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    sumdice = dice1 + dice2
    print("本次掷骰子的结果为:骰子1点数为%s,骰子2点数为%s,和为%s" % (dice1, dice2, sumdice))
    return sumdice


def game(sumdice, last=0):
    def peace():
        print("不胜不败，重新骰殿子\n")
        return game(rolldice(), last=sumdice)

    if last != 0:
        if sumdice == last:
            print("玩家胜")
            result = True
            return result
        elif sumdice == 7:
            print("玩家败")
            result = False
            return result
        else:
            return(peace())
    else:
        if sumdice == 7 or sumdice == 11:
            print("玩家胜")
            result = True
            return result
        elif sumdice == 2 or sumdice == 3 or sumdice == 12:
            print("玩家败")
            result = False
            return result
        else:
            return(peace())


def main():
    game(rolldice())


if __name__ == "__main__":
    main()
