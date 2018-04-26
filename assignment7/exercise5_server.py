#coding:utf-8
#书上的示例地址404，找的是https://docs.python.org/3/library/socket.html?highlight=tcp#example
#18.1.5的示例1

# Echo server program
import socket
from time import ctime
import os
import os
 
mes_dict = {"date":ctime,"os":os.name,"ls":os.listdir,"dir":os.curdir}
HOST = '127.0.0.1'                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            if not data: 
                break
            else:
                mes = data.decode("utf-8")
                print("Received:",mes)
                if mes in mes_dict:
                    mes = mes_dict[mes]
                    if hasattr(mes,"__call__"):
                        mes = mes()
            print("Send:",str(mes))
            conn.sendall(str(mes).encode())
