# coding = utf-8

from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://segmentfault.com/news")

total_page = len(driver.find_element_by_class_name("pagination").find_elements_by_tag_name("li"))-2

current_page = driver.find_element_by_class_name("pagination").find_element_by_class_name("active")
print("Current page is %s"%(current_page.text))

js = "var q=document.documentElement.scrollTop=100000"
driver.execute_script(js)
time.sleep(1)
driver.find_element_by_class_name('pagination').find_element_by_link_text("下一页").click()

time.sleep(2)
driver.quit()