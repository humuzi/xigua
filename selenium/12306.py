# coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://kyfw.12306.cn/otn/index/init")
driver.implicitly_wait(30)
def delete_readonly():
    driver.find_element_by_id("fromStationText").clear()
    driver.find_element_by_id("fromStationText").send_keys("杭州东")
    driver.find_element_by_id("fromStationText").send_keys(Keys.ENTER)
    driver.find_element_by_id("toStationText").clear()
    driver.find_element_by_id("toStationText").send_keys("开封")
    driver.find_element_by_id("toStationText").send_keys(Keys.ENTER)
    js = 'document.getElementById("train_date").removeAttribute("readonly");'
    driver.execute_script(js)
    # js方法输入日期
    js_value = 'document.getElementById("train_date").value = "2017-12-30"'
    driver.execute_script(js_value)
    # selenium方法清空后输入日期
    # driver.find_element_by_id("train_date").clear()
    # driver.find_element_by_id("train_date").send_keys("2017-12-30")
    driver.find_element_by_id("a_search_ticket").click()

time.sleep(5)
driver.quit()
if __name__ == '__main__':
    delete_readonly()

