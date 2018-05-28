import unittest
import ddt
from common import ReadExcl
import ReadConfig 
import requests
import  json 

class TestHome(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print ("TestHome Start")
    
    @classmethod
    def tearDownClass(cls):
        print("TestHome Stop")

    def test_Account(self):
        readconfig=ReadConfig.ReadConfig()
        headers = {"Content-Type":"application/json","Authorization":readconfig.get_member("session")} 
        r = requests.get(url='http://api.hhx.qianjifang.com.cn/api/Home',headers = headers)
        self.assertEqual(200,r.status_code)