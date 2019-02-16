#-*- coding:utf-8 -*-
from selenium import webdriver
import time
import pymouse,os,sys
from pymouse import *

try:
    while True:
        print("Press Ctrl-C to end")
        #ubuntu系统下的firefox插件路径:
        profile_directory=r'/home/tyouki/.mozilla/firefox/j0lo9hlr.default/'
        # 加载插件配置
        profile = webdriver.FirefoxProfile(profile_directory)
        # 启动浏览器配置
        driver = webdriver.Firefox(profile)
        time.sleep(5)
        #启动鼠标
        m = PyMouse()
        m.click(1862, 109,1,1)
        time.sleep(5)
        m.click(1768, 160,1,1)
        time.sleep(120)
        driver.quit()
        time.sleep(5)
except  KeyboardInterrupt:
    print ('end....')