def importAs(modulename):
    name = __import__(modulename)
    return name

if __name__=="__main__":
    ti = importAs("time")
    print(ti.ctime())
