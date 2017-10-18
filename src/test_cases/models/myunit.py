# -*- coding: utf-8 -*-
from selenium import webdriver
from star import  brower
import unittest
import os

class MyTest(unittest.TestCase):
    thirdBoss='thirdBoss'
    subThirdBoss="subThirdBoss"
    thirdManage="thirdManage"
    thirdOper="thirdOper"
    selfBoss="selfBoss"
    selfManage="selfManage"
    selfOper="selfOper"
    oper="oper"
    superDev="superDev"
    service="service"
    
    def setUp(self):
        print "setup"
        self.verificationErrors = []
        self.driver = brower()
        self.driver.maximize_window() 
        print "myunit"
        
    def tearDown(self):
        print "quit"
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        