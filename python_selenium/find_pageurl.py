# coding =utf-8
from selenium import webdriver
import re

driver = webdriver.Chrome()
driver.get("http://www.cnblogs.com/yoyoketang/")
page = driver.page_source

url_list=re.findall('href=\"(.*?)\"',page,re.S)
url_all=[]
for url in url_list:
    if "http" in url:
        print(url)
        url_all.append(url)
    else:
        pass

print(url_all)