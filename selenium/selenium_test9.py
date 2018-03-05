from selenium import webdriver
import os,time

browser = webdriver.Chrome()
browser.get("http://www.baidu.com")

browser.find_element_by_id("kw").send_keys('selenium')
browser.find_element_by_id('su').click()
time.sleep(2)

js = "var q=document.documentElement.scrollTop=10000"
browser.execute_script(js)
time.sleep(3)

js ="var q=document.documentElement.scrollTop=0"
browser.execute_script(js)
time.sleep(3)

browser.quit()