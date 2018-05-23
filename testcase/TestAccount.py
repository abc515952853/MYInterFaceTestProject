import unittest
import ddt
from common import ReadExcl
import ReadConfig 
import requests
import  json 

readconfig=ReadConfig.ReadConfig()

class TestAccount(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print ("TestAccount Start")
    
    @classmethod
    def tearDownClass(cls):
        print("TestAccoun Stop")

    def test_Account(self):
        r = requests.get(url='http://api.hhx.qianjifang.com.cn/api/Account')
        if r.status_code == 200:
            readconfig.set_member('mrename',r.json())
            readconfig.write()
        self.assertEqual(200,r.status_code)
