# coding:utf-8

"""
共搭建4个类，分别为Main,User,Cart,Item,
持久化存储3个字典user_pwd,user_cart,cart_item
序列化存储在B2C文件
"""
import shelve
import os
import exercise4
import msvcrt


class User(object):
    def user_login(self, name=False):
        if Main.inuse_user!="未登录":
            return("请先退出登陆")
        if name:
            login_user = name
        else:
            login_user = input("请输入用户名:").strip()
        if login_user in Main.user_pwd:
            login_pwd = exercise4.User_Mange.creat_pw(self).strip()
            if login_pwd == Main.user_pwd[login_user]:
                Main.inuse_user = login_user
                return("登陆成功")
            else:
                return("密码错误，请重新登陆")
        else:
            return("账号错误，请重新登陆")

    def user_create(self):
        set_user = input("请输入用户名:").strip()
        if set_user in Main.user_pwd:
            print("已注册,请登陆")
            self.user_login(set_user)
        set_pwd = exercise4.User_Mange.creat_pw(self).strip()
        Main.user_pwd.update({set_user: set_pwd})
        Main.inuse_user = set_user
        return(None)

    def user_out(self):
        confirm = input("输入Y以确定退出")
        if confirm == "y"or confirm == "Y":
            print_name = Main.inuse_user
            Main.inuse_user = str()
            return("%s,您已退出" % print_name)


class Cart(object):

    def view_cart(self):
        if Main.inuse_user in Main.user_cart:
            amount_usercart = len(Main.user_cart[Main.inuse_user])
            print("总共有%s个购物车，以下为购物车名称及拥有商品:" % amount_usercart)
            for i in range(amount_usercart):
                print("\n{0}.{1}:".format(
                    i+1, Main.user_cart[Main.inuse_user][i]))
                Item.view_item(self)
            print("\n按任意键以继续")
            msvcrt.getch()
        else:
            print("暂无购物车，去新建一个吧!")
            return(Cart.add_cart(self))

    def add_cart(self):
        new_cart = input("请输入新购物车名:")
        if Main.inuse_user in Main.user_cart:
            if new_cart in Main.user_cart[Main.inuse_user]:
                Main.inuse_cart = new_cart
                return("已有该购物车,已切换至该购物车")
            else:
                Main.user_cart[Main.inuse_user].append(new_cart)
                Main.inuse_cart = new_cart
                return("成功添加并进入该购物车")
        else:
            Main.user_cart.update({Main.inuse_user: [new_cart]})
            Main.inuse_cart = new_cart
            return("成功添加并进入该购物车")

    def choice_cart(self):
        try:
            amount_usercart = len(Main.user_cart[Main.inuse_user])
        except KeyError:
            print("暂无购物车，去新建一个吧!")
            return(Cart.add_cart(self))
        if amount_usercart == 1:
            Main.inuse_cart = Main.user_cart[Main.inuse_user][0]
            return("仅有一个购物车，已进入购物车:%s" % Main.user_cart[Main.inuse_user][0])
        else:
            while True:
                for i in range(amount_usercart):
                    print("{0}.{1}".format(
                        i+1, Main.user_cart[Main.inuse_user][i]))
                choice_cart = input("请输入购物车序号:").strip()
                try:
                    choice_cart = int(choice_cart)
                except (ValueError, TypeError):
                    print("输入有误,请输入数字")
                    continue
                if choice_cart-1 in range(amount_usercart):
                    Main.inuse_cart = Main.user_cart[Main.inuse_user][choice_cart-1]
                    return("已进入购物车:%s" % Main.inuse_cart)
                else:
                    print("请输入正确序号")

    def del_cart(self):
        confirm = input("输入Y以确定删除")
        if confirm == "y"or confirm == "Y":
            print_name = Main.inuse_cart
            Main.user_cart[Main.inuse_user].remove(print_name)
            Main.inuse_cart = "未选择"
            return("您已删除购物车%s" % print_name)


class Item(object):
    def view_item(self):
        print("INview_item")

    def add_item(self):
        cartid = Main.inuse_user+"-"+Main.inuse_cart
        new_item = input("请输入新商品名:")
        if Main.inuse_user in Main.cart_item:
            if new_cart in Main.cart_item[Main.inuse_cart]:
                Main.inuse_cart = new_cart
                return("已有该购物车,已切换至该购物车")
            else:
                Main.cart_item[Main.inuse_user].append(new_cart)
                Main.inuse_cart = new_cart
                return("成功添加并进入该购物车")
        else:
            Main.cart_item.update({Main.inuse_user: [new_cart]})
            Main.inuse_cart = new_cart
            return("成功添加并进入该购物车")

    def del_item(self):
        print("INdel_item")


class Main(object):  # 引用同一py文件下其它类的方法，是不是还有其它方法
    (user_pwd, user_cart, cart_item) = (dict(), dict(), dict())
    inuse_user = "未登录"
    inuse_cart = "未选择"

    def __init__(self):
        '''尝试打开B2C读取3个字典'''
        try:
            B2C_save = shelve.open("B2C")
            Main.user_pwd = B2C_save["user_pwd"]
            Main.user_cart = B2C_save["user_cart"]
            Main.cart_item = B2C_save["cart_item"]
            B2C_save.close()
        except (IOError, KeyError, ImportError):
            pass
        self.menu()

    def __del__(self):
        # 原本函数close_sys的代码是写这的，但弹出报错
        # ImportError: sys.meta_path is None, Python is likely shutting down
        # 意思是指解构器中不能执行外部文件的调用？
        pass

    def menu(self):
        print("当前用户:{0}     当前购物车:{1}".format(
            self.inuse_user, self.inuse_cart))
        menu = '''
**********操作菜单**********

0.登陆用户
1.注册用户
2.登出用户
3.查看名下购物车
4.新建购物车
5.选择购物车
6.删除购物车
7.查看商品
8.添加商品
9.删除商品
88.退出系统

        '''
        print(menu)
        choice_dict = dict(zip((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 88),
                               (User.user_login, User.user_create, User.user_out, Cart.view_cart, Cart.add_cart, Cart.choice_cart, Cart.del_cart, Item.view_item, Item.add_item, Item.del_item, Main.close_sys)))
        hint = "请输入数字0-9/88:"
        while True:
            choice_result = self.check_input(hint, choice_dict)
            if choice_result == None:
                print("还未开放请重选")
            elif choice_result == "no logining user":
                print("请先登陆再进行该操作")
            elif choice_result == "no logining cart":
                print("请先选择购物车在进行该操作")
            else:
                break
        run_hint = choice_result(self)
        if choice_result != Main.close_sys:
            print(('\n'*80))  # 伪清屏，好像IDLE中没有真正清屏的方法
            if not run_hint is None:
                print(run_hint)
            self.menu()

    def check_input(self, hint, choice_dict):
        while True:
            user_input = input(hint)
            try:
                if int(user_input) in choice_dict:
                    if int(user_input) in (2, 3, 4, 5, 6, 7, 8, 9) and Main.inuse_user == "未登录":
                        return("no logining user")
                    elif int(user_input) in (6, 7, 8, 9) and Main.inuse_cart == "未选择":
                        return("no logining cart")
                    else:
                        return choice_dict[int(user_input)]
                else:
                    raise TypeError
            except (TypeError, ValueError):
                print("\n输入有误\n")

    def close_sys(self):
        """3个字典写回"""
        B2C_save = shelve.open("B2C", writeback=True)
        B2C_save["user_pwd"] = Main.user_pwd
        B2C_save["user_cart"] = Main.user_cart
        B2C_save["cart_item"] = Main.cart_item
        B2C_save.close()


a1 = Main()
print(Main.user_pwd)
print(Main.user_cart)
