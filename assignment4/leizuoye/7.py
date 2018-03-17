# coding:utf-8

import time
class mytime(time):
    def __new__(cls, *args, **kwargs):
        return time.__new__(cls,23)


a1 = mytime()
print(a1.bit_length())
