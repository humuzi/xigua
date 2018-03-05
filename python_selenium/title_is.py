# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")

def title_is():
    title = EC.title_is(u"百度一下，你就知道")
    print(title(driver))

def title_contains():
    title = EC.title_contains(u"百度一下")
    print(title(driver))

if __name__ == '__main__':
    title_is()
    title_contains()
    driver.quit()