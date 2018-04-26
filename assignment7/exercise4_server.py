#coding:utf-8
from socket import *
from time import ctime

BUFSIZ = 1024

tcpcocket = socket(AF_INET,SOCK_STREAM)
while True:
    HOST=input("主机地址:")
    PORT=input("端口号:")
    try:
        tcpcocket.bind((HOST,int(PORT)))
        break
    except Exception as e:
        print("输入错误，信息如下:",e)
    else:
        print("完成创建")
tcpcocket.listen(5)
while True:
    print("waiting for connection")
    tcpCliSock,addr = tcpcocket.accept()
    print("...connected from:",addr)
    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send(("[%s]%s" % (ctime(),data.decode())).encode())
    tcpCliSock.close()
tcpCliSock.close()
