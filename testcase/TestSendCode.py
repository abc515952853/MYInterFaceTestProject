import unittest
import ddt
from common import ReadExcl
import ReadConfig 
import requests
import  json 

sheet_name = "SendCode"

excel = ReadExcl.Xlrd()
readconfig=ReadConfig.ReadConfig()

@ddt.ddt
class TestSendCode(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print ("TestSendCode start")

    @classmethod
    def tearDownClass(cls):
        print("TestSendCode stop")

    @ddt.data(*excel.get_xls_next(sheet_name))
    def test_Sencode(self, data):
        payload = {"phone":str(data["phone"]),"type":int(data['type'])}
        headers = {"Content-Type":"application/json"}
        r = requests.post(url='http://api.hhx.qianjifang.com.cn/api/Account/SendCode',data = json.dumps(payload),headers = headers)
        # print(data["case_id"],r.status_code,r.text)
        excel.file.sheet_by_name(sheet_name).put_cell(data["case_id"],8,1,r.text,0)
        # excel.put_cell(data["case_id"],8,1,r.status_code,0)
        if r.status_code==204:
            readconfig.set_member('phone',str(data['phone']))
            readconfig.write()
            # print(excel.get_sheet_colname(sheet_name)['result_msg'])
        self.assertEqual(data['code'],r.status_code)
