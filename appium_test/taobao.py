# coding=utf-8
from appium import webdriver

desired_caps={
    "platformName":"Android",
    "deviceName":"AVRZXA37JL",
    "platformVersion":"4.4.2",
    "appPackage":"com.taobao.taobao",
    "appActivity":"com.taobao.tao.welcome.Welcome"}

driver = webdriver.Remote("http://www.127.0.0.1:4723/wd/hub",desired_caps)