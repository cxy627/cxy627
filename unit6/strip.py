#coding:utf-8
'''
'''

print("输入字符串:",end='')
text = input()
start_num = 0
end_num = len(text)

for i in range(0,len(text)):
    if text[i] != ' ':
        start_num = i
        break


for a in range(len(text),0,-1):
    # print(a)
    if text[a-1]  != ' ':
        end_num = a
        break
print("处理后的字符串是%s。" % text[start_num:end_num])
