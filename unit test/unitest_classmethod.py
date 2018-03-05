# coding = utf-8
import unittest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

class BlogHome(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        url = "http://www.cnblogs.com/yoyoketang/"
        cls.driver.get(url)
        cls.driver.implicitly_wait(30)

    def test_01(self):
        locator = ("id","blog_nav_sitehome")
        text = u"博客园"
        result= EC.text_to_be_present_in_element(locator,text)(self.driver)
        self.assertTrue(result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(BlogHome("test_01"))
    #
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    unittest.main()
