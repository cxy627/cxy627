#coding:utf-8

class Queue(object):
    def __init__(self):
        self.Queue_list=[]

    def enqueue(self,in_value):
        self.Queue_list.append(in_value)

    def dequeue(self):
        return self.Queue_list.pop(0)
    def __test(self):
        print(self.Queue_list)

a1=Queue()
a1._Queue__test()
a1.enqueue(1)
a1.enqueue(2)
a1.enqueue(3)
a1._Queue__test()
print(a1.dequeue())
a1._Queue__test()
