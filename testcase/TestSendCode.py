import unittest
import ddt
from common import ReadExcl
import requests
import  json 


excel = ReadExcl.Xlrd()

@ddt.ddt
class TestSendCode(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print ("start")

    @classmethod
    def tearDownClass(cls):
        print ("stop")

    @ddt.data(*excel.get_xls_next())
    def test_Sencode(self, data):
        payload = {"phone":int(data['phone']),"type":int(data['type'])}
        print(payload)
        headers = {"Content-Type":"application/json"}
        r = requests.post(url='http://api.hhx.qianjifang.com.cn/api/Account/SendCode',data = json.dumps(payload),headers = headers)
        self.assertEqual(data['code'],r.status_code)