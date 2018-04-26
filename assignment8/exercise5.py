# coding:utf-8
'''
网上实在找不到mailbox是怎样的文件,按我的理解应该就是一个包含超链接，邮箱，内容
的备份文件。。就按这个思路做了
我用随机数生成一个带有邮箱地址以及URL以及文本内容的一个文件
，读取文件和写文件分两个线程。
'''

import random
import re
import threading
import string
import queue


class FileCreater(object):
    '''
    用于生成mailbox文件
    '''

    def __init__(self, filename, totalnum):
        self.filename = filename
        self.totalnum = totalnum
        self.writelist = []

    def file_producer(self):
        text_include = string.ascii_lowercase + string.digits
        tldomainname_list = ["org", "com", "cn", "net"]

        for item in range(totalnum):
            content_length = random.randint(10, 50)
            username_length = random.randint(5, 15)
            domainname_length = random.randint(4, 7)
            myurl_length = random.randint(8, 12)

            myurl = str()
            for i in range(myurl_length):
                myurl += random.choice(text_include)

            content = str()
            for i in range(content_length):
                content += random.choice(text_include)

            username = str()
            for i in range(username_length):
                username += random.choice(text_include)

            domainname = str()
            for i in range(domainname_length):
                domainname += random.choice(text_include)

            tldomainname = random.choice(tldomainname_list)

            text = ("mail:%s@%s.%s url:www.%s.%s content:%s"
                    % (username, domainname, tldomainname,
                       myurl, tldomainname, content))

            self.writelist.append(text)

    def file_saver(self):
        with open(self.filename, mode="w", encoding="utf-8") as f:
            for item in self.writelist:
                f.write(item+"\n")


def multiproducer(mailbox_filename, producer_queue):
    with open(mailbox_filename, mode="r", encoding="utf-8") as f:
        produce_list = []
        count = 0
        for i in f:
            produce_list.append(i[:-1])
            count += 1
            if count % 200 == 0:
                producer_queue.put(produce_list)
                produce_list = []
        if produce_list != []:
            producer_queue.put(produce_list)
            produce_list = []


def multicosumer(producer_queue, result_queue):
    while True:
        handle_text = producer_queue.get(1)
        for item in handle_text:
            ss = re.search(r"mail:([\w\.@]+?)\surl:([\w\.]+?)\s", item)
            if ss is not None:
                thismail = ss.group(1)
                thisurl = ss.group(2)
                result_queue.put("mail:%s url:%s" % (thismail, thisurl))
            else:
                print("内容有误:%s" % item)
        producer_queue.task_done()


def multiwriter(html_filename, result_queue):
    f = open(html_filename, mode="w", encoding="utf-8")
    while True:
        val = result_queue.get(1)
        f.write(val+"\n")
        result_queue.task_done()
    f.close()


def filecreater_run():
    print("开始制作邮件数量为%s的mailbox文件" % totalnum)
    f1 = FileCreater(mailbox_filename, totalnum)
    f1.file_producer()
    f1.file_saver()
    print("制作完成")


def multi_run():
    print("多线程计算中")
    producer_queue = queue.Queue()
    mp = threading.Thread(target=multiproducer, name="multiproducer",
                          args=(mailbox_filename, producer_queue))

    result_queue = queue.Queue()
    mp_list = []
    for i in range(thread_amount):
        mc = threading.Thread(target=multicosumer, name="multicosumer",
                              args=(producer_queue, result_queue))
        mc.setDaemon(True)
        mp_list.append(mc)

    mw = threading.Thread(target=multiwriter, name="multiwriter",
                          args=(html_filename, result_queue))
    mw.setDaemon(True)

    mp.start()
    for i in range(thread_amount):
        mp_list[i].start()
    mw.start()

    producer_queue.join()
    result_queue.join()
    print("计算完成")


if __name__ == "__main__":
    mailbox_filename = "as8ex5.mailbox"
    html_filename = "as8ex5.html"
    totalnum = 10000
    thread_amount = 10

    filecreater_run()

    multi_run()

    with open(html_filename, mode="r", encoding="utf-8") as f:
        print(f.read())
