# coding:utf-8
import math


class line(object):
    def __init__(self, start_x, start_y, end_x, end_y):
        self.get_value = []
        give_value = (start_x, start_y, end_x, end_y)
        for count in range(4):
            assert isinstance(give_value[count], (float, int)), "请输入数字"
            self.get_value.append(give_value[count])
        #有无更简便的写法
        self.start_x=self.get_value[0]
        self.start_y=self.get_value[1]
        self.end_x=self.get_value[2]
        self.end_y=self.get_value[3]
        
        print(self.get_value)

    def __repr__(self):
        return "(({0},{1}),({2},{3}))".format(*self.get_value)

        
    def length(self):
        line_len = ((self.end_x-self.start_x)**2 +(self.end_y-self.start_y)**2)**0.5
        return line_len
    def slope(self):
        x_distance = self.end_x-self.start_x
        y_distance =self.end_y-self.start_y
        if x_distance == 0:
            return None
        else:
            return y_distance/x_distance


a=line(1,2,3,4)
print(a.length())
print(a.slope())
print(a)
