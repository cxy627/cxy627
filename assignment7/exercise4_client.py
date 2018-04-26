#coding:utf-8
from socket import *

BUFSIZ = 1024

tcpcocket = socket(AF_INET,SOCK_STREAM)
while True:
    HOST=input("主机地址:")
    PORT=input("端口号:")
    try:
        tcpcocket.connect((HOST,int(PORT)))
        break
    except Exception as e:
        print("输入错误，信息如下:",e)
    else:
        print("完成链接")
while True:
    data = input("> ")
    if not data:
        break
    tcpcocket.send(data.encode())
    data = tcpcocket.recv(BUFSIZ)
    if not data:
        break
    print(data.decode("utf-8"))
tcpcocket.close()
