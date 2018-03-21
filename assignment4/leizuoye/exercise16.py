# coding:utf-8
import exercise14


class capcapopen(exercise14.capopen):
    def __init__(self, file, mode="r", buf=-1, encoding="utf-8", errors=None):
        self.file = open(file, mode, buf, errors)

    def writelines(self, line_feed=False, *lines):
        for i in lines:
            if line_feed:
                self.file.write(i+"\n")
            else:
                self.file.write(i)


if __name__ == "__main__":
    aw = capcapopen("exercise13", "w")
    input_text1 = "12345"
    input_text2 = "45678"
    input_text3 = "asddviwefni"
    input_text4 = "JWsndiw124iwqiejoqw@#"
    aw.writelines(False, input_text1, input_text2, input_text3, input_text4)
    aw.close()
    with capcapopen("exercise13", "r") as ar:
        ar_str = ar.read()
        print(ar_str)
        
    print("*"*20)

    aw = capcapopen("exercise13", "w")
    input_text1 = "12345"
    input_text2 = "45678"
    input_text3 = "asddviwefni"
    input_text4 = "JWsndiw124iwqiejoqw@#"
    aw.writelines(True, input_text1, input_text2, input_text3, input_text4)
    aw.close()
    with capcapopen("exercise13", "r") as ar:
        ar_str = ar.read()
        print(ar_str)
