# coding:utf-8

import socket

HOST = "127.0.0.1"
PORT = 5555
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(1)
print("等待链接...")

conn, addr = tcpSerSock.accept()
print("用户%s已连接,如需退出聊天时输入exit" % str(addr))

while True:
    # 接受消息
    re_mes = conn.recv(BUFSIZ).decode()
    if not re_mes:
        break
    elif re_mes == "exit":
        break
    print("对方:%s" % re_mes)
    # 发送消息
    se_mes = input("我:")
    if se_mes == "exit":
        conn.send(se_mes.encode())
        break
    conn.send(se_mes.encode())
print("已退出聊天")
