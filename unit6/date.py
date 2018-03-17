#coding:utf-8
'''
'''
def inputdate():
    i = 1
    change = {1:"年",2:"月",3:"日"}
    while i<=3:
        print("请输入%s:" % change[i], end='')
        text = input()
        if text.isdigit():
            text = int(text)
        else:
            print("错误,请输入纯数字")
            continue
        if i == 1:
            if 1 <= text <= 5000:
                year = text
            else:
                continue
        elif i == 2:
            if 1 <= text <= 12:
                month = text
            else:
                print("请输入正确月份")
                continue
        elif i == 3:
            if 1 <= text <= 31:
                if month == 2:
                    if year % 4 == 0 and text <= 29:
                        day = text
                    elif year % 4 != 0 and text <= 28:
                        day = text
                    else:
                        print("本年2月无所输天数，请重新输入")
                        continue
                elif month in (4,6,9,11) and text == 31:
                    print("本月无第31天，请重新输入")
                    continue
                elif text > 31:
                    print("无所输日期，请重新输入")
                else:
                    day =text
        i += 1
    print("所输入日期:%s年%s月%s日" % (year, month, day))
    return year,month,day

def date_sum(input_year1,input_month1,input_day1,input_year2,input_month2,input_day2):
    date_counter = 0
    month_date_dict = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    reverse_flag = 0#判断日期大小，如果2比1大，就反过来，并标记，完成后1比2大
    if input_year2 > input_year1:
        (input_year2,input_month2,input_day2,input_year1,input_month1,input_day1)\
         = (input_year1,input_month1,input_day1,input_year2,input_month2,input_day2)
        reverse_flag = 1
    elif input_year1 == input_year2 and input_month2 > input_month1:
        (input_year2,input_month2,input_day2,input_year1,input_month1,input_day1)\
         = (input_year1,input_month1,input_day1,input_year2,input_month2,input_day2)
        reverse_flag = 1
    elif input_year1 == input_year2 and input_month1 == input_month2 \
    and input_day2 > input_day1:
        (input_year2,input_month2,input_day2,input_year1,input_month1,input_day1)\
         = (input_year1,input_month1,input_day1,input_year2,input_month2,input_day2)
        reverse_flag = 1

    if input_year1 - input_year2 <= 1:
        pass
    else:
        for year_counter in range(input_year2+1,input_year1):
            if year_counter % 4 == 0:
                date_counter += 366
            else:
                date_counter += 365

    if input_year1 == input_year2 and input_month1 - input_month2 <= 1:
        pass
    elif input_year1 == input_year2:
        for i in range(input_month2+1,input_month1):
            date_counter += month_date_dict[i]
    else:
        if input_month1 == 1:
            pass
        else:
            for i in range(1,input_month1):
                date_counter += month_date_dict[i]
        if input_month2 == 12:
            pass
        else:
            for i in range(input_month2+1,13):
                date_counter += month_date_dict[i]
        

    if input_year1 == input_year2 and input_month1==input_month2:
        date_counter += input_day1 -input_day2
    else:
        date_counter += input_day1 + (month_date_dict[input_month2] - input_day2) 

    print("第一个日期比第二个日期%s%s天" % ({0:"多",1:"少"}[ reverse_flag],date_counter))
    date_counter_return = date_counter
    if reverse_flag == 1:
        date_counter_return = -date_counter_return
    return(date_counter_return)


def main():
    redate = list()
    print("\n------输入日期------")
    for a in range(1,3):
        print("\n请输入第%s个日期:" % a)
        redate.extend(inputdate())
    confirm = "N"
    while True:
        print("\n------输入完成------\n\n第一个日期为%s年%s月%s日\n第二个日期为%s年%s月%s日\n确认请输入Y,重新输入请按N\n请输入:" %  tuple(redate), end='')
        confirm = str(input())
        if confirm != "Y" and confirm != "y" and confirm != "N" and confirm != "n":
            print("输入错误,请重新输入!")
            continue
        if confirm == "N" or confirm == "n":
            redate = list()
            print("\n------输入日期------")
            for a in range(1,3):
                print("\n请输入第%s个日期:" % a)
                redate.extend(inputdate())
        if confirm == "Y" or confirm == "y":
            break
    print("\n------相差日期------\n")        
    date_sum(*redate)

main()

