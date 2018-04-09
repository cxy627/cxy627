# coding:utf-8

'''
一个采集特定网站IP的类
'''

import re
import urllib
import http.cookiejar
import subprocess
from random import choice
from time import sleep


class CollectIp(object):
    def __init__(self):
        hosturl = "http://www.xicidaili.com"
        proxy_ip_list = ["183.159.90.127:18118"]
        self.hosturl = hosturl
        self.proxy_ip_list = proxy_ip_list

    def set_opener(self, inheader):
        while True:
            try:
                proxy_ip = choice(self.proxy_ip_list)
                proxy_support = urllib.request.ProxyHandler(
                    {"http": "http://"+proxy_ip})
                cj = http.cookiejar.LWPCookieJar()
                cookie_support = urllib.request.HTTPCookieProcessor(cj)
                myopener = urllib.request.build_opener(
                    cookie_support, urllib.request.HTTPHandler)
                urllib.request.install_opener(myopener)
                req = urllib.request.Request(self.hosturl)
                for key in inheader:
                    req.add_header(key, inheader[key])
                html = urllib.request.urlopen(req, timeout=1000)
            except (Exception, ConnectionAbortedError) as e:
                try:
                    print(e.value)
                except AttributeError:
                    print("未知错误原因")
                sleep(10)
                continue
            else:
                break
        print("成功初始化")

    def set_header(self):
        header = {
            "Host": "www.xicidaili.com",
            "Referer": "http://www.xicidaili.com/nn",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"
        }
        return header

    def get_html(self, geturl, inheader=None):
        while True:
            try:
                req = urllib.request.Request(geturl)
                for key in inheader:
                    req.add_header(key, inheader[key])
                html = urllib.request.urlopen(req, timeout=10)
            except Exception as e:
                print(e.value)
                continue
            else:
                break
        return html

    def get_ip_list(self, html):
        ss = re.findall(r'<td class="country"><img src="http://fs.xicidaili.com/images/flag/cn.png" alt="Cn" /></td>.*?<td>(.*?)</td>.\s*?<td>(.*?)</td>.\s*?<td>.\s*?<a href=.*?</a>.\s*?</td>.\s*?<td class="country">高匿</td>.\s*?<td>HTTP</td>\n', html, re.DOTALL)
        return ss

    def write_file(self, writeline):
        with open("proxyip.txt", "a", encoding="utf-8") as f:
            f.writelines(writeline)

    def get_ping_result(self, ip_address):
        p = subprocess.Popen("ping.exe -n 1 -w 500 "+ip_address, stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        out = p.stdout.read().decode('gbk')
        reg_receive = '已接收 = \d'
        match_receive = re.search(reg_receive, out)

        receive_count = -1

        if match_receive:
            receive_count = int(match_receive.group()[6:])

        if receive_count > 0:  # 接受到的反馈大于0，表示网络通
            return True
        else:
            return False


if __name__ == "__main__":
    writeip = []
    ipcj1 = CollectIp()
    this_header = ipcj1.set_header()
    ipcj1.set_opener(this_header)
    for count in range(1, 2849):
        geturl = "http://www.xicidaili.com/nn/"+str(count)
        this_page_writeip=[]
        falsetime=0
        while True:
            try:
                rhtml = ipcj1.get_html(geturl, this_header)
                rhtml = rhtml.read().decode("utf-8")

            except (Exception, ConnectionAbortedError) as e:
                print("第%s页处理失败,30秒后发起重连" % count)
                sleep(30)
                continue
                count+=1
                if falsetime>=5:
                    falsetime=0
                    count+=1
                    print("第%s页处理失败超5次，3分钟后进入下一页" % count)
                    sleep(180)
                    continue
            else:
                print("-----第%s页获取成功-----" % count)
                break
        re_ip = ipcj1.get_ip_list(rhtml)
        for test_ip_item in re_ip:
            if ipcj1.get_ping_result(test_ip_item[0]):
                writeip.append(test_ip_item[0]+":"+test_ip_item[1])
                this_page_writeip.append(test_ip_item[0]+":"+test_ip_item[1]+"\n")
                print("%s 连接 ===> 成功" % test_ip_item[0])
            else: 
                print("%s 连接 ===> 失败" % test_ip_item[0])
        ipcj1.write_file(this_page_writeip)

    print("任务完成,共获得%s个ip" % str(writeip.count))
