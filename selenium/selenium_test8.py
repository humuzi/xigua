# coding=utf-8
from selenium import webdriver
import os,time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC

# browser = webdriver.Chrome()
# file_path = 'file:///'+ os.path.abspath('drop_down.html')
# browser.get(file_path)
# time.sleep(3)
#
# m = browser.find_element_by_id('ShippingMethod')
# m.find_element_by_xpath('//option[@value="10.69"]').click()
# time.sleep(3)
#
# browser.quit()


browser=webdriver.Chrome()
browser.get('http://www.baidu.com')

# 定位搜索设置：
# 法一：
# browser.find_elements_by_name('tj_settingicon').pop().click()
# browser.find_element_by_link_text('搜索设置').click()
# time.sleep(3)

# 方法二：建立动作链
chain = ActionChains(browser)
link = browser.find_element_by_link_text('设置')   #定位设置
chain.move_to_element(link).perform()    #执行
browser.implicitly_wait(30)
browser.find_element_by_link_text('搜索设置').click()
time.sleep(3)

# 法一:
# m = browser.find_element_by_name('NR')
# m.find_element_by_xpath('//option[@value="50"]').click()
# time.sleep(2)

# browser.find_element_by_xpath('//a[@class="prefpanelgo"]').click()
# time.sleep(3)
# browser.switch_to.alert.accept()

# 法二：通过select选择
s = browser.find_element("name","NR")
Select(s).select_by_visible_text(u"每页显示50条")

js = 'document.getElementsByClassName("prefpanelgo")[0].click();'
browser.execute_script(js)
# 判断弹窗结果
result = EC.alert_is_present()(browser)
if result:
    print(result.text)
    result.accept()
else:
    print("alert未弹出")
# browser.switch_to.alert.accept()

browser.find_element_by_id('kw').send_keys('selenium')
browser.find_element_by_id('su').click()
time.sleep(3)

browser.quit()