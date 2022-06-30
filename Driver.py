# Imports
from selenium import webdriver
import time
import csv
import os
from Login import login

# Globals
from SchoologyControl import deleteSchoologyUser
from GenerateUserList import populateUserList


# Fire Fox Web Driver
browser = webdriver.Firefox(executable_path="/Users/zechaaron/Downloads/geckodriver.exe")

# Program Start
populateUserList();

time.sleep(3)
# Start up the web browser and open & login to Schoology
login(browser)
# Operates Schoology website after login
deleteSchoologyUser(browser)