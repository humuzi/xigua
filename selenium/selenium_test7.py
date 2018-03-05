from selenium import webdriver
import os,time

browser = webdriver.Chrome()
file_path = 'file:///'+os.path.abspath('upload_file.html')
browser.get(file_path)

browser.find_element_by_name('file').send_keys('D:\\PythonProject\\selenium\\upload_file.txt')
time.sleep(3)

browser.quit()