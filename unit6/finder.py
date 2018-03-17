#utf-8

def findchr(string, char):
    i = -1
    for i in range(0,len(string)):
        if char == string[i]:
            break
    return i

def rfindchr(string, char):
    i = -1
    for i in range(len(string),0,-1):
        if char == string[i-1]:
            break
    return (i-1)

def subchr(string, origchar,newchar):
    outstring = ''
    for i in range(0,len(string)):
        if origchar == string[i]:
            outstring += newchar
        else:
            outstring += string[i]
    return outstring

a = subchr("abdjshjw","j","i")
print(a)