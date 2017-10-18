# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.remote.webelement import WebElement

class NewGoods(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://admin.codoon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_new_goods(self):
        driver = self.driver
        driver.get(self.base_url + "/admin/html/item-creator-test.html#!new")
        driver.maximize_window() 
        driver.find_element_by_name("login[name]").clear()
        driver.find_element_by_name("login[name]").send_keys("test123")
        driver.find_element_by_name("login[pwd]").clear()
        driver.find_element_by_name("login[pwd]").send_keys("Test123456")
        driver.find_element_by_css_selector("button.llv-submit").click()
        time.sleep(5)
        
#        #driver.find_element_by_css_selector("a.goods_ms. > span").click()
#         driver.find_element_by_xpath("//a[3]/span").click()
#         time.sleep(2)
#        #driver.find_element_by_css_selector("a.sku_ms. > span").click()
#         driver.find_element_by_xpath("//div[2]/a[2]/span").click()
#         time.sleep(2)
#         
#         driver.find_element_by_css_selector("a.pcommon-setting-margin.new-sku > button.btn.btn-success").click()
#         
#         #商品长名称
#         driver.find_element_by_css_selector("textarea.base-unit.pgoods-setting-long-name").clear()
#         driver.find_element_by_css_selector("textarea.base-unit.pgoods-setting-long-name").send_keys(u"�����������������������")
#         
#         #商品短名称
#         driver.find_element_by_css_selector("textarea.base-unit.pgoods-setting-short-name").clear()
#         driver.find_element_by_css_selector("textarea.base-unit.pgoods-setting-short-name").send_keys(u"�óԺóԺóԺóԺóԺóԺóԺóԺóԺó�")
#         
#         #sku单价
#         driver.find_element_by_css_selector("input.unit_price.base-unit").clear()
#         driver.find_element_by_css_selector("input.unit_price.base-unit").send_keys("12")
#         
#         #邮费
#         driver.find_element_by_css_selector("input.mail_fee.base-unit").clear()
#         driver.find_element_by_css_selector("input.mail_fee.base-unit").send_keys("10")
#         
#         #添加属性
#         driver.find_element_by_xpath("//button").click()
#         
#         #属性名称
#         driver.find_element_by_name("attr").clear()
#         driver.find_element_by_name("attr").send_keys(u"ζ��")
#         #属性描述
#         driver.find_element_by_name("desc").clear()
#         driver.find_element_by_name("desc").send_keys(u"����")
#         #确认
#         driver.find_element_by_xpath("//button[@type='button']").click()
#         '''
#         #添加属性
#         driver.find_element_by_xpath("//button").click()
#         #属性名称
#         driver.find_element_by_name("attr").clear()
#         driver.find_element_by_name("attr").send_keys(u"ζ��")
#         time.sleep(5)
#         #属性描述
#         driver.find_element_by_name("desc").clear()
#         #driver.find_element_by_name("desc").send_keys(u"�춹")
#         time.sleep(5)
#         driver.find_element_by_xpath("//form/input[2]").send_keys(u"�춹")
#         #确认
#         time.sleep(3)
#        #driver.find_element_by_xpath("//button[@type='button']").click()
#         driver.find_element_by_xpath("/html/body/div[3]/div/form/div/button").click()
# 
#         
#         driver.find_element_by_xpath("//button").click()
#         driver.find_element_by_name("attr").clear()
#         driver.find_element_by_name("attr").send_keys(u"ζ��")
#         driver.find_element_by_name("desc").clear()
#         driver.find_element_by_name("desc").send_keys(u"����")
#         time.sleep(3)
#         driver.find_element_by_xpath("//button[@type='button']").click()
#         '''
#         driver.find_element_by_name("third_party_sku").clear()
#         driver.find_element_by_name("third_party_sku").send_keys("0101")
#         driver.find_element_by_name("settle_account_type").click()
#         Select(driver.find_element_by_id("settle_account_suppliers")).select_by_visible_text("CCC")
#         driver.find_element_by_name("sku_cost_money").clear()
#         driver.find_element_by_name("sku_cost_money").send_keys("9")
#         driver.find_element_by_xpath("//div[13]/button").click()
#         time.sleep(15)
#         
#         skuid=driver.find_element_by_xpath("/html/body/div[1]/div/table/tbody/tr[2]/td[4]").text
#         print(skuid)
#         
#         time.sleep(5)
#         driver.find_element_by_css_selector("a.goods_ms.active > span").click()
#         driver.find_element_by_css_selector("a.item_ms.active > span").click()
#         driver.find_element_by_css_selector("a.pcommon-setting-margin.new-goods-btn > button.btn.btn-success").click()
#         driver.find_element_by_xpath("/html/body/div[1]/div/button[1]").click()
#       # driver.find_element_by_xpath("//button").click()
#         driver.find_element_by_name("sku_id").clear()
#         driver.find_element_by_name("sku_id").send_keys(skuid)
#         time.sleep(5)
#         driver.find_element_by_xpath("//button[@type='button']").click()
#         driver.find_element_by_css_selector("textarea.pgoods-setting-long-name.base-unit").clear()
#         driver.find_element_by_css_selector("textarea.pgoods-setting-long-name.base-unit").send_keys(u"�������")
#         driver.find_element_by_css_selector("textarea.base-unit.pgoods-setting-short-name").clear()
#         driver.find_element_by_css_selector("textarea.base-unit.pgoods-setting-short-name").send_keys(u"��������")
#         driver.find_element_by_xpath("(//textarea[@id=''])[3]").clear()
#         driver.find_element_by_xpath("(//textarea[@id=''])[3]").send_keys("10")
#         driver.find_element_by_xpath("(//textarea[@id=''])[4]").clear()
#         driver.find_element_by_xpath("(//textarea[@id=''])[4]").send_keys("20")
#         
#         driver.find_element_by_css_selector("input.base-unit").clear()
#         driver.find_element_by_css_selector("input.base-unit").send_keys(u"ѡ��ζ��")
#         time.sleep(5)
#         
#         #上传图片
#         #driver.find_element_by_xpath("//button[2]").click()
#         #driver.find_element_by_id("upload").clear()
#         #driver.find_element_by_id("upload").send_keys("C:\\Users\\yangweijia\\Pictures\\jpg\\6619393151235890154.jpg")
#         
#         #js_string="var q=document.getElementById('upload').style.display='block'; "
#         #jsone="var q=document.querySelectorAll('.pic')"
#         js_string="var q=document.querySelectorAll('input');i=0;while(q[i]){q[i].style.display='block'}"
#         driver.execute_script(js_string)
#         driver.find_element_by_id("upload").send_keys("C:\\Users\\yangweijia\\Pictures\\jpg\\6619393151235890154.jpg")
#         
        
        GoodsInfoWindown=driver.current_window_handle
        print GoodsInfoWindown
        driver.find_element_by_link_text(u"编辑").click()
        time.sleep(2)
        
        for handle in driver.window_handles:
            if handle !=GoodsInfoWindown:  
                driver.switch_to_window(handle)
                driver.switch_to_frame(driver.find_element_by_xpath("//div[6]/div/div/div/div/iframe"))
                driver.find_element_by_xpath("/html/body/div/form/input").send_keys(u"C:\\Users\\yangweijia\\Pictures\\jpg\\6619393151235890154.jpg")
                time.sleep(2)
                driver.switch_to_default_content()
                driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/button")
                driver.close()
                time.sleep(5)
                
                
        driver.switch_to_window(GoodsInfoWindown)
        driver.find_element_by_name("l_name").send_keys(u"�����������������������")
        driver.find_element_by_css_selector("textarea.base-unit.pgoods-setting-long-name").clear()
        driver.find_element_by_css_selector("textarea.base-unit.pgoods-setting-long-name").send_keys(u"�����������������������")
        driver.find_element_by_xpath("/html/body/div[1]/div/div[13]/button[1]").click()
        time.sleep(5)
       #driver.find_element_by_css_selector("a.inventory_ms.active > span").click()
        driver.find_element_by_xpath("//a[2]/span").click()
       #driver.find_element_by_link_text(u"要邮寄SKU库存").click()
        driver.find_element_by_xpath("//div[2]/a").click()
        
        driver.find_element_by_xpath("//table[@id='j-stock-main']/tbody/tr/td[12]/button").click()
        driver.find_element_by_name("num").clear()
        driver.find_element_by_name("num").send_keys("100")
        driver.find_element_by_xpath("//button[@type='button']").click()
        #商品管理
        #driver.find_element_by_link_text(u"��Ʒ����").click()
        driver.find_element_by_xpath("//a[3]/span").click()
        driver.find_element_by_css_selector("a.item_ms.active > span").click()
        time.ctime(2)
        #driver.find_element_by_xpath("//tr[@id='gi_296635977318686241472131']/td[13]/a/button").click()
        driver.find_element_by_xpath("/html/body/div[1]/div/table/tbody/tr[1]/td[13]/a[1]/button").click()
        time.sleep(3)
        driver.find_element_by_xpath("//button[2]").click()
        time.sleep(1)
        driver.find_element_by_name("update_count").clear()
        driver.find_element_by_name("update_count").send_keys("50")
        driver.find_element_by_xpath("//button[@type='button']").click()
        driver.find_element_by_xpath("//div[13]/button").click()
        time.sleep(5)
        #driver.find_element_by_css_selector("a.goods_ms.active > span").click()
        driver.find_element_by_xpath("/html/body/div[5]/div[1]/div[2]/div[3]/a[3]/span").click()
        time.sleep(1)
        driver.find_element_by_css_selector("a.item_ms.active > span").click()
        time.sleep(1)
        #driver.find_element_by_xpath("//tr[@id='gi_296635977318686241472131']/td[13]/button").click()
        driver.find_element_by_xpath("/html/body/div[1]/div/table/tbody/tr[1]/td[13]/button").click()
        
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
