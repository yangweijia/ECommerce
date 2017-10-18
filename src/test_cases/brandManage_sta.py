# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from page_obj.loginPage import loginPage
from page_obj.brandManagePage import brandManagePage
from page_obj.base import Page
from models.myunit import MyTest
from models.function import insert_img
from models.star import  brower
from HTMLTestRunner import HTMLTestRunner

class brandManage_sta(MyTest):
    url = "https://admin.codoon.com/admin/oper_ms/html/tags/brand-manage.html"           
    driver = brower()
    driver.maximize_window()
    
    def setUp(self):
        self.verificationErrors = []
    
    #创建品牌
    def test_001(self):
        loginPage(self.driver).login("Oper","Oper",self.url)
        driver = self.driver
        
        po = brandManagePage(self.driver)
        po.brandManage_newBrand()
        po.brandManage_brandName("YY")
        po.brandManage_uploadPic("C:\\Users\\yangweijia\\Pictures\\jpg\\NEW\\S0FFVHAreFdGdjVKU01OcjRyamhHamJaeFdhN0ppQ0VLdzNteldtbVhqUmtxUUIzOGNQc3pnPT0.jpg")
        po.brandManage_brandNick("X")
        po.brandManage_AddbrandNick()
        po.brandManage_save()
        insert_img(self.driver, "newBrand.jpg")
        try: self.assertEqual(po.brandManage_newBrand_success(),u"操作成功！")
        except AssertionError as e: self.verificationErrors.append(str(e)+"newBrand")  

    
    def tearDown(self):
#         page = Page(self.driver)
#         page.logout()
        self.assertEqual([], self.verificationErrors)
    
           
if __name__ == "__main__":
    unittest.main()
