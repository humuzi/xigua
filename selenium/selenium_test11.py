#  -*- coding=utf-8 -*-
from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get('https://www.youdao.com/')

# 获得cookie信息
cookies = browser.get_cookies()
print(cookies)

browser.add_cookie({'name':'humuzi','value':'18'})

for cookie in browser.get_cookies():
    print('%s -> %s'%(cookie['name'],cookie['value']))

n=browser.delete_cookie('CookieName')
print(n)
browser.delete_all_cookies()

time.sleep(2)
browser.close()


# browser=webdriver.Chrome()
# browser.get('http://passport.cnblogs.com/login.aspx?ReturnUrl=http://www.cnblogs.com/fnng/admin/EditPosts.aspx')
# time.sleep(3)
# browser.maximize_window()
#
# browser.find_element_by_xpath("//input[@id='input1']").send_keys('fnngj')
# browser.find_element_by_xpath("//input[@id='input2']").send_keys('123456')
#
# browser.find_element_by_xpath("//input[@id='remember_me']").click()
# time.sleep(2)
#
# browser.find_element_by_xpath("//input[@id='signin']").click()
#
# cookie = browser.get_cookies()
# print(cookie)
#
# time.sleep(2)
# browser.close()
