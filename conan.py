#-*- coding = utf-8 -*-
#@Time:2021/1/3017:29
#@Author:Linyu
#@Software:PyCharm

import urllib
import urllib.request
import re
from bs4 import BeautifulSoup
import xlwt

#施工未完成
#main函数
def main():
    baseurl = "https://baike.baidu.com/item/%E5%90%8D%E4%BE%A6%E6%8E%A2%E6%9F%AF%E5%8D%97%E5%90%84%E9%9B%86%E5%88%97%E8%A1%A8"
    datalist = getData(baseurl)

def askURL(url):
    head  = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 88.0.4324.104Safari / 537.36"
    }
    #封装request对象
    request = urllib.request.Request(url,headers = head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html


def getData(baseurl):
    datalist = []
    url = baseurl
    html = askURL(url)
    k = 1

    soup = BeautifulSoup(html,"html.parser")
    # print(soup.body.div.table.content)
    for tr in soup.find_all(name = 'tr'):
        k = k+1
        #print(tr)
    trlist = list(tr)
    print(trlist[0].string)



#程序入口
if __name__ == "__main__":
    main()
