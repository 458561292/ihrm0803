import unittest
from case.TestUser import TestUserLogin
from case.TestEmployee import TestEmployee
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
suite.addTest(TestUserLogin("test_login_success"))
suite.addTest(unittest.makeSuite(TestEmployee))

# runner = unittest.TextTestRunner()
# runner.run(suite)

with open("./report/report.html", "wb") as f:
    runner = HTMLTestRunner(f, title="我的测试报告", description="版本 v1.0")
    runner.run(suite)
