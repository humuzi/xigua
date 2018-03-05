# coding = utf-8
from selenium import webdriver
import unittest
import ddt
import time

testdata =[{u'username': u'python\u7fa4', u'password': u'226296743'},
           {u'username': u'selenium\u7fa4', u'password': u'232607095'},
           {u'username': u'胡木子爱吃西瓜', u'password': u'hqy945688'}]
@ddt.ddt
class Blog(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        url = "https://passport.cnblogs.com/user/signin"
        self.driver.get(url)
        self.driver.implicitly_wait(30)

    def login(self,username,psw):
        self.driver.find_element_by_id("input1").send_keys(username)
        self.driver.find_element_by_id("input2").send_keys(psw)
        self.driver.find_element_by_id("signin").click()
        time.sleep(3)

    def is_login_success(self):
    # 判断是否取到登录账户名称
        try:
            text = self.driver.find_element_by_id("lnk_current_user").text
            print(text)
            return True
        except:
            return False
    #
    # def test_01(self):
    #     self.login(u'胡木子爱吃西瓜',"hqy945688")
    #     result = self.is_login_success()
    #     self.assertTrue(result)
    @ddt.data(*testdata)
    def test_01(self,data):
        print("当前测试数据%s"%data)
        try:
            self.login(data["username"],data["pwd"])
            text = self.driver.find_element_by_id("lnk_current_user").text
            print(text)
            self.assertEqual(text,data["username"])
        except Exception as msg:
            print(u"异常原因%s"%msg)
            nowtime =time.strftime("%Y%m%d.%H.%M.%S")
            self.driver.get_screenshot_as_file("./%s.png"%nowtime)
            raise
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(Blog("test_01"))

    runner = unittest.TextTestRunner()
    runner.run(suite)


