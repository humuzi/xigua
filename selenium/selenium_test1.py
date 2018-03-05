# coding = utf-8
from selenium import  webdriver
import time

browser = webdriver.Chrome()
first_url ='http://www.zhihu.com'
browser.get(first_url)
time.sleep(2)

second_url = 'http://www.baidu.com'
browser.get(second_url)
time.sleep(2)

# 退回知乎首页
browser.back()
time.sleep(2)

# 回到百度界面
browser.forward()
time.sleep(2)
# print('浏览器最大化')
# browser.maximize_window()
# 设置浏览器窗口大小
# browser.set_window_size(1024,800)
# time.sleep(2)

# 百度输入框的id叫'kw'，在输入框输入selenium
browser.find_element_by_id('kw').send_keys('selenium')
# 搜索框的ID叫'su',点击一下搜索框
browser.find_element_by_id('su').click()
print(browser.title)
print('Now access %s'%second_url)
time.sleep(3)
browser.quit()
