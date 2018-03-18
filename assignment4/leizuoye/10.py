class FILO_LIFO(object):
    def __init__(self):
        self.FILI_list = []
    def shift(self):
        return self.FILI_list.pop(0)
    def unshift(self,in_value):
        self.FILI_list.reverse()
        self.FILI_list.append(in_value)
        self.FILI_list.reverse()
    def push(self,in_value):
        self.FILI_list.append(in_value)
    def pop(self):
        return self.FILI_list.pop()
    def __test(self):
        print(self.FILI_list)

a1=FILO_LIFO()
a1._FILO_LIFO__test()
a1.unshift(3)
a1.unshift(2)
a1._FILO_LIFO__test()
a1.push(4)
a1.unshift(1)
a1._FILO_LIFO__test()
print(a1.shift())
print(a1.pop())
a1._FILO_LIFO__test()
