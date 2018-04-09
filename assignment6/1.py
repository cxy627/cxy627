import urllib
import http.cookiejar
import re


hosturl = "https://www.baidu.com"
header = {
    "DNT": 1,
    "Host": "www.baidu.com",
    "is_referer": "https://www.baidu.com/",
    "is_xhr": 1,
    "Referer": "https://www.baidu.com/s?ie=utf-8&f=3&rsv_bp=0&rsv_idx=1&tn=baidu&wd=%E7%A7%91%E6%8A%80&rsv_pq=c678be190000286d&rsv_t=acf7SmVE6TYQPxJqgq5k5FbcLmjOFj8XX%2BZQTbYi5UWTm7EQL5I4xJk7%2BZk&rqlang=cn&rsv_enter=0&rsv_sug3=7&rsv_sug1=4&rsv_sug7=100&prefixsug=%25E7%25A7%2591%25E6%258A%2580&rsp=0&inputT=18453&rsv_sug4=38267",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
    "X-Requested-With": "XMLHttpRequest"
}

cj = http.cookiejar.LWPCookieJar()
cookie_supportr = urllib.request.HTTPCookieProcessor(cj)
opener = urllib.request.build_opener(
    cookie_supportr, urllib.request.HTTPHandler)
urllib.request.install_opener(opener)
h = urllib.request.urlopen(hosturl)
kw_list = ("科技", "创新")
for kw in kw_list:
    kw = urllib.request.quote(kw)
    get_url = "https://www.baidu.com/s?ie=utf-8&mod=1&isbd=1&isid=4EE86D6B1C969757&ie=utf-8&f=3&rsv_bp=0&rsv_idx=1&tn=baidu&wd="+kw + \
        "&rsv_pq=c678be190000286d&rsv_t=acf7SmVE6TYQPxJqgq5k5FbcLmjOFj8XX%2BZQTbYi5UWTm7EQL5I4xJk7%2BZk&rqlang=cn&rsv_enter=0&rsv_sug3=7&rsv_sug1=4&rsv_sug7=100&prefixsug=%25E7%25A7%2591%25E6%258A%2580&rsp=0&inputT=18453&rsv_sug4=38267&rsv_sid=1428_21100_22075&_ss=1&clist=&hsug=&f4s=1&csor=2&_cr1=30651"
    req = urllib.request.Request(get_url)
    for key in header:
        req.add_header(key, header[key])
    r = urllib.request.urlopen(req)
    html = r.read().decode("utf-8")
    ss = re.findall("rsv_cq="+kw+"'>(.*?)</a>", html)   
    print(ss)
