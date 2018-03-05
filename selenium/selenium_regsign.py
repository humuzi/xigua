# coding=utf-8

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

# 获得当前窗口
nowhandle = driver.current_window_handle

driver.find_element_by_link_text("登录").click()
driver.implicitly_wait(10)
driver.find_element_by_class_name("tang-foreground").find_element_by_class_name("pass-reglink").click()

allhandles = driver.window_handles
for handle in allhandles:
    if  handle != nowhandle:
        driver.switch_to.window(handle)
        print("Now register window")

        driver.find_element_by_xpath("//input[@id='TANGRAM__PSP_3__userName']")
        js = "var q=document.getElementById(\"TANGRAM__PSP_3__userName\");q.style.border=\"2px solid red\";"
        driver.execute_script(js)
        time.sleep(3)
        driver.close()

time.sleep(2)
driver.quit()

