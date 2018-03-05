# coding=utf-8
from appium import webdriver

desired_caps={
    "platformName":"Android",
    "deviceName":"xxxxxx",
    "platformVersion":"4.4.2",
    "appPackage":"com.taobao.taobao",
    "appActivity":"com.taobao.tao.welcome.Welcome"
    }
driver=webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

def swipeUp(driver,t=500,n=1):
    l=driver.get_window_size()
    x1=l['width']*0.2
    y1=l['height']*0.75
    y2=l['height']*0.25
    for i in range(n):
        driver.swipe(x1,y1,x1,y2,t)

if __name__ == '__main__':
    swipeUp(driver,n=2)