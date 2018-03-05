# coding=utf-8
from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.get("http://www.baidu.com")

js = 'document.getElementsByClassName("mnav")[0].target="";'
driver.execute_script(js)

driver.find_element_by_link_text("新闻").click()
time.sleep(2)

driver.quit()