# coding:utf-8

from random import randint, choice
from string import ascii_lowercase as lowercase
from time import ctime

def gendata():
    doms = ("com", "edu", "net", "org", "gov")
    f = open("redata.txt","w",encoding="utf-8")
    for i in range(randint(5, 10)):
        dtint = randint(0, 2000000000)#用原例子会导致OSError: [Errno 22] Invalid argument
        dtstr = ctime(dtint)
        shorter = randint(4, 7)
        em = ""
        for j in range(shorter):
            em += choice(lowercase)
        longer = randint(shorter, 12)
        dn = ''
        for j in range(longer):
            dn += choice(lowercase)
        thisline = ("%s::%s@%s.%s::%d-%d-%d" %
            (dtstr, em, dn, choice(doms), dtint, shorter, longer))
        f.write(thisline+"\n")
    f.close()  
 
if __name__=="__main__":
     gendata()
