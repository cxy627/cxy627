import sys


class MoneyFmt(object):
    def __init__(self, money, other_echo=False):
        assert isinstance(money, float), "需要输入浮点型"
        self.money = money
        self.other_echo = other_echo
        self.change()

    def change(self):
        if self.money < 0 and self.other_echo == True:
            self.print_money = "<{0}>".format(abs(self.money))
        else:
            self.print_money = str(self.money)

    def __repr__(self):
        return self.money

    def __str__(self):
        return self.dollarize()

    def __bool__(self):
        if self.money >= 1:
            return True
        else:
            return False

    def dollarize(self):
        return(self.print_money)

    def update(self, upmoney):
        self.money = upmoney
        self.change()


foo1 = MoneyFmt(-1.50, other_echo=True)
print(foo1)
print(bool(foo1))

print("-"*10)

foo2 = MoneyFmt(-1.50, other_echo=False)
print(foo2)
print(bool(foo2))

print("-"*10)

foo3 = MoneyFmt(1.50)  
print(foo3)
print(bool(foo3))
