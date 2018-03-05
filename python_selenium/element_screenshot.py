# coding =utf-8
from selenium import webdriver
from PIL import Image

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")

driver.save_screenshot("button.png")
element =driver.find_element_by_id("su")
# element.screenshot('button.png')
print(element.location)
print(element.size)

left = element.location['x']
top = element.location['y']
right = element.location['x']+element.size['width']
bottom = element.location['y']+element.size['height']

im = Image.open('button.png')
im = im.crop((left,top,right,bottom))
im.save('button.png')