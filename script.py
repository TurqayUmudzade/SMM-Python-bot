from time import sleep
from selenium import webdriver
from dotenv import load_dotenv
load_dotenv()

import os
username= os.getenv("instaname")
password=os.getenv("password")

browser = webdriver.Chrome()
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')

username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

username_input.send_keys(username)
password_input.send_keys(password)

# login_button = browser.find_element_by_xpath("//button[@type='submit']")
# login_button.click()

browser.find_element_by_xpath("//button[@type='submit']").click()

browser.find_element_by_xpath("//button[ text()='Save Info']").click()
sleep(3)
browser.find_element_by_xpath("//button[ text()='Not Now']").click()

browser.find_element_by_css_selector("nav svg[aria-label='Direct']").click()


sleep(5)

# browser.close()