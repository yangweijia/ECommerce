# -*- coding: utf-8 -*-
'''
Created on 20161011

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
from page_obj.superGoodsManagePage import superGoodsManagePage
import unittest, time

class superGoodsManage_sta(MyTest):
    url = "https://admin.codoon.com/admin/html/goods-manage/superitem-ms.html"
    driver = brower()
    driver.maximize_window()
    
    def setUp(self):
        self.verificationErrors = []
        
    def test_001(self):
        #超级商品生效（三方Boss）
        loginPage(self.driver).login("boss_admin","Boss123",self.url)
            
        po = superGoodsManagePage(self.driver)
        po.searContInput("299500516141052592407075")

        po.searchButton("thirdBoss")
        po.effectButton()
         
        insert_img(self.driver, "superGoodsManage_001.jpg")
         
        try: self.assertEqual(po.geteffectText(),u"失效")
        except AssertionError as e: self.verificationErrors.append("001")
    
    def test_002(self):
        #超级商品生效（小Boss）  
        loginPage(self.driver).login("ywjBoss1","1234",self.url)
        
        po = superGoodsManagePage(self.driver)
        po.searContInput("379873516136836933038241")
        po.searchButton("subThirdBoss")
        po.effectButton()
         
        insert_img(self.driver, "superGoodsManage_002.jpg")
         
        try: self.assertEqual(po.geteffectText(),u"失效")
        except AssertionError as e: self.verificationErrors.append("002")
    
    def test_003(self):
        #超级商品生效（三方商户）      
        loginPage(self.driver).login("wy","Aa123456",self.url)
        
        po = superGoodsManagePage(self.driver)
        po.searContInput("298372840340646020969458")
        po.searchButton("thirdManage")
        po.effectButton()
         
        insert_img(self.driver, "superGoodsManage_003.jpg")
         
        try: self.assertEqual(po.geteffectText(),u"失效")
        except AssertionError as e: self.verificationErrors.append("003")
        
    def test_004(self):
        #超级商品生效（自营管理员）
        loginPage(self.driver).login("test123","Test123456",self.url)
              
        po = superGoodsManagePage(self.driver)
        po.searContInput("183345641538749679397800")
        po.searchButton("selfManage")
        po.effectButton()
         
         
        insert_img(self.driver, "superGoodsManage_004.jpg")
         
        try: self.assertEqual(po.geteffectText(),u"失效")
        except AssertionError as e: self.verificationErrors.append("004")
     
    def test_005(self):
        #超级商品失效（三方Boss）      
        loginPage(self.driver).login("boss_admin","Boss123",self.url)
        
        po = superGoodsManagePage(self.driver)
        po.searContInput("49649967439324941423407")
        po.searchButton("thirdBoss")
        po.effectButton()
        po.confirmOfEffect()
         
        insert_img(self.driver, "superGoodsManage_005.jpg")
         
        try: self.assertEqual(po.geteffectText(),u"生效")
        except AssertionError as e: self.verificationErrors.append("005")
     
    def test_006(self):
        #超级商品失效（小Boss）    
        loginPage(self.driver).login("ywjBoss1","1234",self.url)
          
        po = superGoodsManagePage(self.driver)
        po.searContInput("379873516136836933038241")
        po.searchButton("subThirdBoss")
        po.effectButton()
        po.confirmOfEffect()
         
        insert_img(self.driver, "superGoodsManage_006.jpg")
         
        try: self.assertEqual(po.geteffectText(),u"生效")
        except AssertionError as e: self.verificationErrors.append("006")
     
    def test_007(self):
        #超级商品失效（三方商户）      
        loginPage(self.driver).login("admin","admin",self.url)
        
        po = superGoodsManagePage(self.driver)
        po.searContInput("15471920739324406367534")
        po.searchButton("thirdManage")
        po.effectButton()
        po.confirmOfEffect()
         
        insert_img(self.driver, "superGoodsManage_007.jpg")
         
        try: self.assertEqual(po.geteffectText(),u"生效")
        except AssertionError as e: self.verificationErrors.append("007")
     
    def test_008(self):
        #超级商品失效（自营管理员）   
        loginPage(self.driver).login("test123","Test123456",self.url)
           
        po = superGoodsManagePage(self.driver)
        po.searContInput("183345641538749679397800")
        po.searchButton("selfManage")
        po.effectButton()
        po.confirmOfEffect()
         
        insert_img(self.driver, "superGoodsManage_008.jpg")
         
        try: self.assertEqual(po.geteffectText(),u"生效")
        except AssertionError as e: self.verificationErrors.append("008")
        
    def tearDown(self):
        page = Page(self.driver)
        page.logout()
        self.assertEqual([], self.verificationErrors)
    
           
if __name__ == "__main__":
#     unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(superGoodsManage_sta("test_001"))
    runner = unittest.TextTestRunner()
    runner.run(suite) 