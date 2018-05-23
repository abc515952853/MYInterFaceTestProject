import unittest
from HTMLTestRunner import HTMLTestRunner
from testcase import TestSendCode,TestAccount

if __name__ =='__main__':
    
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestAccount.TestAccount))
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestSendCode.TestSendCode))

    # with open('UnittestTextReport.html','wb') as f:
    #     runner = HTMLTestRunner(stream=f,title='MathFunc Test Report',description='generated by HTMLTestRunner.',verbosity=2)
    #     runner.run(suite) 
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)