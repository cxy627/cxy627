#coding:utf-8

#函数
def Foo1():
    pass

class Foo(object):
    #函数
    @staticmethod
    def Foo():
        pass  
    
    #方法
    def Bar(self):
        pass  

    @classmethod
    def Bar1(cls):
        pass

#这里的Foo1,Foo是函数，Bar是方法，其实函数与方法的区别就在于它与
#类或者实例有无绑定的关系,Foo1不在类里头，所以自然是普通方法，Foo
#为静态方法，与FOO类无绑定关系，Bar有传递实例属性进入，所以属于方法
#Bar1是类方法，传入了类属性