# coding =utf-8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.touch_actions import TouchActions

url = 'https://login.m.taobao.com/msg_login.htm?spm=0.0.0.0'
mobile_emulation = {"deviceName":"iPhone 6"}
options = Options()
options.add_experimental_option("mobileEmulation",mobile_emulation)
driver =webdriver.Chrome(chrome_options=options)
driver.get(url)
#
def perform():
    driver.find_element_by_id("username").send_keys("18267148256")
    el = driver.find_element_by_id("getCheckcode")
    TouchActions(driver).tap(el).perform()

if __name__ == '__main__':
    perform()
