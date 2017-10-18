# -*- coding: utf-8 -*-
'''
Created on 20161018

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
from page_obj.orderDeliverConfirmPage import orderDeliverConfirmPage
from selenium import webdriver
import unittest, time

class orderDeliverConfirm_sta(MyTest):
    url = "https://admin.codoon.com/admin/html/inventory/order-deliver-confirm.html"
    driver = brower()
    driver.maximize_window()
    
    def setUp(self):
        self.verificationErrors = []
        
    def test_001(self):
        """
                        三方商户
                        商品ID搜索，批量订单确认
        """
        loginPage(self.driver).login("admin","admin",self.url)
        po = orderDeliverConfirmPage(self.driver)
        po.goodsIdOfSearchInput(128612251941052592252053)
        po.searchButton()
        po.batchConfirmButton()
        po.confirmOfBatchButton()
        
        insert_img(self.driver, "orderDeliverConfirm_test_001.jpg")
        
        try: self.assertIn(u"成功",po.getTipText())
        except AssertionError as e: self.verificationErrors.append("001")
    
    def test_002(self):
        """
                        三方商户
                        订单ID搜索，单独订单确认
        """
        loginPage(self.driver).login("admin","admin",self.url)
        po = orderDeliverConfirmPage(self.driver)
        po.orderIdOfSearchInput(70567080541321359850778)
        po.searchButton()
        po.singleConfirmButton()
        
        insert_img(self.driver, "orderDeliverConfirm_test_002.jpg")
        
        try: self.assertEqual(po.getsingleConfirmText(),u"发货")
        except AssertionError as e: self.verificationErrors.append("002")
        
    def test_003(self):
        """
                        自营商户管理员
                        商品ID搜索，批量订单确认
        """
        loginPage(self.driver).login("test123","Test123456",self.url)
        po = orderDeliverConfirmPage(self.driver)
        po.goodsIdOfSearchInput(313590003338741910685126)
        po.searchButton()
        po.batchConfirmButton()
        po.confirmOfBatchButton()
        
        insert_img(self.driver, "orderDeliverConfirm_test_003.jpg")
        
        try: self.assertIn(u"成功",po.getTipText())
        except AssertionError as e: self.verificationErrors.append("003")
    
    def test_004(self):
        """
                        自营商户管理员
                        订单ID搜索，单独订单确认
        """
        loginPage(self.driver).login("test123","Test123456",self.url)
        po = orderDeliverConfirmPage(self.driver)
        po.orderIdOfSearchInput(24763581041160048618610)
        po.searchButton()
        po.singleConfirmButton()
        
        insert_img(self.driver, "orderDeliverConfirm_test_004.jpg")
        
        try: self.assertEqual(po.getsingleConfirmText(),u"发货")
        except AssertionError as e: self.verificationErrors.append("004")
        
        
    
    def tearDown(self):
        time.sleep(2)
        page = Page(self.driver)
        page.logout()
        self.assertEqual([], self.verificationErrors)
        
if __name__ == "__main__":
#     unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(orderDeliverConfirm_sta("test_002"))
    runner = unittest.TextTestRunner()
    runner.run(suite) 