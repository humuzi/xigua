# coding = utf-8

from selenium import webdriver
import time
import os

browser = webdriver.Chrome()
file_path = 'file:///'+os.path.abspath('frame.html')
browser.get(file_path)

browser.implicitly_wait(30)
# 先找到id为f1的iframe
browser.switch_to.frame('f1')
# 再找到id为f2的iframe
browser.switch_to.frame('f2')

browser.find_element_by_id('kw').send_keys('selenium')
browser.find_element_by_id('su').click()
time.sleep(2)

browser.quit()

