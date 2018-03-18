# coding:utf-8


class Point(object):
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        self.__echo()
    def __call__(self,x,y):
        self.x=x
        self.y=y
        self.__echo()
    def __echo(self):
        print("({0},{1})".format(self.x,self.y))


a=Point(0,0)
a(1,2)
