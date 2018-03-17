#coding:utf-8
'''
'''
def strip(string):
    start = 0
    end = len(string)
    for i in range(0,len(string)):
        if string[i] != ' ':
            start = i
            break
    for a in range(start,len(string),-1):
        if string[a] != ' ':
            end = a
            break

    return(string[start:end+1])

if __name__ == "__main__":
    print(strip(input("请输入需要去除空格的字符串:")))