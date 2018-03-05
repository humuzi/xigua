# coding = utf-8
import unittest
from selenium import webdriver

class ElementTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://www.baidu.com")
        cls.driver.implicitly_wait(30)

    def test_element_exist(self):
        self.css = self.get_element_by_key(1)
        self.css = self.driver.find_elements_by_css_selector(css_selector=self.css)
        if len(s)==0:
            print("元素未找到%s"%self.css)
            return False
        elif len(s)==1:
            return True
        else:
            print("找到%s个元素%s"%(len(s),self.css))
            return False

    def get_element_by_key(self,type):
        if type == 1:
            return self.driver.find_element_by_id("kw").send_keys("yoyoketang")
        elif type == 2:
            return self.driver.find_element_by_id("kw").send_keys("yoyoketang")
        elif type == 3:
            return self.driver.find_element_by_id("xxx").send_keys("yoyoketang")



    # def test_is_element_exist(self,css):
    #     try:
    #         self.driver.find_element_by_css_selector(css)
    #         return True
    #     except:
    #         return False


    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()

