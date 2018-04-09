#coding:utf-8
import re

week=("Mon","Tue","Wed","Thu","Fri","Sat","Sun")
with open("redata.txt","r",encoding="utf-8") as f:
    text=f.read()
ss = re.findall(r"Mon|Tue|Wed|Thu|Fri|Sat|Sun",text)
for i in range(7):
    print(week[i]+":",end="")
    print(("".join(ss)).count(week[i]))
