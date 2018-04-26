# coding:utf-8

import socket
import time

HOST = "127.0.0.1"
PORT = 5555
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    try:
        tcpSerSock.connect(ADDR)
        break
    except Exception as e:
        print("链接失败,5秒后重新链接,原因:%s" % e)
        time.sleep(5)
        continue

print("用户%s已连接,如需退出聊天时输入exit" % str(ADDR))

while True:
    # 发送消息
    se_mes = input("我:")
    if se_mes == "exit":
        tcpSerSock.send(se_mes.encode())
        break
    tcpSerSock.send(se_mes.encode())

    # 接受消息
    re_mes = tcpSerSock.recv(BUFSIZ).decode()
    if not re_mes:
        break
    elif re_mes == "exit":
        break
    print("对方:%s" % re_mes)

print("已退出聊天")
