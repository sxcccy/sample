# -*- coding:utf-8 -*-
import urllib
import re
import requests
from lxml import etree
import time


fp = open(r'/home/tyouki/log/61jjj-yazhou-log', 'r')
log = fp.readlines()
fp.close()

url = 'http://www.cfr4.com/AAtupian/AAAtb/asia/'
html = urllib.request.urlopen(url).read()  # 读取首页的内容
selector = etree.HTML(html)  # 转换为xml，用于在接下来识别
links = selector.xpath('//li/a/@href')  # 抓取当前页面的所有帖子的url
titles = selector.xpath('//li/a/text()')
a=[]
for each in links:
    if each[-5:] == '.html':
        a.append(each)

for i in a:
        url1 = 'http://www.cfr4.com' + i
        html2 = urllib.request.urlopen(url1).read()  # 读取当前页面的内容
        selector = etree.HTML(html2)  # 转换为xml用于识别
        link = selector.xpath('//p/img/@src')  # 抓取图片，各位也可以更换为正则，或者其他你想要的内容

        for each in link:
            addlog = each+'\n'
            if addlog not in log:
                try:
                    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
                    req = urllib.request.Request(url=each, headers=headers)
                    fp = open(r'/home/tyouki/img/' + time.asctime() + '.jpg', 'wb')  # 下载在当前目录下 image文件夹内，图片格式为bmp
                    image1 = urllib.request.urlopen(req).read()  # 读取图片的内容
                    fp.write(image1)  # 写入图片
                    fp.close()
                    print(each)
                    log.append(addlog)
                    flog = open(r'/home/tyouki/log/61jjj-yazhou-log', 'a+')
                    flog.write(addlog)
                    flog.close()
                    time.sleep(8)
                except Exception as e:
                    print(e)
            else:
                print('had downloaded')












'''
    for i in links:
        url1 = "http://tieba.baidu.com" + i  # 因为爬取到的地址是相对地址，所以要加上百度的domain
        html2 = urllib.request.urlopen(url1).read()  # 读取当前页面的内容
        selector = etree.HTML(html2)  # 转换为xml用于识别
        link = selector.xpath('//img[@class="BDE_Image"]/@src')  # 抓取图片，各位也可以更换为正则，或者其他你想要的内容
        # print (i)
        # 此处就是遍历下载
        for each in link:
            # print (each)
            print(u'正在下载%d' % k)
            fp = open('D:\\Python3\\apps\\Temp\\' + str(k) + '.bmp', 'wb')  # 下载在当前目录下 image文件夹内，图片格式为bmp
            image1 = urllib.request.urlopen(each).read()  # 读取图片的内容
            fp.write(image1)  # 写入图片
            fp.close()
            k += 1  # k就是文件的名字，每下载一个文件就加1
'''

print(u'下载完成!')
