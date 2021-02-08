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
import xlwt

#施工完成

#main函数
def main():
    #待爬取的原网页
    baseurl = "https://baike.baidu.com/item/%E5%90%8D%E4%BE%A6%E6%8E%A2%E6%9F%AF%E5%8D%97%E5%90%84%E9%9B%86%E5%88%97%E8%A1%A8"
    #数据最终存入的列表
    datalist = []
    #获取所需信息

    for item in getData(baseurl):
    #     # print(item[2])
    #     #将信息加入列表
        datalist.append(item)
#     #将信息写入Excel文档
    write_to_excel(datalist)

#构造Excel文档
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
    #装作响应头
    head  = {
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 88.0.4324.104Safari / 537.36"
    }
    #封装request对象
    request = requests.get(url , headers = head)
    html = ""
    try:
        #获取网页源代码文档
        html = request.text
        #print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

#处理标题里的特殊不匹配字串，如待引用的以及标题分段的
def specialTreat(string):
    #两种情况的正则表达式
    patterndiv = re.compile('(.*)</.*>(.*).?')
    patternsup = re.compile('(.*?)<.*>')
    schar = ''
    itemdiv = re.findall(patterndiv, string)

    #将匹配结果构造出我们要的字符串
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

#获取内容
def getData(baseurl):
    datalist = []
    url = baseurl
    html = askURL(url)
    #解析HTML文件
    soup = BeautifulSoup(html,'lxml')

    #总的正则表达式，含四个信息
    pattern = re.compile('<tr><td align="center".*?><div class="para" label-module="para"><?b?>?(.*?)<?/?b?>?</div></td>'
                         '<td align="center".*?><div class="para" label-module="para"><?b?>?(.*?)<?/?b?>?</div></td>'
                         + '<td .*?>(.*?)</td>'
                         + '<td .*?>(.*?)</td>', re.S)

    #用于原创和特殊出场人物元素特殊情况修正的正则表达式
    pattern2 = re.compile('<div class="para" label-module="para">(.*?)</div>')

    #暂时存储所有提取出的内容
    items = []
    #采用bs4所待的筛选器，找出所有的tr标签内容
    for table in soup.find_all(name='table'):
        for tr in table.find_all(name = 'tr'):
            items.append(tr)
    #这里的一个item就是一条tr标签内容
    for item in items:
        #将一条标签中符合条件的内容存储到its,这里的一个its是一个列表
        #并且这个列表里只有一个元素，这个元素是一个元组
        its  = re.findall(pattern, str(item))
        print(its)
        print("换行")
        # 如果此列表不为空
        if its :
            #这里的it就是元组了，里面包含四个元素
            for it in its:
                Info = []
                #将元组里的内容存到列表中，便于以下操作
                for i in it:
                    k = str(i)
                    Info.append(k)

                #当标题、原创、特殊出场为特殊情况时
                if len(Info[1])>20:
                    string = specialTreat(Info[1])
                    Info[1] = string
                if Info[2]:
                    temp = re.findall(pattern2,Info[2])
                    Info[2] = temp
                if Info[3]:
                    temp = re.findall(pattern2,Info[3])
                    Info[3] = temp
                #生成器，返回
                yield {
                    'number': Info[0],
                    'title': Info[1],
                    'Is': Info[2],
                    'outing': Info[3],
                    }


#程序入口
if __name__ == "__main__":
    main()
    #结束反馈
    print("over")
