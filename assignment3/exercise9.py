# coding:utf-8
'''
习题11-5
'''


def mathtax(Amount, taxrate=0.06):
    try:
        Amount = float(Amount)
        taxrate = float(taxrate)
    except ValueError:
        print("请输入数字")
        return None
    return Amount*taxrate


if __name__ == "__main__":
    print(mathtax(900000))
