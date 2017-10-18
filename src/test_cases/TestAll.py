# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from setuptools.windows_support import hide_file
from login_sta import loginTest
from HTMLTestRunner import HTMLTestRunner   


if __name__ == "__main__":   
    moduleList = ['orderReturnMs_sta','orderMs_sta']         
    for moduleName in moduleList:
            testClass = getattr(__import__(moduleName),moduleName)
            suite = unittest.makeSuite(testClass, "test")
            runner = unittest.TextTestRunner()
            runner.run(suite)
            
    
#            discover = unittest.defaultTestLoader.discover("./", pattern="NewBrand.py")
#            fp = open('./result.html','wb')
#            runner = HTMLTestRunner(stream=fp,title='电商后台品牌管理测试报告',description='用例执行情况：')
#            runner.run(discover)
#            fp.close()
            
            
            