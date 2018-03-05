from selenium import webdriver
import time


browser = webdriver.Chrome()
browser.get('http://www.baidu.com')
# 通过id定位
browser.find_element_by_id('kw').send_keys('selenium')
# 通过name定位
# browser.find_element_by_name('wd').send_keys('selenium')
# 通过tag_name定位
# browser.find_element_by_tag_name('input').send_keys('selenium')
# 通过class_name定位
# browser.find_element_by_class_name('s_ipt').send_keys('selenium')
# 通过css定位
# browser.find_element_by_css_selector('#kw').send_keys('selenium')
# 通过Xpath定位
# browser.find_element_by_xpath("//input[@id='kw']").send_keys('selenium')

browser.find_element_by_id('su').click()
browser.quit()


browser =webdriver.Chrome()
browser.get('http://www.baidu.com')
time.sleep(2)
browser.find_element_by_link_text('贴吧').click()
time.sleep(2)
browser.quit()