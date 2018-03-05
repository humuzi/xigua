# coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://sh.xsjedu.org/")
time.sleep(1)

js = "document.getElementById('doyoo_mon_inner').style.display='none'";
driver.execute_script(js)

time.sleep(1)
driver.quit()