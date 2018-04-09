import re
from time import strftime,localtime
def checkfile():
    check = True
    f=open("redata.txt","r",encoding="utf-8") 
    for i in f.readlines():
        ss= re.search(r"^(\w\w\w).*::(\d+)-",i)
        if ss:
            if ss.group(1) !=strftime("%a",localtime(int(ss.group(2)))):
                check =False
        else:
            check = False
    f.close()
    print(check)

if __name__=="__main__":
    checkfile()
