# coding:utf-8
'''
思路是建两个类，一个是股票市场stock_markrt，输入股票名返回股票编码以及当次输入时的随机价格。
一个是我的股票mystock，包含add_stock,del_stock,earn。
'''
import pickle
from random import uniform, randint
from time import strftime


class stock_market(object):
    def __init__(self, name):
        try:
            with open("stock_market", "rb") as fr:
                stock_save_id = pickle.load(fr)
            if name in stock_save_id:
                self.stock_id = stock_save_id[name]
            else:
                while True:
                    try_id = randint(10000000, 99999999)
                    if try_id in stock_save_id.values():
                        continue
                    self.stock_id = try_id
                    break
        except (FileNotFoundError, EOFError):
            stock_save_id = dict()
            while True:
                try_id = randint(10000000, 99999999)
                if try_id in stock_save_id.values():
                    continue
                self.stock_id = try_id
                break
        stock_save_id.update({name: self.stock_id})
        with open("stock_save_id", "wb") as fw:
            pickle.dump(self.stock_id, fw)
            self.stock_price = uniform(0, 100)


class mystock(object):
    def add_stock(self, name, amount):
        this_stock = stock_market(name)
        self.stock_price = this_stock.stock_price
        try:
            with open("mystock", "rb") as fr:
                mystock_list = pickle.load(fr)
                mystock_list.append(
                    [name, amount, this_stock.stock_price, strftime('%Y-%m-%d %H:%M:%S')])
        except (FileNotFoundError, EOFError):
            mystock_list = []
        with open("mystock", "wb") as fw:
            print(mystock_list)
            pickle.dump(mystock_list, fw)

    def del_stock(self):
        with open("mystock", "wb") as fw:
            pickle.dump([], fw)

    def earn(self):
        try:
            total_earn = 0
            with open("mystock", "rb") as fr:
                mystock_list = pickle.load(fr)
            for this_stock in mystock_list:
                this_stock_name = this_stock[0]
                this_stock_amount = this_stock[1]
                this_stock_price = this_stock[2]
                this_stock_earn = (stock_market(this_stock_name).stock_price
                                   - this_stock_price)*this_stock_amount
                print("{0}earn {1}".format(this_stock_name,this_stock_earn))
                total_earn += this_stock_earn
            print("totaly earn %s"% total_earn)
        except (FileNotFoundError, EOFError):
            pass


a = mystock()
a.del_stock()
a.add_stock("shenzhou1", 101)
a.add_stock("shenzhou2", 101)
a.add_stock("shenzhou3", 101)
a.add_stock("shenzhou4", 101)
a.earn()
#十次九亏....
