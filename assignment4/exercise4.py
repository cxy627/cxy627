class Testclass(object):
    jishu = 100
    mylist = []

    def testjishu(self, number):
        """定义实例属性"""
        self.jishu = number

    def print_jishu(self):
        print("计数:%s" % self.jishu)


mytest = Testclass()
mytest.testjishu(20)
mytest.print_jishu()
