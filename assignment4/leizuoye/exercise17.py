#coding:utf-8

class MoneyFmt(object):
    def __init__(self,value=0.0):
        self.value=float(value)
    def update(self,value=None):
        if value != None:
            self.value=float(value)
    def __repr__(self):
        return "%s"% self.value
    def __str__(self):
        val ="$"+ str(self.value)
        return val
    def __bool__(self):
        return bool(self.value)

if __name__ =="__main__":
    cash =MoneyFmt(123.45)
    print(cash)
    cash.update(10000.4567)
    print(cash)
    print(bool(cash))
    cash.update(0)
    print(bool(cash))
    cash.update(-1.0)
    print(bool(cash))
