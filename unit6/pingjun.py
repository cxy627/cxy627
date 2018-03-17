#coding:utf-8
'''
'''
import string
score = list()
sum = 0
while True:
    print("请输入成绩，如退出输入请输入down:")
    text = input()
    if text == 'down':
        break
    if (text == '') or (not text.isdigit()):
        print("请正确输入,本次输入无效")
        text = ''
        continue
    score.append(int(text))
    text = ''

for i in range(0,len(score)):
    print("%s号学生成绩为%s" % (i+1,score[i]))
    sum += score[i]

print("平均分为%d" % (sum/(i+1)))

