#coding:utf-8

import time
import getpass
db = {"admin":["1234",0,1]}
user_login = None


def newuser():
    prompt = "\n\n------注册用户------\n\n注册名:"
    while True:
        name = input(prompt)
        if name in db:
            prompt = "\n已被注册，请重新输入\n注册名："
            continue
        else:
            if len(name) > 16:
                prompt = "\n用户名不允许超过16位，请重新输入\n\n注册名："
                continue
            else:
                break
    pwd = getpass.getpass(prompt = "密码:")
    db[name] = [pwd, time.time(), 0]
    print("\n欢迎加入,用户%s" % name)
    user_login = name
    return(name)

def olduser():
    print("\n\n------用户登录------\n")
    name = input("用户名:")
    pwd = getpass.getpass(prompt = "密码:")
    try:
        pwd_ture = db.get(name)[0]
    except TypeError:
        pwd_ture = None
        print("无此用户,请重新输入")
        return(None)
    if pwd == pwd_ture:
        print("\n欢迎回来，用户%s" % name)
        user_login = name
        if time.time() - db[name][1] >= 60:
            print("上次登陆时间:%s" % time.strftime("%Y-%m-%d %X",time.localtime(db[name][1])))
        db[name][1] = time.time()
        return(user_login)
    else:
        print("账号或密码错误")
        return(None)

def admin_menu(user_login):
    if user_login is None:
        print("\n尚未登陆,请先登陆")
    else:
        if db.get(user_login)[2] == 1:
            print("\n成功进入管理界面\n")
            prompt = "\n------管理者菜单------\n\n1.管理员授权\n2.管理员注销\n3.查看所有用户账号密码\n4.\n5.返回\n\n请输入选择："
            done = False
            while not done:
                chosen = False
                while not chosen:
                    try:
                        choice = int(input(prompt).strip())
                    except (KeyboardInterrupt, EOFError):
                        choice = 5
                    except ValueError:
                        choice = None
                        prompt = "\n请输入正确数字"
                    if choice == 1:
                        admin_menu_add()
                    if choice == 2:
                        admin_menu_del()
                    if choice == 3:
                        admin_menu_view()
                    if choice == 4:
                        pass
                    if choice == 5:
                        done = True
                        chosen = True

        else:
            print("\n非管理员，禁止登陆")

def admin_menu_add():
    admin_add = input("\n请输入授权管理员权限用户:")
    try:
        db.get(admin_add)[2] = 1
    except TypeError:
        admin_add = None
        print('\n无此用户，请重新输入')
    else:
        print("\n授权管理员权限成功")
        
def admin_menu_del():
    admin_del = input("\n请输入注销管理员权限用户:")
    if admin_del == "admin":
        print("\n根管理员不允许注销权限")
    else:
        try:
            db.get(admin_del)[2] = 0
        except TypeError:
            admin_del = None
            print('无此用户，请重新输入')
        else:
            print("注销管理员权限成功")

def admin_menu_view():
    print("\n------账户列表------\n")
    db_counter = 0
    for key in db:
        db_counter += 1
        print("%s. 账号:%s 密码:%s" % (db_counter, key.ljust(16), db[key][0]))
    print("\n输出完毕,共%s个账户\n" % db_counter)

def showmenu():
    prompt="\n----菜单----\n\n1.注册\n2.登陆\n3.管理者菜单\n4.退出\n\n请输入数字:"
    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = int(input(prompt).strip())
            except (KeyboardInterrupt, EOFError):
                choice = 4
                break
            except ValueError:
                choice = None
                print("\n请输入纯数字")
                continue
            if choice not in range(1, 5):
                print('\n请输入正确选项')
                continue
            else:
                chosen = True    
        if choice == 1:
            user_login = str(newuser())
        if choice == 2:
            user_login_arm = str(olduser())
            if user_login_arm != None:
                user_login = user_login_arm
        if choice == 3:
            try:
                db.get(user_login)
            except (NameError,TypeError):
                print("\n尚未登陆,请先登陆")
            else:
                admin_menu(user_login)
        if choice == 4:
            done = True
 
if __name__ == '__main__':
    showmenu()







