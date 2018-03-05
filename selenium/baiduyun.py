# coding = utf-8

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import unittest,time

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "https://pan.baidu.com/"
        self.verificationErrors = []
        self.accept_next_alert =True

    def test_login(self):
        driver = self.driver
        driver.get(self.base_url)
        # driver.maximize_window()

        driver.add_cookie({"name":"BAIDUID","value":"B5A37A795A7C71BCC5F5DF72BD714CB8:FG=1"})
        driver.add_cookie({"name":"BDUSS","value":"B5fnNCTVZCcU9HSFp-djB6Sm5ENmpyTXhVNFZFelJ1fmZ2WFFjWVBMYzN2bFZhQVFBQUFBJCQAAAAAAAAAAAEAAABadut7uvrEvtfTsK6z1M73uc8AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADcxLlo3MS5ac1"})
        driver.refresh()
        time.sleep(3)

        cookies = driver.get_cookies()
        print(cookies)
        for cookie in driver.get_cookies():
            print("%s->%s"%(cookie["name"],cookie["value"]))

        username = driver.find_element_by_class_name("user-name").text
        print(username)

        # driver.find_element_by_xpath("//a[#class='vs03KA']").click()
        # time.sleep(3)


        # chain = driver.find_element_by_link_text(u"设置")
        # ActionChains(driver).move_to_element(chain).perform()
        # driver.find_element_by_link_text(u"搜索设置").click()
        # time.sleep(2)


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)

if __name__ == '__main__':
    unittest.TestCase()







