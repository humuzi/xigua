# coding = utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()
def csdn_login(username,pwd):

    url = "https://www.csdn.net/"
    driver.get(url)
    driver.implicitly_wait(30)
    driver.find_element_by_link_text("登录").click()
    driver.implicitly_wait(30)
    windows = driver.window_handles
    driver.switch_to.window(windows[-1])
    driver.find_element_by_xpath("//input[@id='username']").send_keys(Keys.TAB)
    driver.find_element_by_xpath("//input[@id='username']").send_keys(username)
    driver.find_element_by_xpath("//input[@id='password']").send_keys(Keys.TAB)
    driver.find_element_by_xpath("//input[@id='password']").send_keys(pwd)
    driver.find_element_by_xpath("//input[@id='password']").send_keys(Keys.ENTER)
    driver.find_element_by_link_text("humuzia").click()


def edit():
    csdn_login("humuzia", "945688**")
    driver.find_element_by_link_text(u"文章管理").click()
    windows =driver.window_handles()
    driver.switch_to.window(windows[0])
    driver.find_element_by_link_text("+写新文章").click()
    edittitle=u"selenium+python 富文本"
    driver.find_element_by_xpath("//input[@id='txtTitle']").send_keys(edittitle)
    editbody = u"这里是发送的正文"
    # 法一：selenium处理富文本
    driver.switch_to.frame("xhe0_iframe")
    driver.find_element_by_xpath("//body[@class='editMode']").send_keys(editbody)
    # 法二：js处理富文本
    # js = 'document.getElementById("xhe0_iframe").contentWindow.document.body.innerHTML="%s"'%editbody
    # driver.execute_script(js)

    driver.switch_to.frame("frm_img_2")
    driver.find_element_by_id("file1").send_keys(r"D://PythonProject//selenium//jay.png")
    driver.find_element_by_xpath("//input[@id='txtTag2']").send_keys("Practice")
    driver.find_element_by_xpath("//input[@id='txtTag']").send_keys(u"测试")
    driver.find_element_by_xpath("//input[@id='radChl1']").click()

    driver.find_element_by_xpath("//input[@id='btnPublish']").click()

time.sleep(2)
driver.quit()



if __name__ == '__main__':
    edit()


