# coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

# options = webdriver.ChromeOptions()
# options.add_argument('headless')
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium")
driver.find_element_by_id("su").click()
driver.implicitly_wait(30)

all = driver.find_elements_by_xpath("//div['@id=content_left']/div/h3/a")
s = len(all)
print("获得总个数：%s"%s)

for i in range(s):
    all[i].click()
    time.sleep(2)
    url = driver.current_url
    print("当期那页面url为：%s"%url)
    handle = driver.current_window_handle  #获得当前窗口的句柄
    handles = driver.window_handles    #获得所有窗口句柄
    for newhandle in handles:
        if newhandle != handle:
            driver.switch_to.window(newhandle)   #切换至当前窗口
            driver.close()    #关闭当前窗口
    driver.switch_to.window(handles[0])    #切换回跳转之前的窗口
    # 重新获取一次元素
    all = driver.find_elements_by_xpath("//div['@id=content_left']/div/h3/a")

driver.quit()