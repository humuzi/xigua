# coding=utf-8
from selenium import webdriver
import unittest
import time

class Testa(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()

    def setUp(self):
        self.driver.get("https://www.cnblogs.com/yoyoketang/")

    def test_01(self):
        t = self.driver.title
        print(t)
        self.assertIn(u"悠悠",t)

    def test_02(self):
        t = self.driver.title
        print(t)
        self.assertIn(u"youyou",t)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()
