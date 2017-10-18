# -*- coding: utf-8 -*-
'''
Created on 20161021

@author: yangweijia
'''
import sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models.myunit import MyTest
from models.star import brower
from models.function import insert_img
from page_obj.loginPage import loginPage
from page_obj.base import Page
from page_obj.Search import Search
from page_obj.orderReturnMsPage import orderReturnMsPage
from selenium import webdriver
import unittest, time

class orderReturnMs_sta(MyTest):
    url = "https://admin.codoon.com/admin/html/inventory/order-return-ms.html"
    driver = brower()
    driver.maximize_window()
    
    def setUp(self):
        self.verificationErrors = []
    
    def test_001(self):
        """
                        三方商户
                        订单ID搜索，确认退货
        """
        loginPage(self.driver).login("admin","admin",self.url)
        search = Search(self.driver)
        po = orderReturnMsPage(self.driver)
        search.orderIdInput(102376960241237453801179)
        search.searchButton()
        po.refundButton()
        po.confirmButton()

        insert_img(self.driver, "orderReturnMs_test_001.jpg")
        
        try: self.assertEqual(u"成功",po.getTipText())
        except AssertionError as e: self.verificationErrors.append("001")
    
    def tearDown(self):
        time.sleep(2)
        page = Page(self.driver)
        page.logout()
        self.assertEqual([], self.verificationErrors)
        
if __name__ == "__main__":
#     unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(orderReturnMs_sta("test_001"))
    runner = unittest.TextTestRunner()
    runner.run(suite) 