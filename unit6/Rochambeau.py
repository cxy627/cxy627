#coding:utf-8
'''
'''

def mathkey():
    (shitou,jiandao,bu,flag) = (-100,-100,-100,0)

    while shitou <= 500 and flag == 0:
        while jiandao <= 500 and flag == 0:
            while bu <= 500 and flag == 0:
                if shitou == 0:
                    shitou += 1
                elif jiandao == 0:
                    jiandao += 1
                elif bu == 0:
                    bu += 1
                if (
                ((abs(shitou%jiandao) == abs(jiandao%bu)) and 
                (abs(shitou%jiandao)== abs(bu%shitou)) and 
                (abs(jiandao%bu) == abs(bu%shitou)) 
                )and
                (
                (abs(jiandao%shitou) == abs(bu%jiandao)) and
                (abs(jiandao%shitou) == abs(shitou%bu)) and 
                (abs(bu%jiandao) == abs(shitou%bu))
                )and
                jiandao != bu and
                bu != shitou and
                jiandao != shitou):
                    return("石头为%s,剪刀为%s,布为%s" % (shitou,jiandao,bu))
                    flag = 1
                bu += 1
            jiandao += 1
            bu = -100
        shitou += 1
        jiandao = -100
        bu = -100   
        print(shitou)      
    if flag == 0:
        return("查无")

def caiquan(user_choice):
    '''
    0石头，1剪刀，2布
    '''

    import random
    print('\n-----比赛开始-----\n')
    compture_choice = random.randint(0,2)
    windict = {0:1,1:2,2:0}
    faildict = {1:0,2:1,0:2}
    translatedict ={0:"石头",1:"剪刀",2:"布"}
    comple_choice = (user_choice,compture_choice)
    if comple_choice in windict.items():
        return("你出:%s\n电脑出:%s\n结果:胜!" % (translatedict[user_choice],translatedict[compture_choice]))
    elif comple_choice in faildict.items():
        return("你出:%s\n电脑出:%s\n结果:负!" % (translatedict[user_choice],translatedict[compture_choice]))
    else:
        return("你出:%s\n电脑出:%s\n结果:平!" % (translatedict[user_choice],translatedict[compture_choice]))

while True:
    print("请输入你的选择:",end = '')
    inchoice = input()
    translatedict ={"石头":0,"剪刀":1,"布":2}
    a = translatedict.keys
    if inchoice in translatedict:
        break
    else:
        print("请重新输入石头/剪刀/布")
choice = translatedict[inchoice]
print(caiquan(choice))

