from selenium import webdriver
import os,time

def insert_img(driver,file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)  
    base_dir = base_dir.replace('\\', '/')
    base = base_dir.split('/test_case')[0]
    file_path = base+"/report/image/"+file_name
    driver.get_screenshot_as_file(file_path)
    
if __name__=='__main__':
    driver = webdriver.Chrome()
    driver.get("https://admin.codoon.com/admin/html/index.html")
    time.sleep(5)
    insert_img(driver, "login.jpg")
    time.sleep(5)
    driver.quit()
                          
    
    