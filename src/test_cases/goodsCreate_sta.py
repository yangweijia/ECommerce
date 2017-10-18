# -*- coding: utf-8 -*-
import sys
sys.path.append("./models")
sys.path.append("./page_obj")
from selenium import webdriver
from models.myunit import MyTest
from models.star import brower
from models.function import insert_img
from page_obj.loginPage import loginPage
from page_obj.base import Page
from page_obj.goodsManagePage import goodsManagePage
from page_obj.superGoodsManagePage import superGoodsManagePage
import unittest, time

class goodsCreate_sta(MyTest):
    url = "https://admin.codoon.com/admin/html/item-creator-test.html#!new"
    driver = brower()
    driver.maximize_window() 
    
    def setUp(self):
        self.verificationErrors = []
           
    def test_001(self):
        """ 三方商户创建超级商品:
                            有广告词；不限购；有市场价；卡币促销可用；不显示正品保证；可用优惠券；多张图片;有图文详情；有商品二级分类；
                             一级属性；二级属性；要邮寄；邮费为0；支持退货；需结算
                              扣点
        """

        loginPage(self.driver).login("admin","admin",self.url)
        
        driver = self.driver
        
        
        po = goodsManagePage(self.driver)
        po.goodsNameInput(u"超级运动鞋")
        po.goodsDescInput(u"智能连接")
        po.goodsAdvInput(u"广告")
        po.skuDescInput(u"尺码")
        po.limitCountInput("0")
        po.marketPriceInput(99.99)
        po.promoteRulesRadio(True)
        po.showQualityRadio(False)
        po.couponRadio(True)
        po.picUploadButtom(2,"C:\\Users\\yangweijia\\Pictures\\jpg\\9d3f07e61a790d50cc563fd8a28db5762271c535.jpg","C:\\Users\\yangweijia\\Pictures\\jpg\\6630751106351088810.jpg")
        po.detailEdit()
        po.firstClassSelect(u"颜色")
        po.secondClassSelect(u"黑色")
        po.brandInput(u"阿迪达斯")
        js = "window.scrollTo(0,150);"
        driver.execute_script(js)
        po.newAssociateButtom()
         
        
        po.firstAttrNamInput(u"颜色")
        po.firstAttrAdd(u"红色",u"翠绿")
        po.secondAttrNamInput(u"尺码")
        po.secondAttrAdd(u"小",u"大")
        po.postRadio(True)
        po.postPriceInput(0)
        po.refundRadio(True,self.thirdManage)
        po.settleRadio(True,self.thirdManage)
#         driver.get("https://admin.codoon.com/admin/html/item-creator-test.html#!sku_table")
        po.nextSkuConfigButton()
        
        
        po.skuInfoInput(1,2,1,2,1,20,None,True,None,50)
        po.skuInfoBatchButton(1, 2, 1, 2, True)
        po.skuInfoBatchPrice_All()
        po.skuInfoBatchNum_All()
        po.skuInfoBatchRebate_All()
        po.skuInfoBatchConfirm()
        po.ConfirmEndButton()
        
        #验证创建了超级商品
        supGoods = superGoodsManagePage(self.driver)
        print supGoods.getSupGoodsLNameOfEdit()
        try: self.assertEqual(supGoods.getSupGoodsLNameOfEdit(),u"超级运动鞋")
        except AssertionError as e: self.verificationErrors.append(str(e))  
        insert_img(self.driver, "goodsCreate_001.jpg")
    
    def test_002(self):
        """ 三方商户创建超级商品:
                             有广告词；不限购；有市场价；卡币促销可用；不显示正品保证；可用优惠券；多张图片;有图文详情；有商品二级分类；
                             一级属性；二级属性；要邮寄；邮费为0；支持退货；需结算
                             成本
        """

        loginPage(self.driver).login("admin","admin",self.url)
        driver = self.driver
        
        po = goodsManagePage(self.driver)
        po.goodsNameInput(u"超级运动鞋")
        po.goodsDescInput(u"智能连接")
        po.goodsAdvInput(u"广告")
        po.skuDescInput(u"尺码")
        po.limitCountInput("0")
        po.marketPriceInput(99.99)
        po.promoteRulesRadio(True)
        po.showQualityRadio(False)
        po.couponRadio(True)
        po.picUploadButtom(2,"C:\\Users\\yangweijia\\Pictures\\jpg\\9d3f07e61a790d50cc563fd8a28db5762271c535.jpg","C:\\Users\\yangweijia\\Pictures\\jpg\\6630751106351088810.jpg")
        po.detailEdit()
        po.firstClassSelect(u"颜色")
        po.secondClassSelect(u"黑色")
        po.brandInput(u"阿迪达斯")
        js = "window.scrollTo(0,150);                                         "
        driver.execute_script(js)
        po.newAssociateButtom()
        
        
        po.firstAttrNamInput(u"颜色")
        po.firstAttrAdd(u"红色",u"翠绿")
        po.secondAttrNamInput(u"尺码")
        po.secondAttrAdd(u"小",u"大")
        po.postRadio(True)
        po.postPriceInput(0)
        po.refundRadio(True,self.thirdManage)
        po.settleRadio(True,self.thirdManage)
        po.nextSkuConfigButton()
        time.sleep(10)
        
        
        po.skuInfoInput(1,2,1,2,1,1,None,True,0.5,None)
        po.skuInfoBatchButton(1, 2, 1, 2, True)
        po.skuInfoBatchPrice_All()
        po.skuInfoBatchNum_All()
        po.skuInfoBatchRebate_All()
        po.skuInfoBatchConfirm()
        po.ConfirmEndButton()
        
        #验证创建了超级商品
        supGoods = superGoodsManagePage(self.driver)
        print supGoods.getSupGoodsLNameOfEdit()
        try: self.assertEqual(supGoods.getSupGoodsLNameOfEdit(),u"超级运动鞋")
        except AssertionError as e: self.verificationErrors.append(str(e))  
        insert_img(self.driver, "goodsCreate_001.jpg")

    def test_003(self):
        """ 三方商户创建超级商品:
                            有广告词；不限购；有市场价；不能选择卡币促销默认不可用；不显示正品保证；可用优惠券；多张图片;有图文详情；有商品二级分类；
                             一级属性；二级属性；要邮寄；邮费为0；支持退货；需结算
                              扣点
        """

        loginPage(self.driver).login("wy","Aa123456",self.url)
        driver = self.driver
        
        po = goodsManagePage(self.driver)
        po.goodsNameInput(u"超级运动鞋")
        po.goodsDescInput(u"智能连接")
        po.goodsAdvInput(u"广告")
        po.skuDescInput(u"尺码")
        po.limitCountInput("0")
        po.marketPriceInput(99.99)
        po.showQualityRadio(False)
        po.couponRadio(True)
        po.picUploadButtom(2,"C:\\Users\\yangweijia\\Pictures\\jpg\\9d3f07e61a790d50cc563fd8a28db5762271c535.jpg","C:\\Users\\yangweijia\\Pictures\\jpg\\6630751106351088810.jpg")
        po.detailEdit()
        po.firstClassSelect(u"颜色")
        po.secondClassSelect(u"黑色")
        po.brandInput(u"阿迪达斯")
        js = "window.scrollTo(0,150);                                         "
        driver.execute_script(js)
        po.newAssociateButtom()
        
        
        po.firstAttrNamInput(u"颜色")
        po.firstAttrAdd(u"红色",u"翠绿")
        po.secondAttrNamInput(u"尺码")
        po.secondAttrAdd(u"小",u"大")
        po.postRadio(True)
        po.postPriceInput(0)
        po.refundRadio(True,self.thirdManage)
        po.settleRadio(True,self.thirdManage)
        po.nextSkuConfigButton()
        time.sleep(10)
        
        
        po.skuInfoInput(1,2,1,2,1,1,None,True,None,50)
        po.skuInfoBatchButton(1, 2, 1, 2, True)
        po.skuInfoBatchPrice_All()
        po.skuInfoBatchNum_All()
        po.skuInfoBatchRebate_All()
        po.skuInfoBatchConfirm()
        po.ConfirmEndButton()
        
        #验证创建了超级商品
        supGoods = superGoodsManagePage(self.driver)
        print supGoods.getSupGoodsLNameOfEdit()
        try: self.assertEqual(supGoods.getSupGoodsLNameOfEdit(),u"超级运动鞋")
        except AssertionError as e: self.verificationErrors.append(str(e))  
        insert_img(self.driver, "goodsCreate_001.jpg")
   
    def test_004(self):
        """ 三方商户创建超级商品:
                            没广告词；限购数量2；没有市场价；卡币促销不可用；显示正品保证；不可用优惠券；单张图片;没有图文详情；没有商品二级分类
                             一级属性；二级属性；要邮寄；邮费为0；不支持退货；不需结算
        """

        loginPage(self.driver).login("admin","admin",self.url)
        driver = self.driver
        
        po = goodsManagePage(self.driver)
        po.goodsNameInput(u"超级运动鞋")
        po.goodsDescInput(u"智能连接")
        po.skuDescInput(u"尺码")
        po.limitCountInput("2")
        po.marketPriceInput(0)
        po.promoteRulesRadio(False)
        po.showQualityRadio(True)
        po.couponRadio(False)
        po.picUploadButtom(1,"C:\\Users\\yangweijia\\Pictures\\jpg\\9d3f07e61a790d50cc563fd8a28db5762271c535.jpg")
        po.firstClassSelect(u"颜色")
        po.brandInput(u"阿迪达斯")
        js = "window.scrollTo(0,150);                                         "
        driver.execute_script(js)
        po.newAssociateButtom()
        
        
        po.firstAttrNamInput(u"颜色")
        po.firstAttrAdd(u"红色",u"翠绿")
        po.secondAttrNamInput(u"尺码")
        po.secondAttrAdd(u"小",u"大")
        po.postRadio(True)
        po.refundRadio(False,self.thirdManage)
        po.settleRadio(False,self.thirdManage)
        po.nextSkuConfigButton()
        
        
        po.skuInfoInput(1,2,1,2,1,100,None,False,None,None)
        po.skuInfoBatchButton(1, 2, 1, 2, False)
        po.skuInfoBatchPrice_All()
        po.skuInfoBatchNum_All()
        po.skuInfoBatchConfirm(False)
        po.ConfirmEndButton()
        
        #验证创建了超级商品
        supGoods = superGoodsManagePage(self.driver)
        print supGoods.getSupGoodsLNameOfEdit()
        insert_img(self.driver, "goodsCreate_002.jpg")
        try: self.assertEqual(supGoods.getSupGoodsLNameOfEdit(),u"超级运动鞋")
        except AssertionError as e: self.verificationErrors.append("004")  
             
    def test_005(self):
        #三方商户创建普通商品
        loginPage(self.driver).login("admin","admin",self.url)
        driver = self.driver
        
        po = goodsManagePage(self.driver)
        po.goodsNameInput(u"杨韦佳专用秒杀1名称普通运动鞋的商品名称普通运动鞋的商品名称普通运动鞋的商品名称")
        po.goodsDescInput(u"商品描述呀商品描述呀商品描述呀商品描述呀")
        po.goodsAdvInput(u"广告词广告词广告词广告词广告词广告词广告词广告词广告词广告词")
        po.skuDescInput(u"颜色颜色颜色颜")
        po.limitCountInput("0")
        po.marketPriceInput(999999.99)
        po.promoteRulesRadio(True)
        po.showQualityRadio(False)
        po.couponRadio(True)
        po.picUploadButtom(2,"C:\\Users\\yangweijia\\Pictures\\jpg\\9d3f07e61a790d50cc563fd8a28db5762271c535.jpg","C:\\Users\\yangweijia\\Pictures\\jpg\\6630751106351088810.jpg")
        po.detailEdit()
        po.firstClassSelect(u"颜色")
        po.secondClassSelect(u"黑色")
        po.brandInput(u"阿迪达斯")
        js = "window.scrollTo(0,150);"
        driver.execute_script(js)
        time.sleep(2)
        po.newAssociateButtom()
        
        
        po.firstAttrNamInput(u"颜色颜色颜色颜")
        po.firstAttrAdd(u"红色红色红色红色红色红色红色红色红色",u"翠绿翠绿翠绿翠绿翠绿翠绿翠绿翠绿翠绿")
        po.postRadio(True)
        po.postPriceInput(0)
        po.refundRadio(True,self.thirdManage)
        po.settleRadio(True,self.thirdManage)
        po.nextSkuConfigButton()
        
        po.skuInfoInput(1,2,0,0,1,50,None,True,0.5,None)
        po.skuInfoInput(2,2,0,0,1.5,25,None,True,0.5,None)
        po.ConfirmEndButton()
        
        #验证创建了商品
        try: self.assertEqual(po.getGoodsLNameOfEdit(),u"普通运动鞋的商品名称普通运动鞋的商品名称普通运动鞋的商品名称普通运动鞋的商品名称")
        except AssertionError as e: self.verificationErrors.append(str(e))  
        insert_img(self.driver, "goodsCreate_002.jpg")

    def test_006(self):
        #自营管理员创建超级商品   
        loginPage(self.driver).login("zdh11","Aa123456",self.url)
        driver = self.driver
        
        po = goodsManagePage(self.driver)
        po.goodsNameInput(u"超级运动鞋")
        po.goodsDescInput(u"智能连接")
        po.goodsAdvInput(u"广告")
        po.skuDescInput(u"尺码")
        po.limitCountInput("0")
        po.marketPriceInput(99.99)
        po.promoteRulesRadio(True)
        po.showQualityRadio(False)
        po.couponRadio(True)
        po.picUploadButtom(2,"C:\\Users\\yangweijia\\Pictures\\jpg\\9d3f07e61a790d50cc563fd8a28db5762271c535.jpg","C:\\Users\\yangweijia\\Pictures\\jpg\\6630751106351088810.jpg")
        po.detailEdit()
        po.firstClassSelect(u"颜色")
        po.secondClassSelect(u"黑色")
        po.brandInput(u"阿迪达斯")
        js = "window.scrollTo(0,150);                                         "
        driver.execute_script(js)
        time.sleep(2)
        po.newAssociateButtom()
        driver.get("https://admin.codoon.com/admin/html/item-creator-test.html#!sku_config")
        time.sleep(2)
        po.firstAttrNamInput(u"颜色")
        po.firstAttrAdd(u"红色",u"翠绿")
        po.secondAttrNamInput(u"尺码")
        po.secondAttrAdd(u"小",u"大")
        po.postRadio(True)
        po.postPriceInput(0)
        po.vendorSelect(u"自营国内")
        po.refundRadio(True,self.thirdManage)
        po.settleRadio(True,self.thirdManage)
        po.nextSkuConfigButton()
        time.sleep(5)
        po.skuInfoInput(1,2,1,2,1,1,None,True,None,50)
        po.skuInfoBatchButton(1, 2, 1, 2, True)
        po.skuInfoBatchPrice_All()
        po.skuInfoBatchNum_All()
        po.skuInfoBatchRebate_All()
        po.skuInfoBatchConfirm()
        po.ConfirmEndButton()
         
        #验证创建了超级商品
        supGoods = superGoodsManagePage(self.driver)
        print supGoods.getSupGoodsLNameOfEdit()
        try: self.assertEqual(supGoods.getSupGoodsLNameOfEdit(),u"超级运动鞋")
        except AssertionError as e: self.verificationErrors.append("006")  
        insert_img(self.driver, "goodsCreate_006.jpg")        
    
    def tearDown(self):
        page = Page(self.driver)
        page.logout()
        self.assertEqual([], self.verificationErrors)
    
           
if __name__ == "__main__":
#    unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(goodsCreate_sta("test_001"))
      
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
  
    
    