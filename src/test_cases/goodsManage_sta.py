# -*- coding: utf-8 -*-
import sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models.myunit import MyTest
from models.star import brower
from models.function import insert_img
from page_obj.loginPage import loginPage
from page_obj.goodsManagePage import goodsManagePage
import unittest, time

class goodsManage_sta(MyTest):
    
    def setUp(self):
        self.driver = brower()
        self.driver.maximize_window() 
        self.verificationErrors = []
        loginPage(self.driver).login("admin","admin")
        self.driver.get("https://admin.codoon.com/admin/html/goods-manage/goods-list.html")
        time.sleep(2)
        
    def test_001(self):
        #按照商品ID搜索       
        po = goodsManagePage(self.driver)
        po.goodsIdInput("348149106539324941323825")
        po.searchButton()
        insert_img(self.driver, "goodsCreate_test_002.jpg")
        try: self.assertEqual(po.getGoodsInfoId(),"348149106539324941323825")
        except AssertionError as e: self.verificationErrors.append(str(e)+"goodsCreate_test_002")  
    
    def test_002(self):
        #按照商品长名称搜索
        po = goodsManagePage(self.driver)
        po.goodsLNameInput("1")
        po.searchButton()
        insert_img(self.driver, "goodsCreate_test_003.jpg")
        try: self.assertEqual(po.getGoodsInfoLName(),"1")
        except AssertionError as e: self.verificationErrors.append(str(e)+"goodsCreate_test_003")
    
    def test_003(self):
        #自营管理员上架
        po = goodsManagePage(self.driver)
        po.goodsIdInput("351668442518935724202665")
        po.searchButton()
        po.upButton()
        po.upEnsureButton()
        
        insert_img(self.driver, "goodsManage_test_003.jpg")
        print po.upSecText()
        try: self.assertEqual(po.upSecText(),u"上架成功")
        except AssertionError as e: self.verificationErrors.append(str(e))
    
    def test_004(self):
        #三方商户提交审核
        po = goodsManagePage(self.driver)
        po.goodsIdInput("128612251941052592252053")
        po.searchButton()
        po.submitButton()
        po.upEnsureButton()
        
        insert_img(self.driver, "goodsManage_test_004.jpg")
        print po.upSecText()
        try: self.assertEqual(po.upSecText(),u"审核提交成功，请耐心等待")
        except AssertionError as e: self.verificationErrors.append(str(e))
        
        
        
        
           
    
    def tearDown(self):
        self.driver.get("https://admin.codoon.com/admin/html/goods-manage/goods-list.html")
        self.assertEqual([], self.verificationErrors)
    
           
if __name__ == "__main__":
#     unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(goodsManage_sta("test_004"))
    runner = unittest.TextTestRunner()
    runner.run(suite)
  
    
    