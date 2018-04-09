# coding:utf-8


class LogicDate(object):
    '''
    '''

    def __init__(self, n):
        self.name = n
        self.output = None

    def getlabel(self):
        print(self.name)

    def getoutput(self):
        self.output = self.prformGateLogic()
        return self.output


class BinaryGate(LogicDate):
    '''
    '''

    def __init__(self, n):
        super(BinaryGate, self).__init__(n)
        self.pina = None
        self.pinb = None

    def getpina(self):
        if self.pina == None:
            return (int(input("Enter Pin A input for gate %s-->" % self.name)))
        else:
            return self.pina.getfrom().getoutput()

    def getpinb(self):
        if self.pinb == None:
            return (int(input("Enter Pin B input for gate %s-->" % self.name)))
        else:
            return self.pinb.getfrom().getoutput()

    def setnextpin(self, source):
        if self.pina == None:
            self.pina = source
        elif self.pinb == None:
            self.pinb = source
        else:
            print("无可用插脚")


class UnaryGate(LogicDate):
    def __init__(self, n):
        super(UnaryGate, self).__init__(n)
        self.pin = None

    def getpin(self):
        if self.pin == None:
            return (int(input("Enter Pin input for gate %s-->" % self.name)))
        else:
            pass  # 待补充

    def setnextpin(self, source):
        if self.pin == None:
            self.pin = source
        else:
            print("无可用插脚")


class AndGate(BinaryGate):
    def __init__(self, n):
        super(AndGate, self).__init__(n)

    def prformGateLogic(self):
        a = self.getpina()
        b = self.getpinb()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):
    def __init__(self, n):
        super(OrGate, self).__init__(n)

    def prformGateLogic(self):
        a = self.getpina()
        b = self.getpinb()
        if a == 1 or b == 1:
            return 1
        else:
            return 0


class NotGate(UnaryGate):
    def __init__(self, n):
        super(NotGate, self).__init__(n)

    def prformGateLogic(self):
        a = self.getpin()
        if a == 0:
            return 1
        else:
            return 0


class Connector(object):
    def __init__(self, fagate, tgate):
        self.fromgate = fagate
        self.togate = tgate
        tgate.setnextpin(self)

    def getfrom(self):
        return self.fromgate

    def getto(self):
        return self.togate


a1 = AndGate("A1")
a2 = NotGate("A2")
b1 = OrGate("B2")
c1 = Connector(a1, b1)
c2 = Connector(a2, b1)
print(b1.getoutput())
