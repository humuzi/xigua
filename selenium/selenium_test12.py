from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://passport.kuaibo.com/login/?referrer=http%3A%2F%2Fwebcloud.kuaibo.com%2F")

driver.find_element_by_id("user_name").send_keys("username")
driver.find_element_by_id("user_pwd").send_keys("123456")
driver.find_element_by_id("user_pwd").send_keys(Keys.ENTER)
time.sleep(2)

chain = ActionChains(driver)
qqq= driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div/div[3]/table/tbody/tr/td[2]")
chain.context_click(qqq).perform()
time.sleep(2)

driver.quit()