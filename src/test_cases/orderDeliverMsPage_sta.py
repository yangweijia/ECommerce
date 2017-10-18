# -*- coding: utf-8 -*-
'''
Created on 20161019

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
from page_obj.orderDeliverMsPage import orderDeliverMsPage
from selenium import webdriver
import unittest, time

class orderDeliverMs_sta(MyTest):
    url = "https://admin.codoon.com/admin/html/inventory/order-deliver-ms.html"
    driver = brower()
    driver.maximize_window()
    
    def setUp(self):
        self.verificationErrors = []
        
    def test_001(self):
        """
                        三方商户
                        商品ID搜索，批量发货导出
        """
        loginPage(self.driver).login("admin","admin",self.url)
        po = orderDeliverMsPage(self.driver)
        po.goodsIdOfSearchInput(128612251941052592252053)
        po.searchButton()
        po.batchConfirmButton()
        po.exportButton()
        po.confirmOfBatchButton()
        
        insert_img(self.driver, "orderDeliverMs_test_001.jpg")
    
    def test_002(self):
        """
                        三方商户
                        订单ID搜索，单独发货
        """
        loginPage(self.driver).login("admin","admin",self.url)
        po = orderDeliverMsPage(self.driver)
        po.orderIdOfSearchInput(70567080541321359850778)
        po.searchButton()
        po.deliverButton()
        po.numSelect(1)
        po.mailCompanyInput(u"顺丰")
        po.mailCostInput(10)
        po.mailCodeInput("hBSjcxsdjcnxx")
        po.confirmOfDeliverButton()
        
        insert_img(self.driver, "orderDeliverMs_test_002.jpg")
        
        try: self.assertEqual(u"操作成功",po.getTipText())
        except AssertionError as e: self.verificationErrors.append("002")
        
    def test_003(self):
        """
                        自营管理员
                        商品ID搜索，批量发货导出
        """
        loginPage(self.driver).login("test123","Test123456",self.url)
        po = orderDeliverMsPage(self.driver)
        po.goodsIdOfSearchInput(313590003338741910685126)
        po.searchButton()
        po.batchConfirmButton()
        po.exportButton()
        po.confirmOfBatchButton()
        
        insert_img(self.driver, "orderDeliverMs_test_003.jpg")
    
    def test_004(self):
        """
                        自营管理员
                        订单ID搜索，单独发货
        """
        loginPage(self.driver).login("test123","Test123456",self.url)
        po = orderDeliverMsPage(self.driver)
        po.orderIdOfSearchInput(24763581041160048618610)
        po.searchButton()
        po.deliverButton()
        po.numSelect(2)
        po.mailCompanyInput(u"顺丰")
        po.mailCostInput(10)
        po.mailCodeInput("shdcjscj")
        po.confirmOfDeliverButton()
        
        insert_img(self.driver, "orderDeliverMs_test_004.jpg")
        
        try: self.assertEqual(u"操作成功",po.getTipText())
        except AssertionError as e: self.verificationErrors.append("004")
        
    def tearDown(self):
        time.sleep(2)
        page = Page(self.driver)
        page.logout()
        self.assertEqual([], self.verificationErrors)
        
if __name__ == "__main__":
#     unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(orderDeliverMs_sta("test_002"))
    runner = unittest.TextTestRunner()
    runner.run(suite) 
