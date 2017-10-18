# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from Basis import Basis

class Table(Basis):
    def __init__(self, path,start):
        self.path = path 
        self.start = start     
       
    def table_cell(self,row,column):
        print "Table"
        driver = Basis.driver
        row = row+self.start-1
        xpath = self.path +"/tr[%s]/td[%s]"%(row, column)
        return driver.find_element_by_xpath(xpath).text
    
    
    
    
    
    