from time import sleep
from selenium import webdriver
from dotenv import load_dotenv
load_dotenv()
import os

def login(username,password):
    username_input = browser.find_element_by_css_selector("input[name='username']")
    password_input = browser.find_element_by_css_selector("input[name='password']")
    username_input.send_keys(username)
    password_input.send_keys(password)

def goToDirect():
    browser.find_element_by_xpath("//button[@type='submit']").click()

    browser.find_element_by_xpath("//button[ text()='Save Info']").click()
    sleep(3)
    browser.find_element_by_xpath("//button[ text()='Not Now']").click()

    browser.find_element_by_css_selector("nav svg[aria-label='Direct']").click()


browser = webdriver.Chrome()
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')

login(os.getenv("instaname"),os.getenv("password"))
goToDirect()
browser.implicitly_wait(2)

dms=browser.find_element_by_xpath("//div[@class='        DPiy6            Igw0E     IwRSH      eGOV_         _4EzTm                                                                                                              ']")
dms.click()

content = browser.find_elements_by_xpath("//div[@class='   CMoMH    _8_yLp  ']//span")
for c in content:
    print(c.text)









# for dm in dms:
#     browser.implicitly_wait(1)
#     dm.click()

# content = browser.find_element_by_xpath("//div[@class='   CMoMH    _8_yLp  ']//span")
# print(content)
# for c in content:
#     print(c.text)


# sleep(5)

# browser.close()