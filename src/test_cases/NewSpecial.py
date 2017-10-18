# -*- coding: utf-8 -*-
# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, datetime, re,sys
sys.path.append("./models")
sys.path.append("./page_obj")
from models.myunit import MyTest
from page_obj.loginPage import loginPage
# from lib2to3.pgen2.driver import Driver
from sqlite3 import Time


class NewSpecial(MyTest):
        
    #进入专题制作配置页面
    def makeSpecial(self):
        driver = self.driver
        driver.find_element_by_css_selector("a.data_ms.active > span").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[4]/span").click()
        time.sleep(2)
        #获取当前窗口句柄
        now_handle = driver.current_window_handle
        #打开新窗口
        driver.find_element_by_css_selector("button.btn.btn-default").click()
        time.sleep(2)
        #切换窗口
        for handle in driver.window_handles:
            if handle == now_handle:
                pass
                time.sleep(1)
            else: 
                driver.switch_to_window(handle)                
    #时间筛选
    def selectByTime(self,timeStr):
        driver = self.driver
        driver.find_element_by_css_selector("a.data_ms.active > span").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[4]/span").click()
        time.sleep(2) 
        
        Select(driver.find_element_by_css_selector("select.date-pick.base-unit")).select_by_visible_text(timeStr)
        time.sleep(2)
        
        today=datetime.date.today()  
       #oneday=datetime.timedelta(days=1) 
        sevenday = datetime.timedelta(days=7)
       # endTime=today-oneday
        endTimeTup = time.mktime(today.timetuple())
        
        startTime = today-sevenday
        startTimeTup = time.mktime(startTime.timetuple())
        #数量
        num = len(driver.find_elements_by_class_name("om_item"))
        
        if num == 0:
            try: self.assertEqual(driver.find_element_by_id("j_pnav_count").text,u'共0页')
            except AssertionError as e: self.verificationErrors.append(str(e))  
            
        else:
            while True:
                try:self.assertGreaterEqual(time.mktime(time.strptime(driver.find_element_by_xpath("//div[2]/div[2]/div/div/span[3]").text,"%Y-%m-%d %H:%M:%S")), startTimeTup)
                except AssertionError as e: self.verificationErrors.append(str(e))
                try:self.assertLessEqual(time.mktime(time.strptime(driver.find_element_by_xpath("//div[2]/div[2]/div/div/span[3]").text,"%Y-%m-%d %H:%M:%S")), endTimeTup)
                except AssertionError as e: self.verificationErrors.append(str(e))
                num = len(driver.find_elements_by_class_name("om_item"))
                if num > 1:
                    for i in range(2,num+1):
                        try:self.assertGreaterEqual(time.mktime(time.strptime(driver.find_element_by_xpath("//div[%s]/div/span[3]"%i).text,"%Y-%m-%d %H:%M:%S")), startTimeTup)
                        except AssertionError as e: self.verificationErrors.append(str(e))
                        try:self.assertLessEqual(time.mktime(time.strptime(driver.find_element_by_xpath("//div[%s]/div/span[3]"%i).text,"%Y-%m-%d %H:%M:%S")), endTimeTup)
                        except AssertionError as e: self.verificationErrors.append(str(e))
                if(driver.find_element_by_id("j_pnav_next").get_attribute("disabled") == None):
                    driver.find_element_by_id("j_pnav_next").click()
                    time.sleep(3)
                else:
                    break
                    
            
    def test_001(self): 
        '''
            001：制作专题：最长昵称+最长备注+一张图片+一个Tab+一个（一行两个）商品
        ''' 
        print "1"
        loginPage(self.driver).login("Oper","Oper")
        print "2"
        driver = self.driver
        driver.find_element_by_css_selector("a.data_ms.active > span").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[4]/span").click()
        time.sleep(2)
        #获取当前窗口句柄
        now_handle = driver.current_window_handle
        #打开新窗口
        driver.find_element_by_css_selector("button.btn.btn-default").click()
        time.sleep(2)
        #切换窗口
        for handle in driver.window_handles:
            driver.switch_to_window(handle)
            if handle == now_handle:
                pass
                time.sleep(1)
            else:     
                driver.find_element_by_name("l_name").clear()
                driver.find_element_by_name("l_name").send_keys("Sue")
        
                driver.find_element_by_xpath("(//input[@name='l_name'])[2]").clear()
                driver.find_element_by_xpath("(//input[@name='l_name'])[2]").send_keys(u"喔你你你你喔你你你你喔你你你你喔你你你你喔你你你你喔你你你你喔你你你你喔你你你你喔你你你你喔你你你你喔你你你你喔你你你你啦啦啦啦啦啦啦啦辣么啦啦啦没啦啦啦啦啦喔你你你你喔你你你你喔你你你你喔你你你你喔")
                 
                #上传图片
                js_one="var q=document.querySelector('#upload').style.display='block'"
                driver.execute_script(js_one)
                driver.find_element_by_id("upload").clear()
                driver.find_element_by_id("upload").send_keys("C:\\Users\\yangweijia\\Pictures\\jpg\\90071992647538756.jpg")
                #添加链接
                driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div/div[2]/input").clear()
                driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div/div[2]/input").send_keys("codoon://www.codoon.com/activity/activity_list?")
                #增加Tab
                driver.find_element_by_css_selector("button.add-tab.base-unit").click()
                #Tab名称
                driver.find_element_by_name("tab_name").clear()
                driver.find_element_by_name("tab_name").send_keys(u"一一一一一")
                #确认
                driver.find_element_by_xpath("//button[@type='button']").click()
                
                #添加商品
                driver.find_element_by_css_selector("button.base-unit.add-tab-goods").click()
                #商品ID
                driver.find_element_by_css_selector("textarea.base-unit.last").clear()
                driver.find_element_by_css_selector("textarea.base-unit.last").send_keys("15682649365469765893507")
                driver.find_element_by_css_selector("textarea.base-unit.last").clear()
                driver.find_element_by_css_selector("textarea.base-unit.last").send_keys("15682649365469765893507\n411941304218153299592925")

                driver.find_element_by_xpath("//button[@type='button']").click()
       
                driver.find_element_by_css_selector("button.add-tab.base-unit").click()
                driver.find_element_by_name("tab_name").clear()
                driver.find_element_by_name("tab_name").send_keys(u"二二二二二")
                driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
                Select(driver.find_element_by_xpath("//div[@id='J_content']/div/div[5]/div/div[2]/div[2]/span/select")).select_by_visible_text(u"左单行")
                driver.find_element_by_xpath("//div[@id='J_content']/div/div[5]/div/div[2]/div[2]/div/button").click()
                driver.find_element_by_css_selector("textarea.base-unit.last").clear()
                driver.find_element_by_css_selector("textarea.base-unit.last").send_keys("320565908718070678832071")
                driver.find_element_by_xpath("//button[@type='button']").click()
                driver.find_element_by_xpath("//div[@id='J_content']/div/div[6]/button").click()
        #回到列表页面        
        time.sleep(2)
        driver.switch_to_window(now_handle)
        time.sleep(2)
        
       
        specialName="Sue"
        specialNameCheck=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div/span[1]").text
        try: self.assertEqual(specialNameCheck,specialName)
        except AssertionError as e: self.verificationErrors.append(str(e)+"1")  

    def test_002(self):
        '''
            002：制作专题：最短昵称+没有备注+五张图片(jpg+png)+四个Tab+一个（一行两个）商品+一个（左单行）商品+多个（一行两个）商品+多个（左单行）商品
        '''
        driver = self.driver
        driver.find_element_by_css_selector("a.data_ms.active > span").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[4]/span").click()
        time.sleep(2)
        #获取当前窗口句柄
        now_handle = driver.current_window_handle
        #打开新窗口
        driver.find_element_by_css_selector("button.btn.btn-default").click()
        time.sleep(2)
        #切换窗口
        for handle in driver.window_handles:
            driver.switch_to_window(handle)
            if handle == now_handle:
                pass
                time.sleep(1)
            else:     
                driver.find_element_by_name("l_name").clear()
                driver.find_element_by_name("l_name").send_keys("S")

                #上传图片
                js_one="var q=document.querySelector('#upload').style.display='block'"
                driver.execute_script(js_one)
                driver.find_element_by_id("upload").clear()
                driver.find_element_by_id("upload").send_keys("C:\\Users\\yangweijia\\Pictures\\jpg\\90071992647538756.jpg")
                time.sleep(3)
                driver.find_element_by_id("upload").clear()
                driver.find_element_by_id("upload").send_keys("C:\\Users\\yangweijia\\Pictures\\jpg\\6619393151235890154.jpg")
                time.sleep(3)
                driver.find_element_by_id("upload").clear()
                driver.find_element_by_id("upload").send_keys("C:\\Users\\yangweijia\\Pictures\\jpg\\6630751106351088810.jpg")
                time.sleep(3)
                driver.find_element_by_id("upload").clear()
                driver.find_element_by_id("upload").send_keys("C:\\Users\\yangweijia\\Pictures\\jpg\\png\\20150726182924.png")
                time.sleep(3)
                driver.find_element_by_id("upload").clear()
                driver.find_element_by_id("upload").send_keys("C:\\Users\\yangweijia\\Pictures\\jpg\\png\\20150726183025.png")
                #添加链接
                driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div/div[2]/input").clear()
                driver.find_element_by_xpath("/html/body/div[1]/div/div[4]/div[2]/div/div[2]/input").send_keys("codoon://www.codoon.com/activity/activity_list?")
                time.sleep(2)
                
                #Tab名称1
                driver.find_element_by_css_selector("button.add-tab.base-unit").click()   
                driver.find_element_by_name("tab_name").clear()
                driver.find_element_by_name("tab_name").send_keys(u"一一一一一")
                driver.find_element_by_xpath("//button[@type='button']").click()
                time.sleep(1)

                #Tab名称3
                driver.find_element_by_css_selector("button.add-tab.base-unit").click()   
                driver.find_element_by_name("tab_name").clear()
                driver.find_element_by_name("tab_name").send_keys(u"三三三三三")
                driver.find_element_by_xpath("//button[@type='button']").click()
                time.sleep(1)

                #Tab名称4
                driver.find_element_by_css_selector("button.add-tab.base-unit").click()   
                driver.find_element_by_name("tab_name").clear()
                driver.find_element_by_name("tab_name").send_keys(u"四四四四四")
                driver.find_element_by_xpath("//button[@type='button']").click()
                time.sleep(1)

                #Tab1添加商品
                driver.find_element_by_css_selector("button.base-unit.add-tab-goods").click()
                driver.find_element_by_css_selector("textarea.base-unit.last").clear()
                driver.find_element_by_css_selector("textarea.base-unit.last").send_keys("320565908718070678832071")
                driver.find_element_by_xpath("//button[@type='button']").click()
                time.sleep(2)

                #Tab名称2
                driver.find_element_by_css_selector("button.add-tab.base-unit").click()
                driver.find_element_by_name("tab_name").clear()
                driver.find_element_by_name("tab_name").send_keys(u"二二二二二")
                driver.find_element_by_xpath("(//button[@type='button'])[2]").click()
                time.sleep(1)

                #Tab2添加商品
                Select(driver.find_element_by_xpath("//div[@id='J_content']/div/div[5]/div/div[2]/div[2]/span/select")).select_by_visible_text(u"左单行")
                driver.find_element_by_xpath("//div[@id='J_content']/div/div[5]/div/div[2]/div[2]/div/button").click()
                driver.find_element_by_css_selector("textarea.base-unit.last").clear()
                driver.find_element_by_css_selector("textarea.base-unit.last").send_keys("320565908718070678832071")
                driver.find_element_by_xpath("//button[@type='button']").click()
                time.sleep(1)

                #Tab3添加商品
                driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div/div[2]/div[3]/div/button").click()
                #driver.find_element_by_css_selector("button.base-unit.add-tab-goods").click()
                driver.find_element_by_css_selector("textarea.base-unit.last").clear()
                driver.find_element_by_css_selector("textarea.base-unit.last").send_keys("15682649365469765893507\n411941304218153299592925\n320565908718070678832071\n15682649365469765893507")
                driver.find_element_by_xpath("//button[@type='button']").click()
                time.sleep(1)

                #Tab4添加商品                                                                        
                Select(driver.find_element_by_xpath("//div[@id='J_content']/div/div[5]/div/div[2]/div[4]/span/select")).select_by_visible_text(u"左单行")
                driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[5]/div/div[2]/div[4]/div/button").click()
                driver.find_element_by_css_selector("textarea.base-unit.last").clear()
                driver.find_element_by_css_selector("textarea.base-unit.last").send_keys("15682649365469765893507\n411941304218153299592925\n320565908718070678832071\n15682649365469765893507")
                driver.find_element_by_xpath("//button[@type='button']").click()
                time.sleep(1)

                #保存
                driver.find_element_by_xpath("//div[@id='J_content']/div/div[6]/button").click()
        #回到列表页面        
        time.sleep(2)
        driver.switch_to_window(now_handle)
        time.sleep(2)
        
       
        specialNameCheck=driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div/span[1]").text
        try: self.assertEqual(specialNameCheck,u'S')
        except AssertionError as e: self.verificationErrors.append(str(e)+"2")   
            
    def test_003(self):
        '''
        003：专题名不能为空
        '''  
        
        self.makeSpecial()
        driver=self.driver
        #保存    
        driver.find_element_by_xpath("//div[@id='J_content']/div/div[6]/button").click()
        NameNotNulCheck=driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/span").text
        try: self.assertEqual(NameNotNulCheck,u"专题名不能为空")
        except AssertionError as e: self.verificationErrors.append(str(e)+"3")    

    def test_004(self):
        '''
        004:专题头图不能为空
        '''  
        self.makeSpecial()
        driver=self.driver
        driver.find_element_by_name("l_name").clear()
        driver.find_element_by_name("l_name").send_keys("Sue")
        time.sleep(2)
        #保存    
        driver.find_element_by_xpath("//div[@id='J_content']/div/div[6]/button").click()
        PicNotNulCheck=driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/span").text
        try: self.assertEqual(PicNotNulCheck,u"至少上传一张专题头图")
        except AssertionError as e: self.verificationErrors.append(str(e)+"4")
     
    def test_005(self):
        '''
        005:至少有一个专题Tab
        '''
        self.makeSpecial()
        driver=self.driver
        driver.find_element_by_name("l_name").clear()
        driver.find_element_by_name("l_name").send_keys("Sue")
               
        #上传图片
        js_one="var q=document.querySelector('#upload').style.display='block'"
        driver.execute_script(js_one)
        driver.find_element_by_id("upload").clear()
        driver.find_element_by_id("upload").send_keys("C:\\Users\\yangweijia\\Pictures\\jpg\\90071992647538756.jpg")
        time.sleep(5)
        #保存    
        driver.find_element_by_xpath("//div[@id='J_content']/div/div[6]/button").click()
        TabNotNulCheck=driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/span").text
        try: self.assertEqual(TabNotNulCheck,u"至少有一个专题Tab")
        except AssertionError as e: self.verificationErrors.append(str(e)+"5")
     
    def test_006(self):
        '''
        006:发布
        '''
        driver = self.driver
        driver.find_element_by_css_selector("a.data_ms.active > span").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[4]/span").click()
        time.sleep(2)
        
        driver.find_element_by_xpath("//span[5]/button").click()
        driver.find_element_by_xpath("//a[2]").click()
        time.sleep(4)
        try: self.assertNotEqual(driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div/span[2]/div").text,u"专题未发布")
        except AssertionError as e: self.verificationErrors.append(str(e)+"6")
     
    def test_007(self):
        """007:预览""" 
        driver = self.driver
        driver.find_element_by_css_selector("a.data_ms.active > span").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[4]/span").click()
        time.sleep(2)  
        
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div/span[5]/button[2]").click()
        
        previewCheck = False
        for handle in driver.window_handles:
            if driver.title != u"编辑器预览":
                pass
                time.sleep(1)
            else:  
                previewCheck = True
                
        try: self.assertNotEqual(previewCheck,True)
        except AssertionError as e: self.verificationErrors.append(str(e+"7"))
     
    def test_008(self):
        """008:编辑"""
        driver = self.driver
        driver.find_element_by_css_selector("a.data_ms.active > span").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[4]/span").click()
        time.sleep(2) 
        now_handle = driver.current_window_handle
        driver.find_element_by_xpath("//span[5]/a").click()
        time.sleep(2)
        
        #切换窗口
        for handle in driver.window_handles:
            if handle == now_handle:
                pass
                time.sleep(1)
            else:
                driver.switch_to_window(handle)
                driver.find_element_by_name("l_name").clear()
                driver.find_element_by_name("l_name").send_keys(u"编辑")
                time.sleep(2)
               # driver.find_element_by_css_selector("button.base-unit.add-tab-goods").click()
               # time.sleep(2)
               # driver.find_element_by_css_selector("textarea.base-unit.last").clear()
               # driver.find_element_by_css_selector("textarea.base-unit.last").send_keys("203226186918011068227144")
               # time.sleep(2)
               # driver.find_element_by_xpath("//button[@type='button']").click()
               # time.sleep(2)
               # goods_Num = len(driver.find_elements_by_class_name("gi-name"))
                driver.find_element_by_xpath("//div[@id='J_content']/div/div[6]/button").click()
                driver.switch_to_window(now_handle)
        
        driver.find_element_by_name("sf[search]").send_keys(u"编辑")       
        time.sleep(4)
        specialNameCheck = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div/div/span[1]").text                     
      # goodsNumCheck = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[1]/div/div/span[4]").text
        #验证专题名
        try: self.assertEqual(specialNameCheck,u'编辑')
        except AssertionError as e: self.verificationErrors.append(str(e)+"8")
        #验证商品数目
        #try: self.assertEqual(goodsNumCheck,str(goods_Num))
        #except AssertionError as e: self.verificationErrors.append(str(e)+"9")
             
    def test_009(self):
        """009:时间筛选"""  
        self.selectByTime("最近7天")
                    
    def test_010(self):
        """010:名称筛选"""
        driver = self.driver
        driver.find_element_by_css_selector("a.data_ms.active > span").click()
        time.sleep(2)
        driver.find_element_by_xpath("//a[4]/span").click()
        time.sleep(2) 
        
        driver.find_element_by_name("sf[search]").send_keys(u"11")
        driver.find_element_by_xpath("//form/div/button").click()
        #数量
        num = len(driver.find_elements_by_class_name("om_item"))
        #为0 为1 大于1
        if num == 0:
            try: self.assertEqual(driver.find_element_by_id("j_pnav_count").text,u'共0页')
            except AssertionError as e: self.verificationErrors.append(str(e))  
            
        else:
            try: self.assertEqual(driver.find_element_by_xpath("//div[2]/div[2]/div/div/span").text,u'Sue')
            except AssertionError as e: self.verificationErrors.append(str(e))  
            if num > 1:
                for i in range(2,num+1):
                    print i
                    locateStr = "//div[%s]/div/span"%i
                    try: self.assertEqual(driver.find_element_by_xpath(locateStr).text,u'Sue')
                    except AssertionError as e: self.verificationErrors.append(str(e))
                           
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    

if __name__ == "__main__":
     
    #unittest.main()
    suite = unittest.TestSuite()
    suite.addTest(NewSpecial("test_001"))
       
    #执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
        
