# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import os

dr = webdriver.Chrome()
file_path = 'file:///'+os.path.abspath('checkbox.html')
dr.get(file_path)

# 通过tag_name定位
# inputs = dr.find_elements_by_tag_name('input')
# for input in inputs:
#     if input.get_attribute('type') == 'checkbox':
#         input.click()
# time.sleep(2)
# dr.quit()

# 通过CSS得方法定位
checkboxs = dr.find_elements_by_css_selector("input[type='checkbox']")
for checkbox in checkboxs:
    checkbox.click()
time.sleep(2)

# 去除最后一个勾
dr.find_elements_by_css_selector("input[type='checkbox']").pop().click()    #pop()用于删除并返回最后一个元素
time.sleep(2)
dr.quit()
