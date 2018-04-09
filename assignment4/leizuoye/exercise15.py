# coding:utf-8
'''
write方法进行了覆盖，自定义的write方法中,self.file.write使用的是内置函数open
中的write方法,这个write方法所传入的参数为经过大写的line属性。因此最后写入的值
为大写的line
而其它的方法由于并未在capopen类中进行定义，因此会在__getattribute__然后
__getattr__，再找不到就会产生AttributeError，由于定义了__getattr__所以会
返回在内置函数open中找到的同名方法
'''


class capopen(object):
    def __init__(self, file, mode="r", buf=-1, encoding="utf-8", errors=None):
        self.file = open(file, mode, buf, errors)

    def __repr__(self):
        return(self.file)

    def __str__(self):
        return("self.file")

    def write(self, line):
        self.file.write(line.upper())

    def __getattr__(self, attr):
        return(getattr(self.file, attr))

# 下面这两个方法为何得自己进行定义,getattr并不能在open中找到这两个方法
# 而直接使用with open 反而可以
    def __enter__(self):
        return self.file

    def __exit__(self, type, value, trace):
        self.file.close()


if __name__ == "__main__":
    aw = capopen("exercise13", "w")
    input_text = "12345"
    aw.write(input_text+"\n")
    input_text = "45678"
    aw.write(input_text+"\n")
    input_text = "asddviwefni"
    aw.write(input_text+"\n")
    input_text = "JWsndiw124iwqiejoqw@#"
    aw.write(input_text+"\n")
    aw.close()
    with capopen("exercise13", "r") as ar:
        ar_str = ar.read()
        print(ar_str)
