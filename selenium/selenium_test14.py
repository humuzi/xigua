from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import UnexpectedAlertPresentException
import time

driver = webdriver.Chrome()
driver.get("https://www.helloweba.com/demo/2017/unlock/")

chains = ActionChains(driver)
element = driver.find_elements_by_class_name("slide-to-unlock-handle")[0]
chains.click_and_hold(element).perform()

for index in range(200):
    try:
        chains.move_by_offset(2,0).perform()
    except UnexpectedAlertPresentException:
        break
    chains.reset_actions()
    time.sleep(0.5)

# success_text = driver.switch_to.alert.text
driver.switch_to.alert.accept()

time.sleep(3)


















































































































































































































































































































