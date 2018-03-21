# coding:utf-8
'''
'''


class Time60(object):

    def __init__(self, *kwarg):
        input_tran = {dict: self.indict, int: self.inint,
                      tuple: self.intuple, str: self.instr}
        if len(kwarg) == 0:
            self.hr = 0
            self.min = 0
        elif type(kwarg[0]) in input_tran:
            input_tran[type(kwarg[0])](kwarg)
            self.recount()


    def indict(self, kwarg):
        self.hr = kwarg[0]["hr"]
        self.min = kwarg[0]["min"]

    def inint(self, kwarg):
        self.hr = kwarg[0]
        self.min = kwarg[1]

    def intuple(self, kwarg):
        self.hr = kwarg[0][0]
        self.min = kwarg[0][1]

    def instr(self, kwarg):
        in_hrmin = kwarg[0].split(":")
        self.hr = int(in_hrmin[0])
        self.min = int(in_hrmin[1])

    def __str__(self):
        return "%s:%s" % (str(self.hr).rjust(2, "0"), str(self.min).rjust(2, "0"))

    def __repr__(self):  # 这个要求没搞很懂，不知写错没
        return("Time60({0}:{1})".format(str(self.hr).rjust(2, "0"), str(self.min).rjust(2, "0")))

    def __iadd__(self, other):
        self.hr += other.hr
        self.min += other.min
        self.recount()
        return self

    def __add__(self, other):
        self.hr += other.hr
        self.min += other.min
        self.recount()
        return self.__class__(self.hr, self.min)

    def __radd__(self, other):  # 其实感觉实现这个没什么必要，这里实现了跟整型的右加
        self.hr += int(other.__repr__())
        self.recount()
        return(self.__class__(self.hr, self.min))

    def recount(self):
        while self.min>=60:
            self.min -=60
            self.hr+=1
        while self.hr>=24:
            self.hr-=24

if __name__=="__main__":
    a1 = Time60(13, 50)
    print(a1)
    print(repr(a1))
    print("****")
    a2 = Time60((16, 80))
    print(a2)
    print(repr(a2))
    print("****")
    a3 = Time60({"hr": 15, "min": 90})
    print(a3)
    print(repr(a3))
    print("****")
    a4 = Time60("18:05")
    print(a4)
    print(repr(a4))
    print("****")
    a5 = Time60("18:55")
    print(a5)
    print(repr(a5))
    print("****")
    a6 = Time60()
    print(a6)
    print(repr(a6))
    print("****")
    a7 = 20+a6
    print(a7)
    print("****")
    a1 += a1
    print(a1)
