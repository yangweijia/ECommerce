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
from page_obj.goodsApprovePage import goodsApprovePage
import unittest, time

class goodsApprove_sta(MyTest):
    
    def setUp(self):
        self.driver = brower()
        self.driver.maximize_window() 
        self.verificationErrors = []
        loginPage(self.driver).login("boss_admin","Boss123")
        self.driver.get("https://admin.codoon.com/admin/html/goods-manage/goods-approve.html")
        time.sleep(2)
        
    def test_001(self):
        #通过上架审批       
        po = goodsApprovePage(self.driver)
        po.goodsIdInput("174112077641052592337076")
        po.searchButton()
        po.passButton()
        po.confirmOfPassButton()
        
        insert_img(self.driver, "goodsApprove_sta_001.jpg")
        
        try: self.assertEqual(po.getTip(),u"无更多数据！")
        except AssertionError as e: self.verificationErrors.append("001")
    
    def tearDown(self):
        self.driver.get("https://admin.codoon.com/admin/html/goods-manage/goods-list.html")
        self.assertEqual([], self.verificationErrors)
    
    
           
if __name__ == "__main__":
#     unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(goodsApprove_sta("test_001"))
    runner = unittest.TextTestRunner()
    runner.run(suite)