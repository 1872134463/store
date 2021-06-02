from ddt import ddt
from ddt import data
from ddt import unpack
from selenium import webdriver
from InitPage import InitPageData
from LoginOpera import LoginPage
import unittest
import time
@ddt
class LoginTest(unittest.TestCase):
    def setUp(self) -> None:
       self.driver = webdriver.Chrome()
       self.driver.get("http://www.jasonisoft.cn:8080/HKR/")
    def tearDown(self) -> None:
       time.sleep(2)
       self.driver.quit()
    #登录成功测试用例
    @data(*InitPageData.success_data)
    def test_success_login(self,testdata):
       #创建页面操作逻辑对象
       login = LoginPage(self.driver)
       #执行登录逻辑
       login.login(testdata["username"],testdata["password"])
       #获取实际结果
       result = login.get_success_login()
       #把期望结果提取出来
       expect = testdata["expect"]
       # 断言
       self.assertEqual(expect,result)
#登录成功测试用例
    @data(*InitPageData.password_error_data)
    def test_error_login(self,testdata):
        #创建页面操作逻辑对象
        login = LoginPage(self.driver)
        #执行登录逻辑
        login.login(testdata["username"],testdata["password"])
        #获取实际结果
        result = login.get_error_password_login()
        #把期望结果提取出来
        expect = testdata["expect"]
        # 断言
        self.assertEqual(expect,result)

