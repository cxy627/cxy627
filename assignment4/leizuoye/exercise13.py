# coding:utf-8
# 愣是没看懂里面的ren,more。百度不到这两方法

from copy import copy


class DOS(object):
    def __init__(self, input_order):
        self.input_order = input_order
        self.test="abv"

    def runit(self):
        trandict = {"ls": "dir", "cat": "type", "cp": "copy", "rm": "del"}
        for i in trandict:
            tran_place = self.input_order.find(i)
            if tran_place >= 0:
                output_order = self.input_order[0:tran_place] + \
                    trandict[i]+"("+self.input_order[tran_place+len(i)+1:]+")"
                # print(repr(output_order))
                # del(self.test)
                return(eval(output_order))
                


a = DOS("ls __builtins__")
print(a.runit())
b= DOS("rm self.test")
#b.runit()#这条怎么都执行不了,SyntaxError,直接写进去试了没错
c = DOS("cp self.test")
print(c.runit())
d = DOS("cat self.test")
print(d.runit())
