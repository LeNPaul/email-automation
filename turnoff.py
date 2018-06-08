from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import json
import time

def disable():

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
        password.send_keys(info['password'])
        password.send_keys(Keys.RETURN)

        nextPage = wait.until(
             EC.presence_of_element_located((By.LINK_TEXT, "About Google")))

        print "[" + time.asctime(time.localtime(time.time())) + "] Success!"

        return True

    def setAllEmail():

        print "[" + time.asctime(time.localtime(time.time())) + "] Changing delivery setting to 'All Email' for internal solutions group member..."

        browser.get(info['linkOne'])
        wait = WebDriverWait(browser,5)

        selector = wait.until(
             EC.presence_of_element_located((By.ID, "gwt-uid-190")))
        selector.click()

        save = wait.until(
             EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Save"]')))
        save.click()

        time.sleep(2)

        nextPage = wait.until(
             EC.presence_of_element_located((By.ID, 'groups-banner-link')))

        print "[" + time.asctime(time.localtime(time.time())) + "] Success! "

        return True

    def enableModeration():

        print "[" + time.asctime(time.localtime(time.time())) + "] Checking 'Moderate messages from non-members of group' to enable approval process..."

        browser.get(info['linkTwo'])
        wait = WebDriverWait(browser,5)

        selector = wait.until(
             EC.presence_of_element_located((By.ID, 'gwt-uid-345')))
        selector.click()

        save = wait.until(
             EC.presence_of_element_located((By.XPATH, '//div[@aria-label="Save"]')))
        save.click()

        time.sleep(2)

        nextPage = wait.until(
             EC.presence_of_element_located((By.XPATH, '//div[@aria-disabled="true"]')))

        print "[" + time.asctime(time.localtime(time.time())) + "] Success! "

        return True

    def disableAutoReply():

        print "[" + time.asctime(time.localtime(time.time())) + "] Disabling autoresponder..."

        browser.get(info['linkThree'])
        wait = WebDriverWait(browser,5)

        enable = wait.until(
             EC.presence_of_element_located((By.ID, 'gwt-uid-277')))
        enable.click()

        save = wait.until(
             EC.presence_of_element_located((By.XPATH, '//*[@data-title="Save"]')))
        save.click()

        time.sleep(2)

        nextPage = wait.until(
             EC.presence_of_element_located((By.XPATH, '//div[@aria-disabled="true"]')))

        print "[" + time.asctime(time.localtime(time.time())) + "] Success! "

        return True

    # Read in credentials and chromedriver file path
    file = open('credentials.json', 'r')
    info = json.loads(file.read())
    file.close()

    # Instantiate a chrome options object so you can set the size and headless preference
    chrome_options = Options()
    chrome_options.set_headless(headless=True)

    print "\n[" + time.asctime(time.localtime(time.time())) + "] Turning off email autoresponder... "

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
            time.sleep(2)

    # Do the first action
    step1 = False
    while not step1:
        try:
            step1 = setAllEmail()
        except:
            print "[" + time.asctime(time.localtime(time.time())) + "] Action failed. Will try again..."
            time.sleep(2)

    # Do the second action
    step2 = False
    while not step2:
        try:
            step2 = enableModeration()
        except:
            print "[" + time.asctime(time.localtime(time.time())) + "] Action failed. Will try again..."
            time.sleep(2)

    # Do the third action
    step3 = None
    while not step3:
        try:
            step3 = disableAutoReply()
        except:
            print "[" + time.asctime(time.localtime(time.time())) + "] Action failed. Will try again..."
            time.sleep(2)

    print "[" + time.asctime(time.localtime(time.time())) + "] Closing browser..."

    browser.close()

    print "[" + time.asctime(time.localtime(time.time())) + "] Browser closed!"

    print "[" + time.asctime(time.localtime(time.time())) + "] Email autoresponder turned off!"

    print "[" + time.asctime(time.localtime(time.time())) + "] Email automation successful!"
