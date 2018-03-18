# coding:utf-8

from time import strftime, localtime


class mytime(object):
    def __init__(self, year=1900, month=1, day=1, hour=0, minute=0, sec=0, wday=0, yday=1, dst=0):
        self.update(year, month, day, hour, minute, sec, wday, yday, dst)

    def update(self, year=1900, month=1, day=1, hour=0, minute=0, sec=0, wday=0, yday=1, dst=0):
        get_time = (year, month, day, hour, minute, sec, wday, yday, dst)
        dafault_time = (1900, 1, 1, 0, 0, 0, 0, 1, 0)
        if get_time == dafault_time:
            self.get_time = localtime()
        else:
            self.get_time = get_time
        try:
            strftime("%b %d %Y %H:%M:%S", self.get_time)
        except ValueError:
            print("输入错误")

    def display(self, format_time="UNIX"):
        format_dict = {"MDY": "%m/%d/%y", "MDYY": "%m/%d/%Y", "DMY": "%d/%m/%y",
                       "DMYY": "%d/%m/%Y", "MODYY": "%b %d,%Y", "UNIX": "%d %b %d,%H:%M %Y"}
        assert str(format_time).upper() in format_dict,\
            "输入错误,请输入MDY/MDYY/DMY/DMYY/MODYY/UNIX"
        print(strftime(format_dict[format_time], self.get_time))


a1 = mytime()
a1.display()
print("*"*10)
a1.update(2018, 3, 17, 16, 36, 20, 5, 17, 0)
a1.display()
print("*"*10)
a1.display("MDY")
