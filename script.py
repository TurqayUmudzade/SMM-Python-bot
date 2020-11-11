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

def readChat():
    browser.implicitly_wait(2)
    #browser.execute_script("var chat = document.getElementsByClassName('frMpI  -sxBV');chat.scrollBy(0,250)")
    content = browser.find_elements_by_xpath("//div[@class='   CMoMH    _8_yLp  ']//span")
    for c in content:
        print(c.text)


browser = webdriver.Chrome()
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')

login(os.getenv("instaname"),os.getenv("password"))
goToDirect()
browser.implicitly_wait(2)

dms=browser.find_elements_by_xpath("//div[@class='        DPiy6            Igw0E     IwRSH      eGOV_         _4EzTm                                                                                                              ']")
for x in range(40):
   try:
        dms=browser.find_elements_by_xpath("//div[@class='        DPiy6            Igw0E     IwRSH      eGOV_         _4EzTm                                                                                                              ']")
        dms[x].click()
        readChat()
        print("-------")
   except IndexError:
       break

