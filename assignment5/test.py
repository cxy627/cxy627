

class Car(object):
    def __init__(self,count):
        print(count)#实例化，就会调用构造函数
for count in range(3):
    t= Car(count)
