# -*- coding:utf-8 -*-
import time
from selenium import webdriver

options = webdriver.ChromeOptions()
pref = {"profile.default_content_settings.popups":0,"download.default_directory":"D:\\PythonProject\\selenium"}
options.add_experimental_option("prefs",pref)

driver = webdriver.Chrome()
driver.get("http://sahitest.com/demo/saveAs.htm")
driver.find_element_by_link_text("testsaveas.zip").click()
time.sleep(3)
driver.quit()