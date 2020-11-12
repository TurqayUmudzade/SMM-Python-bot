from time import sleep
from selenium import webdriver
from dotenv import load_dotenv
load_dotenv()
import os
import io
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


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
    content = browser.find_elements_by_xpath("//div[@class='   CMoMH    _8_yLp  ']//span")
    for c in content:
        f.write(c.text)
        f.write("\n")


def readNChats(n):
    dms=browser.find_elements_by_xpath("//div[@class='        DPiy6            Igw0E     IwRSH      eGOV_         _4EzTm                                                                                                              ']")
    for x in range(n):
       try:
            sleep(1)
            browser.implicitly_wait(5)
            dms=browser.find_elements_by_xpath("//div[@class='        DPiy6            Igw0E     IwRSH      eGOV_         _4EzTm                                                                                                              ']")
            dms[x].click()
            readChat()
            f.write(" \n--------------- \n")
            print(x)
       except IndexError:
           print(x," chats have been read")
           break

def xyClick(x,y):
    actions.move_to_element_with_offset(browser.find_element_by_tag_name('body'), 0,0)
    actions.move_by_offset(x,y).click().perform()

def readNChats2(n):
    script="var element = document.getElementsByClassName('N9abW');element[0].scroll(0,"
    for x in range(n):
        xyClick(91,208)
        readChat()
        f.write(" \n--------------- \n")
        browser.execute_script(script+str(72*x)+")")
        print(x)
        
        
browser = webdriver.Chrome()
actions = ActionChains(browser)
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')

login(os.getenv("instaname"),os.getenv("password"))
goToDirect()
f = io.open("text.txt", "a", encoding="utf-8")
    
browser.implicitly_wait(2)

readNChats2(300)


f.close()



