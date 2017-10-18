# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.remote.webelement import WebElement

class OldSpecial(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://admin.codoon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_old_special(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/html/dms/data-tpl-ms.html")
        driver.find_element_by_name("login[name]").clear()
        driver.find_element_by_name("login[name]").send_keys("Oper")
        driver.find_element_by_name("login[pwd]").clear()
        driver.find_element_by_name("login[pwd]").send_keys("Oper")
        driver.find_element_by_css_selector("button.llv-submit").click()
        '''
        driver.find_element_by_name("sf[search]").clear()
        driver.find_element_by_name("sf[search]").send_keys(u"三方专题")
        driver.find_element_by_css_selector("div.sf-search.clearfix > button.btn.btn-default").click()
        driver.find_element_by_xpath("//div[@id='m_78819039718154619058130']/span[6]/button[4]").click()
        driver.find_element_by_name("name").clear()
        driver.find_element_by_name("name").send_keys(u"旧版专题001")
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_link_text(u"确认").click()
        time.sleep(5)
        '''
        driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[2]/div[9]/div/span[6]/button[3]").click()
        time.sleep(2)
        driver.find_element_by_css_selector("li.active").click()
        time.sleep(2)
        
        driver.find_element_by_name("itemid").clear()
        driver.find_element_by_name("itemid").send_keys("33242735418327574408108")
        time.sleep(1)
                
       #js_string="var q=document.getElementsByClassName('base-unit').style.display='block'; "
        jsone="var dom=document.querySelectorAll('input.base-unit[type=file]');i=0;while(dom[i]){dom[i].style.visibility='visible';dom[i].style.height='1px';dom[i].style.width='1px';i++};"
        driver.execute_script(jsone)
        time.sleep(5)
        driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div[2]/div/form/div[2]/input[2]").clear()
        driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div[2]/div/form/div[2]/input[2]").send_keys("C:\Users\yangweijia\Pictures\jpg\rose.jpg")
        time.sleep(3)
        
        driver.find_element_by_name("desc").clear()
        driver.find_element_by_name("desc").send_keys(u"描述")
        time.sleep(1)
        driver.find_element_by_name("title").clear()
        driver.find_element_by_name("title").send_keys(u"标题")
        time.sleep(1)
        
        driver.find_element_by_xpath("(//button[@type='button'])[7]").click()
        time.sleep(5)
        driver.find_element_by_xpath("(//input[@name='itemid'])[2]").clear()
        driver.find_element_by_xpath("(//input[@name='itemid'])[2]").send_keys("33242735418327574408108")
        driver.execute_script(jsone)
        driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div[2]/div/form[2]/div[2]/input[2]").send_keys("C:\Users\yangweijia\Pictures\jpg\rose.jpg")
        driver.find_element_by_xpath("(//input[@name='desc'])[2]").clear()
        driver.find_element_by_xpath("(//input[@name='desc'])[2]").send_keys("1")
        driver.find_element_by_xpath("(//input[@name='title'])[2]").clear()
        driver.find_element_by_xpath("(//input[@name='title'])[2]").send_keys("1")
        
        driver.find_element_by_xpath("(//button[@type='button'])[12]").click()
        driver.find_element_by_xpath("(//input[@name='itemid'])[2]").clear()
        driver.find_element_by_xpath("(//input[@name='itemid'])[2]").send_keys("33242735418327574408108")
        driver.execute_script(jsone)
        driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div[2]/div/form[3]/div[2]/input[2]").send_keys("C:\Users\yangweijia\Pictures\jpg\rose.jpg")
        driver.find_element_by_xpath("(//input[@name='desc'])[2]").clear()
        driver.find_element_by_xpath("(//input[@name='desc'])[2]").send_keys("1")
        driver.find_element_by_xpath("(//input[@name='title'])[2]").clear()
        driver.find_element_by_xpath("(//input[@name='title'])[2]").send_keys("1")
        
        driver.find_element_by_xpath("(//button[@type='button'])[17]").click() 
        driver.find_element_by_xpath("(//input[@name='itemid'])[2]").clear()
        driver.find_element_by_xpath("(//input[@name='itemid'])[2]").send_keys("33242735418327574408108")
        driver.execute_script(jsone)
        driver.find_element_by_xpath("/html/body/div[5]/div[2]/div/div[2]/div/form[3]/div[2]/input[2]").send_keys("C:\Users\yangweijia\Pictures\jpg\rose.jpg")
        driver.find_element_by_xpath("(//input[@name='desc'])[2]").clear()
        driver.find_element_by_xpath("(//input[@name='desc'])[2]").send_keys("1")
        driver.find_element_by_xpath("(//input[@name='title'])[2]").clear()
        driver.find_element_by_xpath("(//input[@name='title'])[2]").send_keys("1")
        
        #保存草稿
        driver.find_element_by_xpath("(//button[@type='button'])[23]").click()
        #发布
        driver.find_element_by_css_selector("span.cell-9.operates > button.btn.btn-default").click()
        driver.find_element_by_link_text(u"确认").click()
        driver.find_element_by_xpath("//div[@id='m_174031893910314373752660']/span[6]/button[3]").click()
        driver.find_element_by_css_selector("li.active").click()
        driver.find_element_by_xpath("(//button[@type='button'])[157]").click()
        driver.find_element_by_xpath("(//input[@name='url'])[2]").clear()
        driver.find_element_by_xpath("(//input[@name='url'])[2]").send_keys("https://xmall.codoon.com/channel/html/cdetail.html?h_da=chann_1456111794652")
        driver.find_element_by_xpath("(//input[@name='title'])[2]").clear()
        driver.find_element_by_xpath("(//input[@name='title'])[2]").send_keys(u"旧版专题旧版专题")
        driver.find_element_by_xpath("(//button[@type='button'])[7]").click()
        driver.find_element_by_xpath("(//input[@type='file'])[2]").clear()
        driver.find_element_by_xpath("(//input[@type='file'])[2]").send_keys("")
        driver.find_element_by_xpath("(//button[@type='button'])[163]").click()
        driver.find_element_by_css_selector("span.cell-9.operates > button.btn.btn-default").click()
        driver.find_element_by_link_text(u"确认").click()
        
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
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
