# -*- coding: utf-8 -*-
import selenium,time
class Page(object):
    codoon_url = "https://admin.codoon.com/admin/html/index.html"
    
    def __init__(self,selenium_driver,base_url=codoon_url):
        print "base"
        self.base_url = base_url
        self.driver = selenium_driver
    
    def _open(self,url):
        print "open"
        self.driver.get(url)
        print "openover"
        time.sleep(2)
        
    #定位元素  
    def find_element(self,*loc):
        return self.driver.find_element(*loc)
    
    def find_elements(self,*loc):
        return self.driver.find_elements(*loc)
          
    #调用Javascript    
    def script(self,src):
        return self.driver.execute_script(src)   
    
    #退出登录
    def logout(self):
        js_one = "document.querySelector('.logout').click();"
        self.script(js_one)
        time.sleep(2)
      
        
        

        