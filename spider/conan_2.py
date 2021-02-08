#-*- coding = utf-8 -*-
#@Time:2021/1/3019:03
#@Author:Linyu
#@Software:PyCharm

from selenium import webdriver
import re
import xlwt


#施工未完成，作废

#写入Excel文件
def WriteExcel(list):
    pass

#获取数据
def getData(browser):
    #总列表
    topInfos = []
    test = browser.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/table[1]/tbody')
    print(type(test))
    # while True:
    #     try:
    #         for i in range(1,13):
    #             metaInfos = {}
    #             #获取集数
    #             number = browser.find_elemt_by_
    #     except Exception as e :
    #         break
    return topInfos



#启动浏览器进行爬虫
def main():
    browser = webdriver.Chrome()
    browser.get("https://baike.baidu.com/item/%E5%90%8D%E4%BE%A6%E6%8E%A2%E6%9F%AF%E5%8D%97%E5%90%84%E9%9B%86%E5%88%97%E8%A1%A8")
    #writeExcel(getData(browser))
    getData(browser)
if __name__ == '__main__':
    print("ok")
    main()