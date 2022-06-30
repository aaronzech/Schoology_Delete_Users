# Imports
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from GenerateUserList import userList
from GenerateUserList import rowCount;

def clearSearchBox(searchbox):
    searchbox.click(); # error 6/27/22 is not clickable at point (1106,88) because another element <div id="popups-overlay"> obscures it
    searchbox.send_keys(Keys.CONTROL, "a");
    searchbox.send_keys(Keys.BACK_SPACE);

def deleteSchoologyUser(browser):
    searchbox = browser.find_element(By.ID,"edit-filter-search")
    # Loop through the User.csv list
    for i in range(len(userList)):
        student = userList[i];
        print('\ncurrent user',student)
        print('\n\n')
        searchbox.send_keys(student);
        time.sleep(1)
        searchbox.send_keys(Keys.ENTER);
        time.sleep(5);
        
        #checkbox 
        if browser.find_elements(By.XPATH,'/html/body/div[4]/div[3]/div[1]/div[2]/div[2]/div/div[3]/form[2]/div/table[2]/thead/tr/th[1]/span/input'):
            time.sleep(3);
            browser.find_element(By.XPATH,'/html/body/div[4]/div[3]/div[1]/div[2]/div[2]/div/div[3]/form[2]/div/table[2]/thead/tr/th[1]/span/input').click();
        else:
            print("****************************************************")
            print("User NOT FOUND ---- ",student)
            print("****************************************************")
            searchbox = browser.find_element(By.ID,"edit-filter-search")
            clearSearchBox(searchbox)
            continue;
        
        #bulk actions
        bulkActionsBox = browser.find_element(By.ID,'edit-bulk-actions');
        bulkActionsBox.click();
        time.sleep(2);
        bulkActionsBox.send_keys('M');
        bulkActionsBox.send_keys(Keys.ENTER);
        time.sleep(2);

        #submit
        submitButton = browser.find_element(By.ID,'edit-submit').send_keys(Keys.ENTER);
        time.sleep(2)

         # send email checkbox
        sendEmailCheckBox = browser.find_element(By.ID,'user-inactive-send-email');
        sendEmailCheckBox.click();

        # comments
        commentBox = browser.find_element(By.ID,'user-inactive-comments');
        commentBox.send_keys("Termed Staff, deleted by Autoscript program");

        # submit
        submitButton = browser.find_element(By.ID,'popup_submit');

        print("****************************************************")
        print("User deleted ---- ",student)
        print("****************************************************")
        submitButton.click();

        time.sleep(3)
            
        #clear search box   
        searchbox = browser.find_element(By.ID,"edit-filter-search")
        clearSearchBox(searchbox)            
        continue;