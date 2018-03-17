#coding:utf-8
'''
'''

def tr(srcstr, dststr, string_deal):
    str_began = list()
    str_end = list()
    str_counter_end = 0
    counter = 1
    string_down = str()
    #如果有可替换的字符串(不区分大小写)则进行替换，否则原样输出
    if string_deal.lower().find(srcstr.lower()) >= 0:
        #根据可替换的字符串数量进行循环
        while counter <= string_deal.lower().count(srcstr.lower()):
            #找到后将替换字符串在原字符串的绝对起点及终点，写入两个列表中进行记录。
            if string_deal[str_counter_end:].lower().find(srcstr.lower()) >= 0:
                replace_began = (string_deal[str_counter_end:].lower().find(srcstr.lower())\
                + str_counter_end)
                str_began.append(replace_began)
                str_end.append(replace_began + len(srcstr) -1)
                #每次循环后，在下次列表记录数据时补上相对被“裁剪”的长度
                str_counter_end = str_end[counter-1] + 1
                counter += 1
        replace_counter = 0
        #根据找到的可替换的字段数量进行循环
        for replace_counter in range(0, len(str_began)):
            #判断被替换的字段是否处于第一位
            if str_began[replace_counter] != 0:
                #判断是否是第一个被替换的字符串,是第一个替换的话前面的字段都要保留
                if replace_counter != 0:
                    #判断前后两段被替换的字符串中间是否有其它字符
                    if str_began[replace_counter]- str_end[replace_counter - 1] > 1:
                        #有则接上两段被替换字符中间的未被替换的字段
                        string_down += string_deal[str_end[replace_counter - 1] + 1\
                        :str_began[replace_counter]]
                else:
                    string_down += string_deal[0:str_began[replace_counter] - 1]
            #插入替换的字符串
            string_down += dststr
        #如果最后一个被替换的字符串后还有剩余字符，补上去
        if str_end[replace_counter] != len(string_deal)-1:
            string_down += string_deal[str_end[replace_counter] + 1:]
        print(string_down)
        return string_down
    else:
        print(string_deal)
        return string_deal

if __name__ == "__main__":
    tr("abc123", "#########", "AbC123fewaf21aBc123123crfabC123123ABc12321fwABC123ag4aBc123tv3e")
