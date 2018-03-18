# coding:utf-8

"""
共搭建4个类，分别为Main,User,Cart,Item,
持久化存储3个字典user_pwd,user_cart,cart_item
序列化存储在B2C文件
"""
import shelve
import os


class User(object):
    def user_login(self):
        print("INuser_login")

    def user_create(self):
        print("IN user_create")

    def user_out(self):
        print("IN user_out")


class Cart(object):

    def view_cart(self):
        print("INview_cart")

    def add_cart(self):
        print("INadd_cart")

    def choice_cart(self):
        print("INchoice_cart")

    def del_cart(self):
        print("INdel_cart")


class Item(object):
    def view_item(self):
        print("INview_item")

    def add_item(self):
        print("INadd_item")

    def del_item(self):
        print("INdel_item")


class Main(object):  # 引用同一py文件下其它类的方法，是不是还有其它方法
    def __init__(self):
        '''尝试打开B2C读取3个字典，打开失败则重新建立3个字典'''
        (self.user_pwd, self.user_cart, self.cart_item) = (dict(), dict(), dict())
        try:
            B2C_save = shelve.open("B2C")
            self.user_pwd = B2C_save["user_pwd"]
            self.user_cart = B2C_save["user_cart"]
            self.cart_item = B2C_save["cart_item"]
            B2C_save.close()
        except (IOError, KeyError, ImportError):
            pass
        self.inuse_user = str()
        self.inuse_cart = str()
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
            else:
                break
        choice_result(self)
        if choice_result != Main.close_sys:
            # print(('\n'*80))#伪清屏，好像IDLE中没有真正清屏的方法
            self.menu()

    def check_input(self, hint, choice_dict):
        while True:
            user_input = input(hint)
            try:
                if int(user_input) in choice_dict:
                    return choice_dict[int(user_input)]
                else:
                    raise TypeError
            except (TypeError, ValueError):
                print("\n输入有误\n")

    def close_sys(self):
        """3个字典写回"""
        B2C_save = shelve.open("B2C", writeback=True)
        B2C_save["user_pwd"] = self.user_pwd
        B2C_save["user_cart"] = self.user_cart
        B2C_save["cart_item"] = self.cart_item
        B2C_save.close()


a1 = Main()
