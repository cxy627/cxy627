# coding:utf-8
'''
通过实验，发现由于读取文件占据绝大部分时间，而文件无法并发读取，因此无论单线程
还是多线程都占了这个速度的亏。在大文件时多线程因频繁加锁反而会略慢，在小文件时
多线程因为提前处理部分内容，相对较快。速度是制约于硬盘读取速度的。
'''
import random
import threading
import queue
import time


class FileCreater(object):
    '''
    生成二进制数据文件
    '''

    def __init__(self, totalnum, filename):
        self.totalnum = totalnum
        self.filename = filename

    def producer(self):
        prod_list = []
        for i in range(self.totalnum):
            prod_list.append(bin(random.randint(0, 255)))
        return prod_list

    def saver(self, save_list):
        with open(self.filename, mode="w", encoding="UTF-8") as f:
            for i in range(self.totalnum):
                f.write(str(save_list[i])+"\n")


class Seacher(threading.Thread):
    '''
    为了防止因线程库导致的性能损耗，
    单线程及多线程都由线程库进行创建。
    '''

    def __init__(self, filename, reslut_list):
        self.filename = filename
        self.reslut_list = reslut_list
        super(Seacher, self).__init__(name="Seacher")

    def run(self):
        with open(self.filename, mode="r", encoding="utf-8") as f:
            produce_list = []
            for i in f:
                produce_list.append(i[:-1])
        for i in range(256):
            self.reslut_list[i] += produce_list.count(str(bin(i)))


class MultiProducer(threading.Thread):
    '''
    多线程中的读取文件的子线程
    '''

    def __init__(self, queue, filename):
        self.filename = filename
        self.queue = queue
        super(MultiProducer, self).__init__(name="MultiProducer")

    def run(self):
        with open(self.filename, mode="r", encoding="utf-8") as f:
            produce_list = []
            count = 0
            for i in f:
                produce_list.append(i[:-1])
                count += 1
                if count % 200 == 0:
                    self.queue.put(produce_list)
                    produce_list = []
            if produce_list != []:
                self.queue.put(produce_list)
                produce_list = []

class MultiCosumer(threading.Thread):
    '''
    多线程中负责统计的子线程
    '''

    def __init__(self, queue, reslut_list, lock):
        self.queue = queue
        self.reslut_list = reslut_list
        self.lock = lock
        super(MultiCosumer, self).__init__(name="MultiCosumer")

    def run(self):
        this_result = [0]*256
        while True:
            consume_list = self.queue.get(1)
            for i in range(256):
                this_result[i] += consume_list.count(str(bin(i)))
            self.lock.acquire()
            for i in range(256):
                self.reslut_list[i] += this_result[i]
            self.lock.release()
            this_result = [0]*256
            self.queue.task_done()


def single_run():
    '''
    用于单线程任务的变量定义，运行，显示结果
    '''
    # 单线程线程建立
    reslut_list = [0]*256
    s1 = Seacher(filename, reslut_list)

    # 单线程正式运行
    start = time.time()
    s1.start()
    s1.join()
    end = time.time()

    # 单线程结果显示
    print("单线程用时:%s" % (end-start))
    sum = 0
    for i in reslut_list:
        sum += i
    # print("单线程统计总数:", sum)
    # print("单线程计算结果:")
    # print(reslut_list)


def multi_run():
    '''
    用于多线程任务的变量定义，运行，显示结果
    '''
    # 多线程队列，线程，锁的建立
    multi_queue = queue.Queue()
    reslut_list = [0]*256
    wlock = threading.Lock()
    mp = MultiProducer(multi_queue, filename)
    pd_thread_list = []
    for i in range(10):
        mc = MultiCosumer(multi_queue, reslut_list, wlock)
        mc.setDaemon(True)
        pd_thread_list.append(mc)

    # 多线程正式运行
    start = time.time()
    mp.start()
    thread_num = range(len(pd_thread_list))
    for i in thread_num:
        pd_thread_list[i].start()
    mp.join()
    multi_queue.join()
    end = time.time()

    # 多线程结果显示
    print("多线程用时:%s" % (end-start))
    sum = 0
    for i in reslut_list:
        sum += i
    # print("多线程统计总数:", sum)
    # print("多线程计算结果:")
    # print(reslut_list)


if __name__ == "__main__":

    for totalnum in [3000, 30000, 300000, 3000000]:
        filename = "as8ex4.txt"
        print("\n创建字节数为%s的文件中" % totalnum)
        f1 = FileCreater(totalnum, filename)
        f1.saver(f1.producer())
        print("创建完成\n")

        print("单线程计算中")
        single_run()

        time.sleep(0.5)
        
        print("\n多线程计算中")
        multi_run()

        print("\n")
        print("*"*20)
