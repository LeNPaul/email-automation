# todo:
#   - Need to action some kind of checking to make sure that actions aren't repeated (therefore cancelling each out) on a retry

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import base64
import json
import time

def enable():

    def login():

        print "[" + time.asctime(time.localtime(time.time())) + "] Logging into Google account..."

        browser.get('https://accounts.google.com')
        wait = WebDriverWait(browser,5)

        email = wait.until(
             EC.presence_of_element_located((By.CSS_SELECTOR, "input[type=email]")))
        email.send_keys(info['username'])
        email.send_keys(Keys.RETURN)

        password = wait.until(
             EC.presence_of_element_located((By.CSS_SELECTOR, "input[type=password]")))
        password.send_keys(base64.b64decode(info['password']))
        password.send_keys(Keys.RETURN)

        nextPage = wait.until(
             EC.presence_of_element_located((By.LINK_TEXT, "About Google")))

        print "[" + time.asctime(time.localtime(time.time())) + "] Success!"

        return True

    def setNoEmail():

        print "[" + time.asctime(time.localtime(time.time())) + "] Changing delivery setting to 'No Email' for internal solutions group member..."

        browser.get(info['linkOne'])
        wait = WebDriverWait(browser,5)

        selector = wait.until(
             EC.presence_of_element_located((By.ID, 'gwt-uid-184')))
        selector.click()

        save = browser.find_element_by_xpath('//div[@aria-label="Save"]')
        save.click()

        time.sleep(2)

        nextPage = wait.until(
             EC.presence_of_element_located((By.ID, 'groups-banner-link')))

        print "[" + time.asctime(time.localtime(time.time())) + "] Success!"

        return True

    def disableModeration():

        print "[" + time.asctime(time.localtime(time.time())) + "] Unchecking 'Moderate messages from non-members of group' to disable approval process..."

        browser.get(info['linkTwo'])
        wait = WebDriverWait(browser,5)

        selector = wait.until(
             EC.presence_of_element_located((By.ID, 'gwt-uid-345')))
        if "true" in selector.get_attribute('aria-checked'):
            selector.click()

        save = wait.until(
             EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Save"]')))
        save.click()

        time.sleep(2)

        nextPage = wait.until(
             EC.presence_of_element_located((By.XPATH, '//div[@aria-disabled="true"]')))

        print "[" + time.asctime(time.localtime(time.time())) + "] Success!"

        return True

    def enableAutoReply():

        print "[" + time.asctime(time.localtime(time.time())) + "] Enabling autoresponder with default message..."

        browser.get(info['linkThree'])
        wait = WebDriverWait(browser,5)

        enable = wait.until(
             EC.presence_of_element_located((By.ID, 'gwt-uid-277')))
        enable.click()

        file = open(info['emailText'], 'r')
        email =file.read()

        textBox = wait.until(
             EC.presence_of_element_located((By.XPATH, "//textarea[@id='gwt-uid-261']")))
        textBox.send_keys(email)

        save = wait.until(
             EC.presence_of_element_located((By.XPATH, '//*[@data-title="Save"]')))
        save.click()

        time.sleep(2)

        nextPage = wait.until(
             EC.presence_of_element_located((By.ID, 'groups-banner-link')))

        print "[" + time.asctime(time.localtime(time.time())) + "] Success!"

        return True

    # Read in credentials and chromedriver file path
    file = open('credentials.json', 'r')
    info = json.loads(file.read())
    file.close()

    # Instantiate a chrome options object so you can set the size and headless preference
    chrome_options = Options()
    chrome_options.set_headless(headless=True)

    print "\n[" + time.asctime(time.localtime(time.time())) + "] Initializing email autoresponder..."

    try:
        # Log into Google account
        loggedIn = False
        while not loggedIn:
            try:
                # Set path to the chromedriver
                browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=info['cdPath'])
                loggedIn = login()
            except:
                # Close previous browser object
                browser.quit()
                print "[" + time.asctime(time.localtime(time.time())) + "] Failed to login. Will try again..."
                time.sleep(5)

        # Do the first action
        step1 = False
        while not step1:
            try:
                step1 = setNoEmail()
            except:
                print "[" + time.asctime(time.localtime(time.time())) + "] Action failed - will try again..."
                browser.refresh()
                time.sleep(5)

        # Do the second action
        step2 = False
        while not step2:
            try:
                step2 = disableModeration()
            except:
                print "[" + time.asctime(time.localtime(time.time())) + "] Action failed. Will try again..."
                browser.refresh()
                time.sleep(5)

        # Do the third action
        step3 = False
        while not step3:
            try:
                step3 = enableAutoReply()
            except:
                print "[" + time.asctime(time.localtime(time.time())) + "] Action failed. Will try again..."
                browser.refresh()
                time.sleep(5)

        print "[" + time.asctime(time.localtime(time.time())) + "] Closing browser..."
        browser.close()
        print "[" + time.asctime(time.localtime(time.time())) + "] Browser turned off"

        print "[" + time.asctime(time.localtime(time.time())) + "] Email autoresponder turned on!"

        logs = open(info['logText'],'a')
        logs.write("[" + time.asctime(time.localtime(time.time())) + "] Process completed, email autoresponder enabled! Email automation successful! \n")
        logs.close()
    except:
        print "[" + time.asctime(time.localtime(time.time())) + "] Process error, email autoresponder not enabled! Email automation failed! \n"
        logs = open(info['logText'],'a')
        logs.write("[" + time.asctime(time.localtime(time.time())) + "] Process error, email autoresponder not enabled! Email automation failed! \n")
