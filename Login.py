#pudated 6/27/2022 - runs

import time
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import secrets
browser = webdriver.Firefox(executable_path="/Users/zechaaron/Downloads/geckodriver.exe")



def login(browser):
    time.sleep(4)  # delay for more reliablity
    browser.get("https://osseo.schoology.com/users/manage?perpage=1")
    time.sleep(4)  # delay for more reliablity

   # browser.find_element_by_id('edit-mail-wrapper')

    # Locate Username Box
    userName = browser.find_element(By.ID,"edit-mail")

    userName.send_keys(secrets.username)

    time.sleep(0.1) # delay for more reliablity

    # Locate Password Box
    passwordBox = browser.find_element(By.ID,'edit-pass')

    passwordBox.send_keys(secrets.password)

    browser.find_element(By.CLASS_NAME,'submit-span-wrapper')  # find log in button

    elem = browser.find_element(By.CLASS_NAME,'submit-span-wrapper')

    elem.click()  # click log in button

    print("Login Finished\n")
    time.sleep(6)  # delay for more reliablitiy

