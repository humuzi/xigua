# coding=utf-8
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://mail.163.com")
first_cookie = driver.get_cookies()
print(first_cookie)

driver.switch_to.frame("x-URS-iframe")
driver.find_element_by_xpath("//input[@name='email']").send_keys("huqiuyueya")
driver.find_element_by_xpath("//input[@name='password']").send_keys("hqy945688")
driver.find_element_by_id("dologin").click()
driver.implicitly_wait(30)
second_cookie = driver.get_cookies()
print(second_cookie)