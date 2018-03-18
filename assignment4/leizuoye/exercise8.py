#coding:utf-8
class Stack(list):
    def __new__(cls,*kwarg,**kwargs):
        return list.__new__(cls,*kwarg,**kwargs)
    
    def __init__(self):
        self.stack_list =[]
        if hasattr(list,"pop"):
            Stack.pop=Stack.original_pop
        else:
            Stack.pop = Stack.my_pop

    def inlist(self,*kwarg):
        def in_inlist(*kwarg):
            self
        return in_inlist
    def my_pop(self):
        last =self.stack_list[-1]
        self.stack_list=self.stack_list[0:-1]
        return last
    def original_pop(self):
        #这里有个疑问，写这段的目的是希望pop像其他实例方法一样使用，而不是需要对
        #实例中的属性使用。除了这样覆盖原有方法，还有没其它方式，我想到的只有写成模块（装饰器不知行不）。
        return self.stack_list.pop()
    def push(self,in_value):
        self.stack_list.reverse()
        self.stack_list.append(in_value)
        self.stack_list.reverse()
    
    def isempty(self):
        if self.stack_list == []:
            return True
        else:
            return False
    
    def __bool__(self):
        return self.isempty()

    def peek(self):
        return self.stack_list[-1]
    
    def __test(self):
        print(self.stack_list)

a1 = Stack()
a1._Stack__test()
print(bool(a1))
print(a1.isempty())
a1.push(12)
a1.push(1)
a1._Stack__test()
print(a1.pop())
a1._Stack__test()
a1.push(22)
a1.push(32)
a1._Stack__test()
print(a1.peek())
a1.pop = a1.my_pop
print(a1.pop())
a1._Stack__test()
