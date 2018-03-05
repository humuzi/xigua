# coding = utf-8

from selenium import webdriver
import time,os


# 登录知乎并使用户名输入框标红
browser = webdriver.Chrome()
browser.get('https://www.zhihu.com/#signin')
browser.find_element_by_class_name('signin-switch-password').click()

js = "var q=document.getElementsByName(\"account\")[0];q.style.border=\"1px solid red\";"
browser.execute_script(js)
time.sleep(3)

browser.find_element_by_name('account').send_keys('18267148256')
browser.find_element_by_name('password').send_keys('1992814512')
browser.find_element_by_class_name('sign-button submit').click()
time.sleep(3)

browser.quit()


# 通过JS隐藏选中的元素
driver = webdriver.Chrome()
file_path = 'file:///'+os.path.abspath('js.html')
driver.get(file_path)

# 方法一：
driver.execute_script('$("#tooltip").fadeOut();')
time.sleep(5)

# 方法二：
button = driver.find_element_by_class_name('btn')
driver.execute_script('$(arguments[0]).fadeOut()',button)
time.sleep(5)
driver.quit()


