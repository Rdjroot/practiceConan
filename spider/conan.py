#-*- coding = utf-8 -*-
#@Time:2021/1/3017:29
#@Author:Linyu
#@Software:PyCharm

import urllib
import urllib.request
import requests
import re
from bs4 import BeautifulSoup
import lxml
from lxml import etree
import xlwt

#施工完成

#main函数
def main():
    baseurl = "https://baike.baidu.com/item/%E5%90%8D%E4%BE%A6%E6%8E%A2%E6%9F%AF%E5%8D%97%E5%90%84%E9%9B%86%E5%88%97%E8%A1%A8"

    i = 1
    j = 1
    datalist = []
    for item in getData(baseurl):
        # print(item[2])
        datalist.append(item)
    # for item in datalist:
    #     print(item['Is'])
    write_to_excel(datalist)

def write_to_excel(datalist):
    workbook = xlwt.Workbook(encoding="utf-8")
    worksheet = workbook.add_sheet('名侦探柯南集数')
    i = 1
    worksheet.write(0,0,"集数(括号内为国内编号)")
    worksheet.write(0,1,"章节名")
    worksheet.write(0,2,"原创")
    worksheet.write(0,3,"出场人物")
    worksheet.write(0,4, "B——黑衣组织；F——FBI；C——CIA（Company）；S——工藤新一（变小前 / 恢复身体后）；H——服部平次")
    worksheet.write(0,5, "K——《魔术快斗》系列角色；Y——《剑勇传说》系列角色；N——《四号三垒》系列角色")

    for items in datalist:
        worksheet.write(i, 0, items["number"])
        worksheet.write(i, 1, items["title"])
        worksheet.write(i, 2, items["Is"])
        worksheet.write(i, 3, items["outing"])
        i = i+1
    workbook.save('Conan.xls')
#获取整个页面信息
def askURL(url):
    head  = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 88.0.4324.104Safari / 537.36"
    }
    #封装request对象
    request = requests.get(url , headers = head)
    html = ""
    try:
        html = request.text
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

def specialTreat(string):
    patterndiv = re.compile('(.*)</.*>(.*).?')
    patternsup = re.compile('(.*?)<.*>')
    schar = ''
    itemdiv = re.findall(patterndiv, string)

    if len(str(itemdiv)) < 30:
        for item in itemdiv:
            for it in item:
                if schar:
                    schar = schar + ':' + str(it)
                else:
                    schar = schar + str(it)
        # print('运行1')
    else:
        itemsup = re.findall(patternsup, string)
        k = 0
        for item in itemsup:
            schar = schar + str(item)
            k = k+1
            if k != 0:
                break
        # print('运行2')
    return schar

def getData(baseurl):
    datalist = []
    url = baseurl
    html = askURL(url)
    soup = BeautifulSoup(html,'lxml')

    pattern = re.compile('<tr><td align="center".*?><div class="para" label-module="para"><?b?>?(.*?)<?/?b?>?</div></td>'
                         '<td align="center".*?><div class="para" label-module="para"><?b?>?(.*?)<?/?b?>?</div></td>'
                         + '<td .*?>(.*?)</td>'
                         + '<td .*?>(.*?)</td>', re.S)
    pattern2 = re.compile('<div class="para" label-module="para">(.*?)</div>')
    items = []
    for table in soup.find_all(name='table'):
        for tr in table.find_all(name = 'tr'):
            items.append(tr)
    for item in items:
        its  = re.findall(pattern, str(item))
        # print(its)
        if its :
            for it in its:
                Info = []
                for i in it:
                    k = str(i)
                    Info.append(k)
                if len(Info[1])>20:
                    string = specialTreat(Info[1])
                    Info[1] = string
                if Info[2]:
                    temp = re.findall(pattern2,Info[2])
                    Info[2] = temp
                if Info[3]:
                    temp = re.findall(pattern2,Info[3])
                    Info[3] = temp
                yield {
                    'number': Info[0],
                    'title': Info[1],
                    'Is': Info[2],
                    'outing': Info[3],
                    }
            # for it in its:
            #     it2 = ()
            #     if it[2] and it[3]:
            #         a = it[0]
            #         b = it[1]
            #         temp1 = re.findall(pattern2, it[2])
            #         temp2 = re.findall(pattern2,it[3])
            #         it2 = (a,b,temp1,temp2)
            #     elif it[3]:
            #         temp = re.findall(pattern2,it[3])
            #         a = it[0]
            #         b = it[1]
            #         c = it[2]
            #         it2 = (a,b,c,temp)
            #     elif it[2]:
            #         temp = re.findall(pattern2, it[2])
            #         a = it[0]
            #         b = it[1]
            #         d = it[3]
            #         it2 = (a, b, temp,d)
            #     else:
            #         a = it[0]
            #         b = it[1]
            #         c = it[2]
            #         d = it[3]
            #         it2 = (a, b, c, d)
            #     yield {
            #         'number': it2[0],
            #         'title': it2[1],
            #         'Is': it2[2],
            #         'outing': it2[3],
            #     }




#程序入口
if __name__ == "__main__":
    main()
    print("over")
