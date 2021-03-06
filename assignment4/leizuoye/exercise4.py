# coding:utf-8
import time
lct = time.localtime
sft = time.strftime
from pickle import load as pload, dump as pdump


class User_Mange(object):
    def __init__(self, file_path="savefile"):
        try:
            with open(file_path, "rb") as read_file:
                self.user_text = pload(read_file)
        except (IOError, EOFError):
            self.user_text = dict()
        self.save_file = open("savefile", "wb")

    def add_user(self, name, password):
        if name not in self.user_text:
            assert isinstance(name, (int, str, float, tuple)), "用户名需为不可变对象"
            ntime = time.time()
            self.user_text.update({name:{password: ntime}})
        else:
            print("已创建的用户，本次操作无效")
    def __echo_user(self):
        for key in self.user_text:
            print("用户名:%s" % key)
            for count in self.user_text[key]:
                print("密码:{0} 创建密码时间:{1}".format(count,sft("%Y-%m-%d %H:%M:%S", time.localtime(self.user_text[key][count]))))

    def login(self,login_name):
        get_keydict = self.user_text.get(login_name)
        if get_keydict == None:
            print("无此用户")
            return None
        else:
            ctime =0
            for cpwd in get_keydict:
                if get_keydict[cpwd]>ctime:
                    time=get_keydict[cpwd]
                    get_key = cpwd
            login_pwd = self.creat_pw()
            if str(login_pwd) == str(get_key):
                self.user = str(login_name)
                print("登陆成功")
                return self.user
            else:
                print("密码错误")
                return None

    def creat_pw(self):
        import msvcrt
        print('请输入密码: ', end='', flush=True)
        li = []
        while 1:
            ch = msvcrt.getch()
            # 回车
            if ch == b'\r':
                msvcrt.putch(b'\n')
                # print('输入的密码是：%s' % b''.join(li).decode())
                return b''.join(li).decode()
            # 退格
            elif ch == b'\x08':
                if li:
                    li.pop()
                    msvcrt.putch(b'\b')
                    msvcrt.putch(b' ')
                    msvcrt.putch(b'\b')
            # Esc
            elif ch == b'\x1b':
                break
            else:
                li.append(ch)
                msvcrt.putch(b'*')

    def __del__(self):
        # with open("savefile", "wb") as sf:
            # pdump( self.user_text,sf)
        # 这里这么写会报错，会弹出NameError: name 'open' is not defined
        # 不知是不是与python的垃圾回收机制有关
        pdump(self.user_text, self.save_file)
        self.save_file.close()


if __name__ =="__main__":
    a1 = User_Mange()
    a1.add_user("python", "123456")
    a1._User_Mange__echo_user()
    a1.login("python")
