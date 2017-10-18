# -*- coding: utf-8 -*-
'''
Created on 20161020

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
from page_obj.orderMsPage import orderMsPage
from selenium import webdriver
import unittest, time

class orderMs_sta(MyTest):
    url = "https://admin.codoon.com/admin/html/order/order-ms.html"
    driver = brower()
    driver.maximize_window()
    
    def setUp(self):
        self.verificationErrors = []
        
    def test_001(self):
        """
                        三方商户
                        订单ID搜索——》退款
        """
        loginPage(self.driver).login("admin","admin",self.url)
        search = Search(self.driver)
        po = orderMsPage(self.driver)
        search.orderIdInput(102376960241237453801179)
        search.searchButton()
        po.refundButton()
        po.refundNumSelec("1","1")
        po.refundReasonInput(u"退款原因")
        po.confirmOfRefundButton(True)

        insert_img(self.driver, "orderMs_test_001.jpg")
        
        try: self.assertEqual(u"成功",po.getTipText())
        except AssertionError as e: self.verificationErrors.append("001")
    
    def test_002(self):
        """
                        三方商户
                        订单ID搜索——》部分退款
        """
        loginPage(self.driver).login("admin","admin",self.url)
        search = Search(self.driver)
        po = orderMsPage(self.driver)
        search.orderIdInput(172633044241312573652709)
        search.searchButton()
        po.refundButton()
        po.refundNumSelec("1")
        po.refundFeeInput(0)
        po.refundReasonInput(u"退款原因")
        po.confirmOfRefundButton(False)

        insert_img(self.driver, "orderMs_test_002.jpg")
        
        try: self.assertEqual(u"成功",po.getTipText())
        except AssertionError as e: self.verificationErrors.append("002")
    
    def test_003(self):
        """
                        三方商户
                        订单ID搜索——》退货完全退款
        """
        loginPage(self.driver).login("admin","admin",self.url)
        search = Search(self.driver)
        po = orderMsPage(self.driver)
        search.orderIdInput(414142828241325152668183)
        search.searchButton()
        po.refundButton()
        po.refundNumSelec("1","2")
        po.mailCompanyInput(u"韵达")
        po.mailNumInput("hcfsdhvfidi")
        po.refundReasonInput(u"退货原因")
        po.confirmOfReturnButton(True)

        insert_img(self.driver, "orderMs_test_003.jpg")
        
        try: self.assertEqual(u"成功",po.getTipText())
        except AssertionError as e: self.verificationErrors.append("003")
        
    def test_004(self):
        """
                        三方商户
                        订单ID搜索——》退货部分退款
        """
        loginPage(self.driver).login("admin","admin",self.url)
        search = Search(self.driver)
        po = orderMsPage(self.driver)
        search.orderIdInput(70567080541321359850778)
        search.searchButton()
        po.refundButton()
        po.refundNumSelec("1","2","3")
        po.mailCompanyInput(u"韵达")
        po.mailNumInput("hcfsdhvfidi")
        po.refundFeeInput(0)
        po.refundReasonInput(u"退货原因")
        po.confirmOfReturnButton(False)

        insert_img(self.driver, "orderMs_test_004.jpg")
        
        try: self.assertEqual(u"成功",po.getTipText())
        except AssertionError as e: self.verificationErrors.append("004")
        
        
    def tearDown(self):
        time.sleep(2)
        page = Page(self.driver)
        page.logout()
        self.assertEqual([], self.verificationErrors)
        
if __name__ == "__main__":
#     unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(orderMs_sta("test_006"))
    runner = unittest.TextTestRunner()
    runner.run(suite) 
