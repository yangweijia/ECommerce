# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import unittest, time, datetime, re,sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models.myunit import MyTest
from page_obj.loginPage import loginPage
from page_obj.Table import Table
from models.driver import brower
from page_obj.BasicOperation import BasicOperation


class SkuThirdParty(MyTest):


    
    #SKU长名称 SKU短名称 SKU邮寄类型 SKU单价 邮费 SKU属性 是否支持退货 三方商家SKU编号#   
    def new_sku_one(self,longName,shortName,mailType,price,mailCost,**skuAttribute):       
        driver = self.driver
        driver.find_element_by_xpath("//a[contains(@href, 'https://admin.codoon.com/admin/html/goods-manage/goods-manage.html')]").click()
        driver.implicitly_wait(10)

        driver.find_element_by_xpath("//div[2]/a[2]/span").click()
        
        driver.implicitly_wait(10)
        driver.find_element_by_css_selector("a.pcommon-setting-margin.new-sku > button.btn.btn-success").click()
        time.sleep(1)
        #SKU长名称
        driver.find_element_by_css_selector("textarea.base-unit.pgoods-setting-long-name").clear()
        driver.find_element_by_css_selector("textarea.base-unit.pgoods-setting-long-name").send_keys(longName)
        #SKU短名称
        driver.find_element_by_css_selector("textarea.base-unit.pgoods-setting-short-name").clear()
        driver.find_element_by_css_selector("textarea.base-unit.pgoods-setting-short-name").send_keys(shortName)
        #SKU邮寄类型
        if mailType == True:
            pass
        else:
            driver.find_element_by_xpath("//input[2]").click()
        #SKU单价   
        driver.find_element_by_css_selector("input.unit_price.base-unit").clear()
        driver.find_element_by_css_selector("input.unit_price.base-unit").send_keys(price)
        #邮费
        driver.find_element_by_css_selector("input.mail_fee.base-unit").clear()
        driver.find_element_by_css_selector("input.mail_fee.base-unit").send_keys(mailCost)
        #属性
        for name, address in skuAttribute.items():
            driver.find_element_by_xpath("//button").click()
            driver.find_element_by_name("attr").clear()
            driver.find_element_by_name("attr").send_keys(name)
            time.sleep(2)
             
            driver.find_element_by_name("desc").clear()
            driver.find_element_by_name("desc").send_keys(address)
            time.sleep(2)
            driver.find_element_by_xpath("//button[@type='button']").click()
            time.sleep(2)
    #是否支持退货 三方商家SKU编号
    def new_sku_two(self,refundType,thirdSku):
        driver = self.driver
 
        #是否支持退货
        if refundType == True:
            pass
        else:
            driver.find_element_by_xpath("/html/body/div[1]/div/input[6]").click()
        #三方商家SKU编号
        if thirdSku == None:
            pass
        else:
            driver.find_element_by_name("third_party_sku").clear()
            driver.find_element_by_name("third_party_sku").send_keys(thirdSku)
            time.sleep(1)
         
        driver.find_element_by_xpath("//div[11]/button").click()
        time.sleep(2)

    def thirdUser_checkGoods(self):
        """第三方商户新建sku sku入库 新建商品 增加商品上架数量 提交审核"""
        driver = self.driver
        #新建sku
        self.thirdUser_sku()
        #获取新建SKU的ID
        time.sleep(4)
        skuId = self.skuTable.table_cell(1,4)
        skulist = [skuId]        
        #入库
        Basis.stock_sku(self, True, skuId, 500)
        time.sleep(3)       
        #新增商品 绑定sku
        Basis.new_sku(self,u"水果柠檬酸水果柠檬酸水果柠檬酸水果柠檬酸水果柠檬酸水果柠檬酸水果柠檬酸水果柠檬酸", u"柠檬酸酸酸柠檬酸酸酸柠檬酸酸酸柠檬酸酸酸", 1, 0.02, True, u"颜色", "C:\\Users\\yangweijia\\Pictures\\jpg\\6619393151235890154.jpg", False,*skulist)
        time.sleep(3)
        goods_id = self.goodsTable.table_cell(1, 8)
        #补充加上数量
        Basis.add_list_num(self, goods_id, 200)
        time.sleep(2)       
        #提交审核
        driver.find_element_by_xpath("//td[11]/button").click()
        time.sleep(1)
        driver.find_element_by_id("up-ensure").click()
        time.sleep(4)
        #编辑sku
        driver.find_element_by_xpath("/html/body/div[5]/div[2]/a[2]/span").click()
        time.sleep(2)
        driver.find_element_by_id("sku_id").send_keys(skuId)
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/button").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/div/table/tbody/tr[2]/td[12]/a[1]/button").click()
        time.sleep(2)

        

    """身份：第三方商户"""
    #增加sku    
    def test_001(self):
        """三方商户管理员:最长长名称+最长短名称+要邮寄+非0单价+非0邮费+多个SKU属性+支持退货+存在三方商家SKU编号"""
        loginPage(self.driver).login("admin","admin")
        driver = self.driver
    
        sku_attribute = {       u'颜色'   : u'蓝色',
                                u'尺寸'   : u'38'}
        self.new_sku_one(u"即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬",u"柠檬柠檬柠檬柠檬柠檬柠檬柠檬柠檬柠檬柠檬",True,0.01,0.01,**sku_attribute) 
        self.new_sku_two(True, "001001001001001001001") 
        
        time.sleep(2)
        skuTable = Table(self.driver,"/html/body/div[1]/div/table/tbody",2)
        #SKU类型
        try: self.assertEqual(skuTable.table_cell(1, 1), u"要邮寄")
        except AssertionError as e: self.verificationErrors.append(str(e)+"1.1")
        #库存状态
        try: self.assertEqual(skuTable.table_cell(1,2), u"无货")
        except AssertionError as e: self.verificationErrors.append(str(e)+"1.2")
        #长名称
        try: self.assertEqual(skuTable.table_cell(1,5), u"即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬")
        except AssertionError as e: self.verificationErrors.append(str(e)+"1.3")
        #短名称
        try: self.assertEqual(skuTable.table_cell(1,6), u"柠檬柠檬柠檬柠檬柠檬柠檬柠檬柠檬柠檬柠檬")
        except AssertionError as e: self.verificationErrors.append(str(e)+"1.4")
        #库存数量
        try: self.assertEqual(skuTable.table_cell(1,7), u"0")
        except AssertionError as e: self.verificationErrors.append(str(e)+"1.5")
        #邮费
        try: self.assertEqual(skuTable.table_cell(1,8), u"￥0.01")
        except AssertionError as e: self.verificationErrors.append(str(e)+"1.6")
        #单价
        try: self.assertEqual(skuTable.table_cell(1,9), u"￥0.01")
        except AssertionError as e: self.verificationErrors.append(str(e)+"1.7")       
        #SKU属性
        try: self.assertEqual(skuTable.table_cell(1,10), u"颜色:蓝色;尺寸:38")
        except AssertionError as e: self.verificationErrors.append(str(e)+"1.8")
        #三方商家SKU编号
        try: self.assertEqual(skuTable.table_cell(1,11), "001001001001001001001")
        except AssertionError as e: self.verificationErrors.append(str(e)+"1.9")
        #是否支持退货 
        time.sleep(2)                                                              
        driver.find_element_by_xpath("/html/body/div[1]/div/table/tbody/tr[2]/td[12]/a[1]/button").click()
        time.sleep(2)
        try: self.assertNotEqual(self.driver.find_element_by_xpath("/html/body/div[1]/div/input[5]").get_attribute("checked"), None)
        except AssertionError as e: self.verificationErrors.append(str(e)+"2.0")
     
    def test_002(self):
        """三方商户管理员:不要邮寄+0邮费+单个SKU属性+不支持退货+不存在三方商家SKU编号"""
        loginPage(self.driver).login("weiyun","Weiyun0206")
        driver = self.driver
        sku_attribute = { u'color' : u'red'}
        self.new_sku_one(u"123Google鲜花",u"123Google",False,100.01,0.00,**sku_attribute) 
        self.new_sku_two(False,None) 
        
        time.sleep(2)
        skuTable = Table(self.driver,"/html/body/div[1]/div/table/tbody",2)
        #SKU类型
        try: self.assertEqual(skuTable.table_cell(1,1), u"不邮寄")
        except AssertionError as e: self.verificationErrors.append(str(e)+"2.1")
        #邮费
        try: self.assertEqual(skuTable.table_cell(1,8), u"￥0.00")
        except AssertionError as e: self.verificationErrors.append(str(e)+"2.2")
        #SKU属性
        try: self.assertEqual(skuTable.table_cell(1,10), u"color:red")
        except AssertionError as e: self.verificationErrors.append(str(e)+"2.3")
        #不存在三方商家SKU编号
        try: self.assertEqual(skuTable.table_cell(1,11), u"")
        except AssertionError as e: self.verificationErrors.append(str(e)+"2.4")
        #是否支持退货 
        time.sleep(2)                                                              
        driver.find_element_by_xpath("/html/body/div[1]/div/table/tbody/tr[2]/td[12]/a[1]/button").click()
        time.sleep(2)
        try: self.assertEqual(self.driver.find_element_by_xpath("/html/body/div[1]/div/input[5]").get_attribute("checked"), None)
        except AssertionError as e: self.verificationErrors.append(str(e)+"2.4")             
     
    #编辑SKU：SKU未绑定商品
    def test_003(self):
        """第三方商户 SKU未绑定商品 
           SKU长名称                                                不可编辑
           SKU短名称                                                不可编辑
                                 邮寄类型                                                     不可编辑
                                 单价                                                             可以编辑
                                 邮费                                                             可以编辑
           SKU属性增加、删除                                不可编辑
                                是否支持退货                                              可以编辑
                                三方商家SKU编号                                     可以编辑
           SKU库存数量                                            可以编辑                     
        """
        loginPage(self.driver).login("weiyun","Weiyun0206")
        driver = self.driver
        
        sku_attribute = {       u'颜色'   : u'蓝色',
                                u'尺寸'   : u'38'}
        self.new_sku_one(u"即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬",u"柠檬柠檬柠檬柠檬柠檬柠檬柠檬柠檬柠檬柠檬",True,0.01,0.01,**sku_attribute) 
        self.new_sku_two(True, "001001001001001001001") 
        skuTable = Table(self.driver,"/html/body/div[1]/div/table/tbody",2)
        #进入编辑
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/table/tbody/tr[2]/td[12]/a[1]/button").click()
        time.sleep(2)
        #SKU长名称：不可编辑
        try: self.assertEqual(driver.find_element_by_css_selector("textarea.base-unit.pgoods-setting-long-name").get_attribute("disabled"), u"true")
        except AssertionError as e: self.verificationErrors.append(str(e)+"3.1")
        #SKU短名称：不可编辑
        try: self.assertEqual(driver.find_element_by_css_selector("textarea.base-unit.pgoods-setting-short-name").get_attribute("disabled"), u"true")
        except AssertionError as e: self.verificationErrors.append(str(e)+"4.1")
        #邮寄类型：不可编辑
        try: self.assertEqual(driver.find_element_by_xpath("//input").get_attribute("disabled"), u"true")
        except AssertionError as e: self.verificationErrors.append(str(e)+"4.1")
        try: self.assertEqual(driver.find_element_by_xpath("//input[2]").get_attribute("disabled"), u"true")
        except AssertionError as e: self.verificationErrors.append(str(e)+"4.2")
        #单价：可以编辑
        #改变单价
        oldPrice = float(driver.find_element_by_css_selector("input.unit_price.base-unit").get_attribute("value"))
        newPrice = oldPrice + 1.00
        driver.find_element_by_css_selector("input.unit_price.base-unit").clear()
        driver.find_element_by_css_selector("input.unit_price.base-unit").send_keys(newPrice)
        time.sleep(1)
        #邮费：可以编辑
        #改变邮费
        oldMailCost = float(driver.find_element_by_css_selector("input.mail_fee.base-unit").get_attribute("value"))
        newMailCost = oldMailCost + 1.00
        driver.find_element_by_css_selector("input.mail_fee.base-unit").clear()
        driver.find_element_by_css_selector("input.mail_fee.base-unit").send_keys(newMailCost)
        time.sleep(1)
        #SKU属性：不可编辑
        try: self.assertEqual(driver.find_element_by_xpath("//button").get_attribute("disabled"), u"true")
        except AssertionError as e: self.verificationErrors.append(str(e)+"9.1")
        #sku属性：不可删除
        oldskuAttributeOne = driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[1]").text
        driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[1]").click()
         
        try: self.assertEqual(driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[1]").text, oldskuAttributeOne)
        except AssertionError as e: self.verificationErrors.append(str(e)+"10.1")
         
        oldskuAttributeTwo = driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[2]").text
        driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[2]").click()
         
        try: self.assertEqual(driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[2]").text, oldskuAttributeTwo)
        except AssertionError as e: self.verificationErrors.append(str(e)+"10.2")
        #退货：可以编辑
        #变为不退货
        driver.find_element_by_xpath("/html/body/div[1]/div/input[6]").click()
        time.sleep(1)
        #三方商家SKU编号：可以编辑
        driver.find_element_by_name("third_party_sku").clear()
        driver.find_element_by_name("third_party_sku").send_keys("003003")
        time.sleep(1)
        #保存
        driver.find_element_by_xpath("//div[11]/button").click()
        time.sleep(4)
        #验证新的单价
        try: self.assertEqual(skuTable.table_cell(1,9), u"￥1.01")
        except AssertionError as e: self.verificationErrors.append(str(e)+"6.1")
        #验证新的邮费
        try: self.assertEqual(skuTable.table_cell(1,8), u"￥1.01")
        except AssertionError as e: self.verificationErrors.append(str(e)+"7.1")
        #验证三方商家sku编号
        try: self.assertEqual(skuTable.table_cell(1,11), "003003")
        except AssertionError as e: self.verificationErrors.append(str(e)+"12.1")              
        #进入编辑
        driver.find_element_by_xpath("//td[12]/a/button").click()
        time.sleep(2)
        #退货
        try: self.assertEqual(driver.find_element_by_xpath("/html/body/div[1]/div/input[5]").get_attribute("checked"), None)
        except AssertionError as e: self.verificationErrors.append(str(e)+"11.1")
         
    def test_004(self):
        """第三方商户 SKU未绑定商品 
                                 邮费                   可以编辑为0
        """
        loginPage(self.driver).login("weiyun","Weiyun0206")
        driver = self.driver
         
        sku_attribute = {       u'颜色'   : u'蓝色',
                                u'尺寸'   : u'38'}
        self.new_sku_one(u"即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬",u"柠檬柠檬柠檬柠檬柠檬柠檬柠檬柠檬柠檬柠檬",True,0.01,0.01,**sku_attribute) 
        self.new_sku_two(True, "001001001001001001001") 
        skuTable = Table(self.driver,"/html/body/div[1]/div/table/tbody",2)
        #进入编辑
        time.sleep(3)
        driver.find_element_by_xpath("//td[12]/a/button").click()
        time.sleep(2)
        #SKU邮费
        driver.find_element_by_css_selector("input.mail_fee.base-unit").clear()
        driver.find_element_by_css_selector("input.mail_fee.base-unit").send_keys(u"0.00")
        time.sleep(1)
        #保存
        driver.find_element_by_xpath("//div[11]/button").click()
        time.sleep(2)
        #验证新的邮费
        try: self.assertEqual(skuTable.table_cell(1,8), u"￥0.00")
        except AssertionError as e: self.verificationErrors.append(str(e)+"8.1")    
       
    def test_005(self):
        """第三方商户 SKU未绑定商品 
           SKU库存数量        可以编辑
        """
        loginPage(self.driver).login("weiyun","Weiyun0206")
        driver = self.driver
         
        sku_attribute = {       u'颜色'   : u'蓝色',
                                u'尺寸'   : u'38'}
        self.new_sku_one(u"即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬",u"柠檬柠檬柠檬柠檬柠檬柠檬柠檬柠檬柠檬柠檬",True,0.01,0.01,**sku_attribute) 
        self.new_sku_two(True, "001001001001001001001") 
        #库存管理
        time.sleep(2)
        driver.find_element_by_xpath("//a[2]/span").click()
        time.sleep(4)
        #要邮寄SKU库存
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/a[1]/span").click()
        time.sleep(4)
        #入库
        driver.find_element_by_xpath("//td[12]/button").click()
        time.sleep(1)
        driver.find_element_by_name("num").clear()
        driver.find_element_by_name("num").send_keys("500")
        time.sleep(1)
        driver.find_element_by_xpath("//button[@type='button']").click()
        time.sleep(3)
        #商品管理
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[2]/div[3]/a[3]/span").click()
        time.sleep(3)
        #SKU管理
        driver.find_element_by_css_selector("a.sku_ms > span").click()
        time.sleep(3)
        #进入编辑
        driver.find_element_by_xpath("//td[12]/a/button").click()
        time.sleep(3)
        try: self.assertEqual("500", driver.find_element_by_xpath("//div[10]/div").text)
        except AssertionError as e: self.verificationErrors.append(str(e)+"13.1")
     
    #编辑SKU：绑定商品从未上架
    def test_006(self):
        """第三方商户 绑定商品从未上架 
           SKU长名称                                                不可编辑
           SKU短名称                                                不可编辑
                                 邮寄类型                                                     不可编辑
                                 单价                                                             可以编辑
                                 邮费                                                             可以编辑
           SKU属性增加、删除                                不可编辑
                                是否支持退货                                              可以编辑
                                三方商家SKU编号                                     可以编辑
           SKU库存数量                                            可以编辑                     
        """
        loginPage(self.driver).login("weiyun","Weiyun0206")
        driver = self.driver
         
        sku_attribute = {       u'颜色'   : u'蓝色',
                                u'尺寸'   : u'38'}
        self.new_sku_one(u"即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬",u"柠檬柠檬柠檬柠檬柠檬柠檬柠檬柠檬柠檬柠檬",True,0.01,0.01,**sku_attribute) 
        self.new_sku_two(True, "001001001001001001001") 
        skuTable = Table(self.driver,"/html/body/div[1]/div/table/tbody",2)
        #获取新建SKU的ID
        skuId = skuTable.table_cell(1,4)
        time.sleep(5)
        #SKU绑定草稿商品
        #商品管理
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//div[2]/a").click()
        #driver.find_element_by_css_selector("a.item_ms. > span").click()
        time.sleep(1)
        #选择草稿
        Select(driver.find_element_by_id("state")).select_by_visible_text(u"草稿")
        time.sleep(2)
        #点击编辑
        driver.find_element_by_xpath("/html/body/div[1]/div/table/tbody/tr[1]/td[11]/a[1]/button").click()
        time.sleep(2)
        #新增关联sku
        driver.find_element_by_xpath("//button").click()
        time.sleep(2)
        driver.find_element_by_name("sku_id").clear()
        driver.find_element_by_name("sku_id").send_keys(skuId)
        time.sleep(2)
        driver.find_element_by_xpath("//button[@type='button']").click() 
        time.sleep(2)   
        driver.find_element_by_xpath("//div[12]/button").click()
        time.sleep(4)
        #进入SKU管理                                                           
        driver.find_element_by_xpath("//div[2]/a[2]/span").click()
        time.sleep(3)
        driver.find_element_by_id("sku_id").send_keys(skuId)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/button").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/table/tbody/tr[2]/td[12]/a[1]/button").click()
        time.sleep(2)
        #SKU长名称：不可编辑
        try: self.assertEqual(driver.find_element_by_css_selector("textarea.base-unit.pgoods-setting-long-name").get_attribute("disabled"), u"true")
        except AssertionError as e: self.verificationErrors.append(str(e)+"3.1")
        #SKU短名称：不可编辑
        try: self.assertEqual(driver.find_element_by_css_selector("textarea.base-unit.pgoods-setting-short-name").get_attribute("disabled"), u"true")
        except AssertionError as e: self.verificationErrors.append(str(e)+"4.1")
        #邮寄类型：不可编辑
        try: self.assertEqual(driver.find_element_by_xpath("//input").get_attribute("disabled"), u"true")
        except AssertionError as e: self.verificationErrors.append(str(e)+"4.1")
        try: self.assertEqual(driver.find_element_by_xpath("//input[2]").get_attribute("disabled"), u"true")
        except AssertionError as e: self.verificationErrors.append(str(e)+"4.2")
        #单价：可以编辑
        #改变单价
        oldPrice = float(driver.find_element_by_css_selector("input.unit_price.base-unit").get_attribute("value"))
        newPrice = oldPrice + 1.00
        driver.find_element_by_css_selector("input.unit_price.base-unit").clear()
        driver.find_element_by_css_selector("input.unit_price.base-unit").send_keys(newPrice)
        time.sleep(1)
        #邮费：可以编辑
        #改变邮费
        oldMailCost = float(driver.find_element_by_css_selector("input.mail_fee.base-unit").get_attribute("value"))
        newMailCost = oldMailCost + 1.00
        driver.find_element_by_css_selector("input.mail_fee.base-unit").clear()
        driver.find_element_by_css_selector("input.mail_fee.base-unit").send_keys(newMailCost)
        time.sleep(1)
        #SKU属性：不可编辑
        try: self.assertEqual(driver.find_element_by_xpath("//button").get_attribute("disabled"), u"true")
        except AssertionError as e: self.verificationErrors.append(str(e)+"9.1")
        #sku属性：不可删除
        oldskuAttributeOne = driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[1]").text
        driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[1]").click()
         
        try: self.assertEqual(driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[1]").text, oldskuAttributeOne)
        except AssertionError as e: self.verificationErrors.append(str(e)+"10.1")
         
        oldskuAttributeTwo = driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[2]").text
        driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[2]").click()
         
        try: self.assertEqual(driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[2]").text, oldskuAttributeTwo)
        except AssertionError as e: self.verificationErrors.append(str(e)+"10.2")
        #退货：可以编辑
        #变为不退货
        driver.find_element_by_xpath("/html/body/div[1]/div/input[6]").click()
        time.sleep(1)
        #三方商家SKU编号：可以编辑
        driver.find_element_by_name("third_party_sku").clear()
        driver.find_element_by_name("third_party_sku").send_keys("003003")
        time.sleep(1)
        #保存
        driver.find_element_by_xpath("//div[11]/button").click()
        time.sleep(4)
        #验证新的单价
        try: self.assertEqual(skuTable.table_cell(1,9), u"￥1.01")
        except AssertionError as e: self.verificationErrors.append(str(e)+"6.1")
        #验证新的邮费
        try: self.assertEqual(skuTable.table_cell(1,8), u"￥1.01")
        except AssertionError as e: self.verificationErrors.append(str(e)+"7.1")
        #验证三方商家sku编号
        try: self.assertEqual(skuTable.table_cell(1,11), "003003")
        except AssertionError as e: self.verificationErrors.append(str(e)+"12.1")              
        #进入编辑
        driver.find_element_by_xpath("//td[12]/a/button").click()
        time.sleep(2)
        #退货
        try: self.assertEqual(self.driver.find_element_by_xpath("/html/body/div[1]/div/input[5]").get_attribute("checked"), None)
        except AssertionError as e: self.verificationErrors.append(str(e)+"11.1")
      
    def test_007(self):
        """第三方商户 绑定商品从未上架 
                                 邮费                      可以编辑为0
        """
        loginPage(self.driver).login("weiyun","Weiyun0206")
        driver = self.driver
         
        sku_attribute = {       u'颜色'   : u'蓝色',
                                u'尺寸'   : u'38'}
        self.new_sku_one(u"即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬",u"柠檬柠檬柠檬柠檬柠檬柠檬柠檬柠檬柠檬柠檬",True,0.01,0.01,**sku_attribute) 
        self.new_sku_two(True, "001001001001001001001") 
        skuTable = Table(self.driver,"/html/body/div[1]/div/table/tbody",2)
        time.sleep(4)
        #获取新建SKU的ID
        skuId = skuTable.table_cell(1,4)
        #SKU绑定草稿商品
                #SKU绑定草稿商品
        #商品管理
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//div[2]/a").click()
        #driver.find_element_by_css_selector("a.item_ms. > span").click()
        time.sleep(1)
        #选择草稿
        Select(driver.find_element_by_id("state")).select_by_visible_text(u"草稿")
        time.sleep(2)
        #点击编辑
        driver.find_element_by_xpath("/html/body/div[1]/div/table/tbody/tr[1]/td[11]/a[1]/button").click()
        time.sleep(2)
        #新增关联sku
        driver.find_element_by_xpath("//button").click()
        time.sleep(2)
        driver.find_element_by_name("sku_id").clear()
        driver.find_element_by_name("sku_id").send_keys(skuId)
        time.sleep(2)
        driver.find_element_by_xpath("//button[@type='button']").click() 
        time.sleep(2)   
        driver.find_element_by_xpath("//div[12]/button").click()
        time.sleep(4)
        #进入SKU管理                                                           
        driver.find_element_by_xpath("//div[2]/a[2]/span").click()
        time.sleep(3)
        driver.find_element_by_id("sku_id").send_keys(skuId)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/button").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/table/tbody/tr[2]/td[12]/a[1]/button").click()
        time.sleep(2)
        #SKU邮费
        driver.find_element_by_css_selector("input.mail_fee.base-unit").clear()
        driver.find_element_by_css_selector("input.mail_fee.base-unit").send_keys(u"0.00")
        time.sleep(1)
        #保存
        driver.find_element_by_xpath("//div[11]/button").click()
        time.sleep(2)
        #验证新的邮费
        try: self.assertEqual(skuTable.table_cell(1,8), u"￥0.00")
        except AssertionError as e: self.verificationErrors.append(str(e)+"8.1")
     
    def test_008(self):
        """第三方商户 绑定商品从未上架 
           SKU库存数量        可以编辑
        """
        loginPage(self.driver).login("weiyun","Weiyun0206")
        driver = self.driver
         
        sku_attribute = {       u'颜色'   : u'蓝色',
                                u'尺寸'   : u'38'}
        self.new_sku_one(u"即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬",u"柠檬柠檬柠檬柠檬柠檬柠檬柠檬柠檬柠檬柠檬",True,0.01,0.01,**sku_attribute) 
        self.new_sku_two(True, "001001001001001001001") 
        skuTable = Table(self.driver,"/html/body/div[1]/div/table/tbody",2)
        time.sleep(4)
        #获取新建SKU的ID
        skuId = skuTable.table_cell(1,4)
        #SKU绑定草稿商品
                #SKU绑定草稿商品
        #商品管理
        driver.implicitly_wait(10)
        driver.find_element_by_xpath("//div[2]/a").click()
        #driver.find_element_by_css_selector("a.item_ms. > span").click()
        time.sleep(1)
        #选择草稿
        Select(driver.find_element_by_id("state")).select_by_visible_text(u"草稿")
        time.sleep(2)
        #点击编辑
        driver.find_element_by_xpath("/html/body/div[1]/div/table/tbody/tr[1]/td[11]/a[1]/button").click()
        time.sleep(2)
        #新增关联sku
        driver.find_element_by_xpath("//button").click()
        time.sleep(2)
        driver.find_element_by_name("sku_id").clear()
        driver.find_element_by_name("sku_id").send_keys(skuId)
        time.sleep(2)
        driver.find_element_by_xpath("//button[@type='button']").click() 
        time.sleep(2)   
        driver.find_element_by_xpath("//div[12]/button").click()
        time.sleep(4)
         
        #库存管理
        time.sleep(2)
        driver.find_element_by_xpath("//a[2]/span").click()
        time.sleep(2)
        #要邮寄SKU库存
        driver.find_element_by_xpath("/html/body/div[4]/div[2]/a[1]/span").click()
        time.sleep(2)
        #入库
        driver.find_element_by_xpath("//td[12]/button").click()
        time.sleep(1)
        driver.find_element_by_name("num").clear()
        driver.find_element_by_name("num").send_keys("500")
        time.sleep(1)
        driver.find_element_by_xpath("//button[@type='button']").click()
        time.sleep(3)
        #商品管理
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[2]/div[3]/a[3]/span").click()
        time.sleep(3)
        #SKU管理
        driver.find_element_by_css_selector("a.sku_ms > span").click()
        time.sleep(2)
        #进入编辑
        driver.find_element_by_xpath("//td[12]/a/button").click()
        try: self.assertEqual("500", driver.find_element_by_xpath("//div[10]/div").text)
        except AssertionError as e: self.verificationErrors.append(str(e)+"13.1")
     
    #编辑SKU：绑定商品审批中
    def test_009(self):
        """第三方商户 绑定商品审批中 
           SKU长名称                                                不可编辑
           SKU短名称                                                不可编辑
                                 邮寄类型                                                     不可编辑
                                 单价                                                             不可编辑
                                 邮费                                                             不可编辑
           SKU属性增加、删除                                不可编辑
                                是否支持退货                                              不可编辑
                                三方商家SKU编号                                     不可编辑                   
        """
        loginPage(self.driver).login("weiyun","Weiyun0206")
        driver = self.driver
         
        sku_attribute = {       u'颜色'   : u'蓝色',
                                u'尺寸'   : u'38'}
        self.new_sku_one(u"即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬",u"柠檬柠檬柠檬柠檬柠檬柠檬柠檬柠檬柠檬柠檬",True,0.01,0.01,**sku_attribute) 
        self.new_sku_two(True, "001001001001001001001") 
        skuTable = Table(self.driver,"/html/body/div[1]/div/table/tbody",2)
        time.sleep(4)
        
        skuId = skuTable.table_cell(1,4)
        skulist = [skuId]        
        #入库
        BasicOperation(self.driver).stock_sku(True, skuId, 500)
        time.sleep(3)       
        #新增商品 绑定sku
        BasicOperation(self.driver).new_sku(u"水果柠檬酸水果柠檬酸水果柠檬酸水果柠檬酸水果柠檬酸水果柠檬酸水果柠檬酸水果柠檬酸", u"柠檬酸酸酸柠檬酸酸酸柠檬酸酸酸柠檬酸酸酸", 1, 0.02, True, u"颜色", "C:\\Users\\yangweijia\\Pictures\\jpg\\6619393151235890154.jpg", False,*skulist)
        time.sleep(3)
        goodsTable = Table(self.driver,"/html/body/div[1]/div/table/tbody",1)
        goods_id = goodsTable.table_cell(1, 8)
        #补充加上数量
        BasicOperation(self.driver).add_list_num(goods_id, 200)
        time.sleep(2)       
        #提交审核
        driver.find_element_by_xpath("//td[11]/button").click()
        time.sleep(1)
        driver.find_element_by_id("up-ensure").click()
        time.sleep(4)
        #编辑sku
        driver.find_element_by_xpath("/html/body/div[5]/div[2]/a[2]/span").click()
        time.sleep(2)
        driver.find_element_by_id("sku_id").send_keys(skuId)
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/button").click()
        time.sleep(3)
        driver.find_element_by_xpath("/html/body/div[1]/div/table/tbody/tr[2]/td[12]/a[1]/button").click()
        time.sleep(2)
        


        #SKU长名称：不可编辑    
        try: self.assertEqual(driver.find_element_by_css_selector("textarea.base-unit.pgoods-setting-long-name").get_attribute("disabled"), u"true")
        except AssertionError as e: self.verificationErrors.append(str(e)+"25.1")
        #SKU短名称：不可编辑
        try: self.assertEqual(driver.find_element_by_css_selector("textarea.base-unit.pgoods-setting-short-name").get_attribute("disabled"), u"true")
        except AssertionError as e: self.verificationErrors.append(str(e)+"26.1")
        #邮寄类型：不可编辑
        try: self.assertEqual(driver.find_element_by_xpath("//input").get_attribute("disabled"), u"true")
        except AssertionError as e: self.verificationErrors.append(str(e)+"27.1")
        try: self.assertEqual(driver.find_element_by_xpath("//input[2]").get_attribute("disabled"), u"true")
        except AssertionError as e: self.verificationErrors.append(str(e)+"27.2")
        #单价：不可编辑
        try: self.assertEqual(driver.find_element_by_css_selector("input.unit_price.base-unit").get_attribute("disabled"), u"true")
        except AssertionError as e: self.verificationErrors.append(str(e)+"28.1")
        #邮费：不可编辑
        try: self.assertEqual(driver.find_element_by_css_selector("input.mail_fee.base-unit").get_attribute("disabled"), u"true")
        except AssertionError as e: self.verificationErrors.append(str(e)+"29.1")
        #SKU属性：不可编辑
        try: self.assertEqual(driver.find_element_by_xpath("//button").get_attribute("disabled"), u"true")
        except AssertionError as e: self.verificationErrors.append(str(e)+"9.1")
        #sku属性：不可删除
        oldskuAttributeOne = driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[1]").text
        driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[1]").click()       
        try: self.assertEqual(driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[1]").text, oldskuAttributeOne)
        except AssertionError as e: self.verificationErrors.append(str(e)+"10.1")      
        oldskuAttributeTwo = driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[2]").text
        driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[2]").click()       
        try: self.assertEqual(driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[2]").text, oldskuAttributeTwo)
        except AssertionError as e: self.verificationErrors.append(str(e)+"10.2")
        #退货：不可编辑
        try: self.assertEqual(driver.find_element_by_xpath("html/body/div[1]/div/input[5]").get_attribute("disabled"), u"true")
        except AssertionError as e: self.verificationErrors.append(str(e)+"9.1")
        try: self.assertEqual(driver.find_element_by_xpath("/html/body/div[1]/div/input[6]").get_attribute("disabled"), u"true")
        except AssertionError as e: self.verificationErrors.append(str(e)+"9.1")
        #三方商家SKU编号
        try: self.assertEqual(driver.find_element_by_name("third_party_sku").get_attribute("disabled"), u"true")
        except AssertionError as e: self.verificationErrors.append(str(e)+"9.1")
           
    def test_010(self):
        """第三方商户 绑定商品审批中 
           SKU库存数量        可以编辑
        """
        loginPage(self.driver).login("weiyun","Weiyun0206")
        driver = self.driver
         
        sku_attribute = {       u'颜色'   : u'蓝色',
                                u'尺寸'   : u'38'}
        self.new_sku_one(u"即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬即食柠檬",u"柠檬柠檬柠檬柠檬柠檬柠檬柠檬柠檬柠檬柠檬",True,0.01,0.01,**sku_attribute) 
        self.new_sku_two(True, "001001001001001001001") 
        skuTable = Table(self.driver,"/html/body/div[1]/div/table/tbody",2)
        time.sleep(4)
        
        skuId = skuTable.table_cell(1,4)
        skulist = [skuId]        
        #入库
        BasicOperation(self.driver).stock_sku(True, skuId, 500)
        time.sleep(3)       
        #新增商品 绑定sku
        BasicOperation(self.driver).new_sku(u"水果柠檬酸水果柠檬酸水果柠檬酸水果柠檬酸水果柠檬酸水果柠檬酸水果柠檬酸水果柠檬酸", u"柠檬酸酸酸柠檬酸酸酸柠檬酸酸酸柠檬酸酸酸", 1, 0.02, True, u"颜色", "C:\\Users\\yangweijia\\Pictures\\jpg\\6619393151235890154.jpg", False,*skulist)
        time.sleep(3)
        goodsTable = Table(self.driver,"/html/body/div[1]/div/table/tbody",1)
        goods_id = goodsTable.table_cell(1, 8)
        #补充加上数量
        BasicOperation(self.driver).add_list_num(goods_id, 200)
        time.sleep(2)       
        #提交审核
        driver.find_element_by_xpath("//td[11]/button").click()
        time.sleep(1)
        driver.find_element_by_id("up-ensure").click()
        time.sleep(4)       
        #入库
        BasicOperation(self.driver).stock_sku(True,skuId,400)
        time.sleep(3)
        #商品管理
        driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[2]/div[3]/a[3]/span").click()
        time.sleep(3)
        #SKU管理
        driver.find_element_by_css_selector("a.sku_ms > span").click()
        time.sleep(2)
        #进入编辑
        driver.find_element_by_xpath("//td[12]/a/button").click()
        try: self.assertEqual("900", driver.find_element_by_xpath("//div[10]/div").text)
        except AssertionError as e: self.verificationErrors.append(str(e)+"13.1")
     
#     #编辑SKU：绑定商品上架中    
#     def test_011(self):
#         """第三方商户 绑定商品从未上架 
#            SKU长名称                                                不可编辑
#            SKU短名称                                                不可编辑
#                                  邮寄类型                                                     不可编辑
#                                  单价                                                             不可编辑
#                                  邮费                                                             不可编辑
#            SKU属性增加、删除                                不可编辑
#                                 是否支持退货                                              不可编辑
#                                 三方商家SKU编号                                     不可编辑                   
#         """    
#         driver = Basis.driver
#                
#         #新建sku
#         self.thirdUser_sku()
#         #获取新建SKU的ID
#         time.sleep(4)
#         skuId = self.skuTable.table_cell(1,4)
#         skulist = [skuId]        
#         #入库
#         Basis.stock_sku(self, True, skuId, 500)
#         time.sleep(3)       
#         #新增商品 绑定sku
#         Basis.new_sku(self,u"水果柠檬酸水果柠檬酸水果柠檬酸水果柠檬酸水果柠檬酸水果柠檬酸水果柠檬酸水果柠檬酸", u"柠檬酸酸酸柠檬酸酸酸柠檬酸酸酸柠檬酸酸酸", 1, 0.02, True, u"颜色", "C:\\Users\\yangweijia\\Pictures\\jpg\\6619393151235890154.jpg", False,*skulist)
#         time.sleep(3)
#         goods_id = Goods.goodsTable.table_cell(1, 8)
#         #补充加上数量
#         Basis.add_list_num(self, goods_id, 200)
#         time.sleep(2)       
#         #提交审核
#         driver.find_element_by_xpath("//td[11]/button").click()
#         time.sleep(1)
#         driver.find_element_by_id("up-ensure").click()
#         time.sleep(4)
#         
#         #退出登录
#         js_one="document.querySelector('.cmbs-setting').style.opacity='100';"
#         driver.execute_script(js_one) 
#         time.sleep(2) 
#         js_two="document.querySelector('.logout').click();"   
#         driver.execute_script(js_two)
#         time.sleep(2)
#         #登录第三方Boss
#         driver.find_element_by_name("login[name]").clear()
#         driver.find_element_by_name("login[name]").send_keys('boss_admin')
#         time.sleep(1)
#         driver.find_element_by_name("login[pwd]").clear()
#         driver.find_element_by_name("login[pwd]").send_keys('Boss123')
#         time.sleep(1)      
#         driver.find_element_by_css_selector("button.llv-submit").click()
#         time.sleep(2)
#         #商品管理
#         driver.find_element_by_xpath("//a[2]/span").click()
#         time.sleep(2)
#         #上架审批
#         driver.find_element_by_xpath("/html/body/div[5]/div[2]/a[4]/span").click()
#         time.sleep(2)
#         #输入商品ID
#         driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/div[1]/div/div[2]/input").send_keys(goods_id)
#         time.sleep(1)
#         #搜索
#         driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/div[1]/div/button").click()
#         time.sleep(2)
#         #通过
#         driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/span[10]/button[1]").click()
#         time.sleep(1)
#         #确认
#         driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/a[2]").click()
#         time.sleep(2)
#         #退出登录
#         driver.execute_script(js_one) 
#         time.sleep(2) 
#         driver.execute_script(js_two)
#         time.sleep(2)
#         #登录三方商户
#         driver.find_element_by_name("login[name]").clear()
#         driver.find_element_by_name("login[name]").send_keys('weiyun')
#         time.sleep(1)
#         driver.find_element_by_name("login[pwd]").clear()
#         driver.find_element_by_name("login[pwd]").send_keys('Weiyun0206')
#         time.sleep(1)      
#         driver.find_element_by_css_selector("button.llv-submit").click()
#         time.sleep(2)
#         #SKU管理
#         driver.find_element_by_css_selector("a.sku_ms > span").click()
#         time.sleep(2)
#         #ID
#         driver.find_element_by_id("sku_id").send_keys(skuId)
#         time.sleep(1)
#         #搜索
#         driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/button").click()
#         time.sleep(2)
#         #进入编辑
#         driver.find_element_by_xpath("//td[12]/a/button").click()
#         time.sleep(2)
#         #SKU长名称：不可编辑    
#         try: self.assertEqual(driver.find_element_by_css_selector("textarea.base-unit.pgoods-setting-long-name").get_attribute("disabled"), u"true")
#         except AssertionError as e: self.verificationErrors.append(str(e)+"11.1")
#         #SKU短名称：不可编辑
#         try: self.assertEqual(driver.find_element_by_css_selector("textarea.base-unit.pgoods-setting-short-name").get_attribute("disabled"), u"true")
#         except AssertionError as e: self.verificationErrors.append(str(e)+"11.2")
#         #邮寄类型：不可编辑
#         try: self.assertEqual(driver.find_element_by_xpath("//input").get_attribute("disabled"), u"true")
#         except AssertionError as e: self.verificationErrors.append(str(e)+"11.3")
#         try: self.assertEqual(driver.find_element_by_xpath("//input[2]").get_attribute("disabled"), u"true")
#         except AssertionError as e: self.verificationErrors.append(str(e)+"11.4")
#         #单价：不可编辑
#         try: self.assertEqual(driver.find_element_by_css_selector("input.unit_price.base-unit").get_attribute("disabled"), u"true")
#         except AssertionError as e: self.verificationErrors.append(str(e)+"11.5")
#         #邮费：不可编辑
#         try: self.assertEqual(driver.find_element_by_css_selector("input.mail_fee.base-unit").get_attribute("disabled"), u"true")
#         except AssertionError as e: self.verificationErrors.append(str(e)+"11.6")
#         #SKU属性：不可编辑
#         try: self.assertEqual(driver.find_element_by_xpath("//button").get_attribute("disabled"), u"true")
#         except AssertionError as e: self.verificationErrors.append(str(e)+"11.7")
#         #sku属性：不可删除
#         oldskuAttributeOne = driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[1]").text
#         driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[1]").click()       
#         try: self.assertEqual(driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[1]").text, oldskuAttributeOne)
#         except AssertionError as e: self.verificationErrors.append(str(e)+"11.8")      
#         oldskuAttributeTwo = driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[2]").text
#         driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[2]").click()       
#         try: self.assertEqual(driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[2]").text, oldskuAttributeTwo)
#         except AssertionError as e: self.verificationErrors.append(str(e)+"11.9")
#         #退货：不可编辑
#         try: self.assertEqual(driver.find_element_by_xpath("html/body/div[1]/div/input[5]").get_attribute("disabled"), u"true")
#         except AssertionError as e: self.verificationErrors.append(str(e)+"11.10")
#         try: self.assertEqual(driver.find_element_by_xpath("/html/body/div[1]/div/input[6]").get_attribute("disabled"), u"true")
#         except AssertionError as e: self.verificationErrors.append(str(e)+"11.11")
#         #三方商家SKU编号
#         try: self.assertEqual(driver.find_element_by_name("third_party_sku").get_attribute("disabled"), u"true")
#         except AssertionError as e: self.verificationErrors.append(str(e)+"11.12")
#     
#     def test_012(self):
#         """第三方商户 绑定商品上架中 
#            SKU库存数量        可以编辑
#         """
#         driver = Basis.driver
#                
#         #新建sku
#         self.thirdUser_sku()
#         #获取新建SKU的ID
#         time.sleep(4)
#         skuId = self.skuTable.table_cell(1,4)
#         skulist = [skuId]        
#         #入库
#         Basis.stock_sku(self, True, skuId, 500)
#         time.sleep(3)       
#         #新增商品 绑定sku
#         Basis.new_sku(self,u"水果柠檬酸水果柠檬酸水果柠檬酸水果柠檬酸水果柠檬酸水果柠檬酸水果柠檬酸水果柠檬酸", u"柠檬酸酸酸柠檬酸酸酸柠檬酸酸酸柠檬酸酸酸", 1, 0.02, True, u"颜色", "C:\\Users\\yangweijia\\Pictures\\jpg\\6619393151235890154.jpg", False,*skulist)
#         time.sleep(3)
#         goods_id = Goods.goodsTable.table_cell(1, 8)
#         #补充加上数量
#         Basis.add_list_num(self, goods_id, 200)
#         time.sleep(2)       
#         #提交审核
#         driver.find_element_by_xpath("//td[11]/button").click()
#         time.sleep(1)
#         driver.find_element_by_id("up-ensure").click()
#         time.sleep(4)
#         
#         #退出登录
#         js_one="document.querySelector('.cmbs-setting').style.opacity='100';"
#         driver.execute_script(js_one) 
#         time.sleep(2) 
#         js_two="document.querySelector('.logout').click();"   
#         driver.execute_script(js_two)
#         time.sleep(2)
#         #登录第三方Boss
#         driver.find_element_by_name("login[name]").clear()
#         driver.find_element_by_name("login[name]").send_keys('boss_admin')
#         time.sleep(1)
#         driver.find_element_by_name("login[pwd]").clear()
#         driver.find_element_by_name("login[pwd]").send_keys('Boss123')
#         time.sleep(1)      
#         driver.find_element_by_css_selector("button.llv-submit").click()
#         time.sleep(2)
#         #商品管理
#         driver.find_element_by_xpath("//a[2]/span").click()
#         time.sleep(2)
#         #上架审批
#         driver.find_element_by_xpath("/html/body/div[5]/div[2]/a[4]/span").click()
#         time.sleep(2)
#         #输入商品ID
#         driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/div[1]/div/div[2]/input").send_keys(goods_id)
#         time.sleep(1)
#         #搜索
#         driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/div[1]/div/button").click()
#         time.sleep(2)
#         #通过
#         driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/span[10]/button[1]").click()
#         time.sleep(1)
#         #确认
#         driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/a[2]").click()
#         time.sleep(2)
#         #退出登录
#         driver.execute_script(js_one) 
#         time.sleep(2) 
#         driver.execute_script(js_two)
#         time.sleep(2)
#         #登录三方商户
#         driver.find_element_by_name("login[name]").clear()
#         driver.find_element_by_name("login[name]").send_keys('weiyun')
#         time.sleep(1)
#         driver.find_element_by_name("login[pwd]").clear()
#         driver.find_element_by_name("login[pwd]").send_keys('Weiyun0206')
#         time.sleep(1)      
#         driver.find_element_by_css_selector("button.llv-submit").click()
#         time.sleep(2)
#         #入库
#         Basis.stock_sku(self,True,skuId,"400")
#         time.sleep(3)
#         #商品管理
#         driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[2]/div[3]/a[3]/span").click()
#         time.sleep(3)
#         #SKU管理
#         driver.find_element_by_css_selector("a.sku_ms > span").click()
#         time.sleep(2)
#         #进入编辑
#         driver.find_element_by_xpath("//td[12]/a/button").click()
#         try: self.assertEqual("900", driver.find_element_by_xpath("//div[10]/div").text)
#         except AssertionError as e: self.verificationErrors.append(str(e)+"13.1")
#         
#     #编辑SKU：绑定商品下架后
#     def test_013(self): 
#         """第三方商户 绑定商品下架后 
#            SKU长名称                                                不可编辑
#            SKU短名称                                                不可编辑
#                                  邮寄类型                                                     不可编辑
#                                  单价                                                             可以编辑
#                                  邮费                                                             可以编辑
#            SKU属性增加、删除                                不可编辑
#                                 是否支持退货                                              可以编辑
#                                 三方商家SKU编号                                     可以编辑              
#         """ 
#         driver = Basis.driver
#                
#         #新建sku
#         self.thirdUser_sku()
#         #获取新建SKU的ID
#         time.sleep(4)
#         skuId = self.skuTable.table_cell(1,4)
#         skulist = [skuId]        
#         #入库
#         Basis.stock_sku(self, True, skuId, 500)
#         time.sleep(3)       
#         #新增商品 绑定sku
#         Basis.new_sku(self,u"水果柠檬酸水果柠檬酸水果柠檬酸水果柠檬酸水果柠檬酸水果柠檬酸水果柠檬酸水果柠檬酸", u"柠檬酸酸酸柠檬酸酸酸柠檬酸酸酸柠檬酸酸酸", 1, 0.02, True, u"颜色", "C:\\Users\\yangweijia\\Pictures\\jpg\\6619393151235890154.jpg", False,*skulist)
#         time.sleep(3)
#         goods_id = Goods.goodsTable.table_cell(1, 8)
#         #补充加上数量
#         Basis.add_list_num(self, goods_id, 200)
#         time.sleep(2)       
#         #提交审核
#         driver.find_element_by_xpath("//td[11]/button").click()
#         time.sleep(1)
#         driver.find_element_by_id("up-ensure").click()
#         time.sleep(4)
#         
#         #退出登录
#         js_one="document.querySelector('.cmbs-setting').style.opacity='100';"
#         driver.execute_script(js_one) 
#         time.sleep(2) 
#         js_two="document.querySelector('.logout').click();"   
#         driver.execute_script(js_two)
#         time.sleep(2)
#         #登录第三方Boss
#         driver.find_element_by_name("login[name]").clear()
#         driver.find_element_by_name("login[name]").send_keys('boss_admin')
#         time.sleep(1)
#         driver.find_element_by_name("login[pwd]").clear()
#         driver.find_element_by_name("login[pwd]").send_keys('Boss123')
#         time.sleep(1)      
#         driver.find_element_by_css_selector("button.llv-submit").click()
#         time.sleep(2)
#         #商品管理
#         driver.find_element_by_xpath("//a[2]/span").click()
#         time.sleep(2)
#         #上架审批
#         driver.find_element_by_xpath("/html/body/div[5]/div[2]/a[4]/span").click()
#         time.sleep(2)
#         #输入商品ID
#         driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/div[1]/div/div[2]/input").send_keys(goods_id)
#         time.sleep(1)
#         #搜索
#         driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/div[1]/div/button").click()
#         time.sleep(2)
#         #通过
#         driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/span[10]/button[1]").click()
#         time.sleep(1)
#         #确认
#         driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/a[2]").click()
#         time.sleep(2)
#         #退出登录
#         driver.execute_script(js_one) 
#         time.sleep(2) 
#         driver.execute_script(js_two)
#         time.sleep(2)
#         #登录三方商户
#         driver.find_element_by_name("login[name]").clear()
#         driver.find_element_by_name("login[name]").send_keys('weiyun')
#         time.sleep(1)
#         driver.find_element_by_name("login[pwd]").clear()
#         driver.find_element_by_name("login[pwd]").send_keys('Weiyun0206')
#         time.sleep(1)      
#         driver.find_element_by_css_selector("button.llv-submit").click()
#         time.sleep(2) 
#         #搜索商品
#         Basis.goods_search(self, goods_id)
#         #下架
#         driver.find_element_by_xpath("//td[11]/button").click()
#         time.sleep(2)
#         #入库
#         driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/a[2]").click()
#         time.sleep(3)
#         #搜索sku
#         Basis.sku_search(self, skuId)
#         #进入编辑
#         driver.find_element_by_xpath("//td[12]/a/button").click()
#         time.sleep(2)
# 
#         #SKU长名称：不可编辑
#         try: self.assertEqual(driver.find_element_by_css_selector("textarea.base-unit.pgoods-setting-long-name").get_attribute("disabled"), u"true")
#         except AssertionError as e: self.verificationErrors.append(str(e)+"3.1")
#         #SKU短名称：不可编辑
#         try: self.assertEqual(driver.find_element_by_css_selector("textarea.base-unit.pgoods-setting-short-name").get_attribute("disabled"), u"true")
#         except AssertionError as e: self.verificationErrors.append(str(e)+"4.1")
#         #邮寄类型：不可编辑
#         try: self.assertEqual(driver.find_element_by_xpath("//input").get_attribute("disabled"), u"true")
#         except AssertionError as e: self.verificationErrors.append(str(e)+"4.1")
#         try: self.assertEqual(driver.find_element_by_xpath("//input[2]").get_attribute("disabled"), u"true")
#         except AssertionError as e: self.verificationErrors.append(str(e)+"4.2")
#         #单价：可以编辑
#         #改变单价
#         oldPrice = float(driver.find_element_by_css_selector("input.unit_price.base-unit").get_attribute("value"))
#         newPrice = oldPrice + 1.00
#         driver.find_element_by_css_selector("input.unit_price.base-unit").clear()
#         driver.find_element_by_css_selector("input.unit_price.base-unit").send_keys(newPrice)
#         time.sleep(1)
#         #邮费：可以编辑
#         #改变邮费
#         oldMailCost = float(driver.find_element_by_css_selector("input.mail_fee.base-unit").get_attribute("value"))
#         newMailCost = oldMailCost + 1.00
#         driver.find_element_by_css_selector("input.mail_fee.base-unit").clear()
#         driver.find_element_by_css_selector("input.mail_fee.base-unit").send_keys(newMailCost)
#         time.sleep(1)
#         #SKU属性：不可编辑
#         try: self.assertEqual(driver.find_element_by_xpath("//button").get_attribute("disabled"), u"true")
#         except AssertionError as e: self.verificationErrors.append(str(e)+"9.1")
#         #sku属性：不可删除
#         oldskuAttributeOne = driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[1]").text
#         driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[1]").click()
#         
#         try: self.assertEqual(driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[1]").text, oldskuAttributeOne)
#         except AssertionError as e: self.verificationErrors.append(str(e)+"10.1")
#         
#         oldskuAttributeTwo = driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[2]").text
#         driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[2]").click()
#         
#         try: self.assertEqual(driver.find_element_by_xpath("/html/body/div[1]/div/div[7]/div[2]").text, oldskuAttributeTwo)
#         except AssertionError as e: self.verificationErrors.append(str(e)+"10.2")
#         #退货：可以编辑
#         #变为不退货
#         driver.find_element_by_xpath("/html/body/div[1]/div/input[6]").click()
#         time.sleep(1)
#         #三方商家SKU编号：可以编辑
#         driver.find_element_by_name("third_party_sku").clear()
#         driver.find_element_by_name("third_party_sku").send_keys("003003")
#         time.sleep(1)
#         #保存
#         driver.find_element_by_xpath("//div[11]/button").click()
#         time.sleep(4)
#         #验证新的单价
#         try: self.assertEqual(self.skuTable.table_cell(1,9), u"￥1.01")
#         except AssertionError as e: self.verificationErrors.append(str(e)+"6.1")
#         #验证新的邮费
#         try: self.assertEqual(self.skuTable.table_cell(1,8), u"￥1.01")
#         except AssertionError as e: self.verificationErrors.append(str(e)+"7.1")
#         #验证三方商家sku编号
#         try: self.assertEqual(self.skuTable.table_cell(1,11), "003003")
#         except AssertionError as e: self.verificationErrors.append(str(e)+"12.1")              
#         #进入编辑
#         driver.find_element_by_xpath("//td[12]/a/button").click()
#         time.sleep(2)
#         #退货
#         try: self.assertEqual(self.driver.find_element_by_xpath("/html/body/div[1]/div/input[5]").get_attribute("checked"), None)
#         except AssertionError as e: self.verificationErrors.append(str(e)+"11.1")
#         
#     def test_014(self):
#         """第三方商户   绑定商品下架后 
#            SKU库存数量          可以编辑
#         """
#         driver = Basis.driver
#                
#         #新建sku
#         self.thirdUser_sku()
#         #获取新建SKU的ID
#         time.sleep(4)
#         skuId = self.skuTable.table_cell(1,4)
#         skulist = [skuId]        
#         #入库
#         Basis.stock_sku(self, True, skuId, 500)
#         time.sleep(3)       
#         #新增商品 绑定sku
#         Basis.new_sku(self,u"水果柠檬酸水果柠檬酸水果柠檬酸水果柠檬酸水果柠檬酸水果柠檬酸水果柠檬酸水果柠檬酸", u"柠檬酸酸酸柠檬酸酸酸柠檬酸酸酸柠檬酸酸酸", 1, 0.02, True, u"颜色", "C:\\Users\\yangweijia\\Pictures\\jpg\\6619393151235890154.jpg", False,*skulist)
#         time.sleep(3)
#         goods_id = Goods.goodsTable.table_cell(1, 8)
#         #补充加上数量
#         Basis.add_list_num(self, goods_id, 200)
#         time.sleep(2)       
#         #提交审核
#         driver.find_element_by_xpath("//td[11]/button").click()
#         time.sleep(1)
#         driver.find_element_by_id("up-ensure").click()
#         time.sleep(4)
#         
#         #退出登录
#         js_one="document.querySelector('.cmbs-setting').style.opacity='100';"
#         driver.execute_script(js_one) 
#         time.sleep(2) 
#         js_two="document.querySelector('.logout').click();"   
#         driver.execute_script(js_two)
#         time.sleep(2)
#         #登录第三方Boss
#         driver.find_element_by_name("login[name]").clear()
#         driver.find_element_by_name("login[name]").send_keys('boss_admin')
#         time.sleep(1)
#         driver.find_element_by_name("login[pwd]").clear()
#         driver.find_element_by_name("login[pwd]").send_keys('Boss123')
#         time.sleep(1)      
#         driver.find_element_by_css_selector("button.llv-submit").click()
#         time.sleep(2)
#         #商品管理
#         driver.find_element_by_xpath("//a[2]/span").click()
#         time.sleep(2)
#         #上架审批
#         driver.find_element_by_xpath("/html/body/div[5]/div[2]/a[4]/span").click()
#         time.sleep(2)
#         #输入商品ID
#         driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/div[1]/div/div[2]/input").send_keys(goods_id)
#         time.sleep(1)
#         #搜索
#         driver.find_element_by_xpath("/html/body/div[1]/div[1]/form/div[1]/div/button").click()
#         time.sleep(2)
#         #通过
#         driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[2]/div/span[10]/button[1]").click()
#         time.sleep(1)
#         #确认
#         driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/a[2]").click()
#         time.sleep(2)
#         #退出登录
#         driver.execute_script(js_one) 
#         time.sleep(2) 
#         driver.execute_script(js_two)
#         time.sleep(2)
#         #登录三方商户
#         driver.find_element_by_name("login[name]").clear()
#         driver.find_element_by_name("login[name]").send_keys('weiyun')
#         time.sleep(1)
#         driver.find_element_by_name("login[pwd]").clear()
#         driver.find_element_by_name("login[pwd]").send_keys('Weiyun0206')
#         time.sleep(1)      
#         driver.find_element_by_css_selector("button.llv-submit").click()
#         time.sleep(2) 
#         #搜索商品
#         Basis.goods_search(self, goods_id)
#         #下架
#         driver.find_element_by_xpath("//td[11]/button").click()
#         time.sleep(2)
#         #入库
#         driver.find_element_by_xpath("/html/body/div[2]/div/div/div[2]/a[2]").click()
#         time.sleep(3)
#         
#         #入库
#         Basis.stock_sku(self, True, skuId, 300)
#         #搜索sku
#         Basis.sku_search(self, skuId)       
#         #进入编辑
#         driver.find_element_by_xpath("//td[12]/a/button").click()
#         try: self.assertEqual("800", driver.find_element_by_xpath("//div[10]/div").text)
#         except AssertionError as e: self.verificationErrors.append(str(e)+"13.1")
#         
#         
        



if __name__ == "__main__":
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(SkuThirdParty("test_001"))
       
          
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
