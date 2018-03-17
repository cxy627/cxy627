# coding:utf-8


class Foo(object):
    a1 = [1]
    '''
    123
    '''

    def __init__(self, x, y):
        self.x = x
        self.y = y
        Foo.a1.append(2)

    def print_xy(self):
        print("{0}123{1}".format(self.x, self.y))


a = Foo(1, 2)
a.a1.append(3)
a.print_xy()
print(Foo.__dir__(Foo))
print(dir(Foo))
print(Foo.__name__)
print(Foo.__module__)
print(a.__class__)
print(Foo.a1)
print(a.a1)
