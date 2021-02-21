#-*- coding = utf-8 -*-
#@Time:2021/2/720:58
#@Author:Linyu
#@Software:PyCharm
import re

#以下为正则表达式测试

# text = '<tr><td align="center"><div class="para" label-module="para">1</div></td><td align="center"><div class="para" label-module="para">云霄飞车杀人事件</div></td><td align="center"></td><td align="center"><div class="para" label-module="para">B/S</div></td><td align="center" rowspan="2"><div class="para" label-module="para"><a data-lemmaid="3494663" href="/item/%E6%9F%8F%E5%8E%9F%E5%AE%BD%E5%8F%B8/3494663" target="_blank">柏原宽司</a></div></td><td align="center" rowspan="10"><div class="para" label-module="para">-</div></td><td align="center" rowspan="2"><div class="para" label-module="para"><a data-lemmaid="11055588" href="/item/%E5%84%BF%E7%8E%89%E5%85%BC%E5%97%A3/11055588" target="_blank">儿玉兼嗣</a></div></td><td align="center" rowspan="2"><div class="para" label-module="para"><a data-lemmaid="51665957" href="/item/%E9%A1%BB%E8%97%A4%E6%98%8C%E6%9C%8B/51665957" target="_blank">须藤昌朋</a></div></td></tr>'

# text = '<tr><td align="center"><div class="para" label-module="para"><b>964（1021）</b></div></td><td align="center"><div class="para" label-module="para"><b>毛利小五郎的盛大演讲会（下集）</b></div></td><td align="center"><div class="para" label-module="para">√</div></td><td align="center"></td><td align="center"><div class="para" label-module="para">津吹明日香</div><div class="para" label-module="para">山本道隆</div></td></tr>'
# pattern = re.compile('<tr><td align="center".*?><div class="para" label-module="para"><?b?>?(.*?)<?/?b?>?</div></td>'
#                      '<td align="center".*?><div class="para" label-module="para"><?b?>?(.*?)<?/?b?>?</div></td>'
#                      + '<td .*?>(.*?)</td>'
#                      + '<td .*?>(.*?)</td>', re.S)
# text = '<div class="para" label-module="para">B/S</div>'
# text = '<div class="para" label-module="para">√</div>'
# pattern = re.compile('<div class="para" label-module="para">(.*?)</div>')
chapter = '走投无路的名侦探</div><div class="para" label-module="para">连续两大杀人事件'
chapter2 = '目标是警视厅交通部（四）<sup class=""sup--normal"" data-ctrmap="":2,"" data-sup=""2"">[2]</sup><a class=""sup-anchor"" name=""ref_[2]_25263565""> </a>'
chapter3 = '寻妻的秘密</b><sup class="sup--normal" data-ctrmap=":3," data-sup="3">[3]</sup><a class="sup-anchor" name="ref_[3]_25263565"> </a>'
def spe(string):
    patterndiv = re.compile('(.*)</.*>(.*).?')
    patternsup = re.compile('(.*?)<.*>')
    schar = ''
    itemdiv = re.findall(patterndiv,string)

    if len(str(itemdiv))<30:
        for item in itemdiv:
            for it in item:
                if schar:
                    schar = schar + ':' + str(it)
                else:
                    schar = schar +str(it)
        print('运行1')
    else:
        itemsup = re.findall(patternsup,string)
        for item in itemsup:
            schar = schar + str(item)
        print('运行2')
    return schar
print(spe(chapter))
print(spe(chapter2))
print(spe(chapter3))


# for item in items:
#     for it in item:
#         if schar:
#             schar = schar + ':' + str(it)
#         else:
#             schar = schar +str(it)
# print(schar)
# # pattern = re.compile('(.*?)<.*>')
# items = re.findall(pattern,chapter)
# schar = ''
# for item in items:
#     schar = schar +str(item)
# print(schar)
