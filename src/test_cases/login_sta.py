from time import sleep
import unittest,sys
from msilib.schema import SelfReg
sys.path.append("./models")
sys.path.append("./page_obj")
from models import myunit
from models.myunit import MyTest
from page_obj.loginPage import loginPage


class loginTest(MyTest):

    def test_login001(self):
        print"test_login001"
    
    def test_login002(self):
        print"test_login001"
        
if __name__ == "__main__":
    unittest.main()