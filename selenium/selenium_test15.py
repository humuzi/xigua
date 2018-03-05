from selenium import webdriver
from selenium.webdriver.support.select import Select
import os,time

driver = webdriver.Chrome()
file_path = "file:///"+os.path.abspath("test.html")
driver.get(file_path)

js = 'document.querySelectorAll("Select")[0].style.display="block";'
driver.execute_script(js)

sel = driver.find_element_by_tag_name('select')
Select(sel).select_by_value('opel')
time.sleep(2)

driver.quit()
