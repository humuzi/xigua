from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import os,time

browser = webdriver.Chrome()
browser.get('http://mail.163.com/')
browser.implicitly_wait(30)

# 方法一：直接定位框架名称
browser.switch_to.frame("x-URS-iframe")
# 方法二：通过tag标签定位iframe
# iframe = browser.find_element_by_tag_name('iframe')
# browser.switch_to.frame(iframe)
# frame = browser.find_element_by_id("lbNormal")
# js = ActionChains(browser).move_to_element(frame).perform()
# browser.execute_script(js)
browser.find_element_by_name("email").send_keys('huqiuyueya')
browser.find_element_by_name('password').send_keys('hqy945688')
browser.find_element_by_name('password').send_keys(Keys.ENTER)
time.sleep(3)

browser.quit()

# browser = webdriver.Chrome()
# browser.get('http://www.baidu.com')
#
# browser.find_element_by_id('kw').send_keys('selenium')
# browser.find_element_by_id('su').click()
# time.sleep(2)
#
# browser.find_element_by_id('kw').send_keys(Keys.CONTROL,'a')
# time.sleep(2)
#
# browser.find_element_by_id('kw').send_keys(Keys.CONTROL,'x')
# time.sleep(2)
#
# browser.find_element_by_id('kw').send_keys(u'虫师 cnblogs')
# browser.find_element_by_id('su').click()
# time.sleep(2)
#
# browser.quit()

