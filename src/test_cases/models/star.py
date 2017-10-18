# -*- coding: utf-8 -*-
from selenium import webdriver

#启动浏览器驱动
def brower():
    print "driver"
    driver = webdriver.Chrome()
    return driver
