# -*- coding:utf-8 -*-
import urllib
import re
import requests
import csv
from lxml import etree

links = []
username = []
# 遍历url的地址
print(u'请输入最后的页数：')
endPage = int(input()) + 1  # 最终的页数　
csvFile2 = open('D:\\Python3\\apps\\Temp\\' + 'forum.worldofwarships.username.csv','w', newline='')
writer = csv.writer(csvFile2)
for j in range(1, endPage):
    url = 'https://forum.worldofwarships.com/forum/35-general-game-discussion/?page=' + str(j)
    print(url)
    html = urllib.request.urlopen(url).read()  # 读取首页的内容
    selector = etree.HTML(html)  # 转换为xml，用于在接下来识别
    links = selector.xpath('//span/a[@class=""][@title][@data-ipshover-timeout]/@href')

    for i in links:
        html2 = urllib.request.urlopen(i).read()  # 读取当前页面的内容
        selector = etree.HTML(html2)  # 转换为xml用于识别
        link = selector.xpath('//a[@href][@title][@class="ipsType_break"]/text()')
        link = set(link)  # 去重复
        # 此处就是遍历下载
        for each in link:
            if each not in username:
                username.append(each)
                # print (each)
                writer.writerow([each + '@gmail.com'])
                writer.writerow([each + '@hotmail.com'])
                writer.writerow([each + '@yahoo.com'])

print(u'下载完成!')
csvFile2.close()
