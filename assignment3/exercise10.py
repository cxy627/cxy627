def printf(caozuofu, *inlist):
    if caozuofu.count("%") != len(inlist):
        print("长度不符，请重新输入")
        return None
    try:
        print(caozuofu % inlist)
    except (TypeError, ValueError):
        print("格式化操作符方法不适用对应字符")
    return None


printf("%s, %d, %f", "aaa", 10.54, 10)
