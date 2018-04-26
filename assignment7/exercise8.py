# coding:utf-8
'''
该模块可选服务端和客户端,Main为子线程,sender1,receiver1为孙线程且为守护线程。
如果要结束将事件stopchat设为True,break子线程从而关闭孙线程
(上网没查到更好的方法，threading好像没有立刻终止其它进程的方法,
sender会一直阻塞在input()那)
'''

import time
import socket
import threading

HOST = "127.0.0.1"
PORT = 5555
BUFSIZ = 1024
ADDR = (HOST, PORT)


class Main(threading.Thread):
    def __init__(self, event, conn, sender, receiver, name="main"):
        self.stopchat = event
        self.sender1 = sender
        self.receiver1 = receiver
        super(Main, self).__init__(name=name)

    def run(self):
        self.sender1.setDaemon(True)
        self.receiver1.setDaemon(True)
        self.sender1.start()
        self.receiver1.start()
        while True:
            if self.stopchat.is_set():
                break


class Switch(object):
    def __init__(self):
        self.tcpSerSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.be_Server = int(input("0为客户端,1为服务端:"))
        assert self.be_Server == 0 or self.be_Server == 1, "请输入0/1"

    def init_socket(self):
        if bool(self.be_Server):
            self.tcpSerSock.bind(ADDR)
            self.tcpSerSock.listen(1)
            print("等待链接。。。")
            self.conn, self.addr = self.tcpSerSock.accept()
            print("用户%s已链接，如需退出群聊请输入exit:" % str(self.addr))
            return self.conn
        else:
            while True:
                try:
                    self.tcpSerSock.connect(ADDR)
                    break
                except KeyboardInterrupt:
                    exit()
                except Exception as e:
                    print("5秒后重连，因以下原因失败%s" % e)
                    time.sleep(5)
                    continue
            self.conn = self.tcpSerSock
            print("用户%s已链接，如需退出群聊请输入exit:" % str(ADDR))
        return self.conn


class Sender(Main):
    def __init__(self, event, conn):
        self.conn = conn
        self.stopchat = event
        threading.Thread.__init__(self, name="Sender")
        # super(Sender,self).__init__(name="Sender")

    def run(self):
        while True:
            se_mes = input()
            if not se_mes:
                print("请输入信息")
                continue
            self.conn.send(se_mes.encode())
            if se_mes == "exit":
                self.stopchat.set()


class Receiver(Main):
    def __init__(self, event, conn):
        self.conn = conn
        self.stopchat = event
        threading.Thread.__init__(self, name="Receiver")
        # super(Receiver,self).__init__(name="Receiver")

    def run(self):
        while True:
            re_mes = self.conn.recv(BUFSIZ)
            print("对方:%s" % re_mes.decode())
            if (re_mes.decode() == "exit") or (not re_mes):
                self.stopchat.set()


if __name__ == "__main__":
    s1 = Switch()
    conn = s1.init_socket()
    stopchat = threading.Event()
    sender1 = Sender(stopchat, conn)
    receiver1 = Receiver(stopchat, conn)
    M1 = Main(stopchat, conn, sender1, receiver1)
    M1.start()
    M1.join()
    print("已退出聊天")
