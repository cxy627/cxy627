# coding:utf-8
'''
'''

from string import punctuation
import codecs


def main():
    text = str()
    f = codecs.open("gettysburg.txt", "r", "utf-8")
    strfile = str(f.readlines())
    f.close
    for i in strfile:
        if i not in punctuation:
            text += i.lower()

    allw = text.split(" ")
    allword = [item for item in allw if len(item) >= 1]
    norepeatword = tuple(set(allword))
    print("\n本文件所有单词共%s个,分别为:%s\n" % (len(allword), allword))
    print("-"*20)
    print("\n本文件所有不重复的单词共%s个,分别为:%s\n" % (len(norepeatword), norepeatword))
    print("-"*20)
    print("\n以下为所有单词频次表\n")
    for word in norepeatword:
        print("单词:%s 频次:%s" % (word.ljust(15), allword.count(word)))


if __name__ == "__main__":
    main()
