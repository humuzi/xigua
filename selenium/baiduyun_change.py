# coding=utf-8

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://pan.baidu.com/disk/home#list/path=%2F&vmode=list")
