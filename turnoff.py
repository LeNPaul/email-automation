from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import base64
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

        time.sleep(2)

        password = wait.until(
             EC.presence_of_element_located((By.CSS_SELECTOR, "input[type=password]")))
        password.send_keys(base64.b64decode(info['password']))
        password.send_keys(Keys.RETURN)

        time.sleep(2)

        nextPage = wait.until(
             EC.presence_of_element_located((By.LINK_TEXT, "About Google")))

        print "[" + time.asctime(time.localtime(time.time())) + "] Success!"

        return True

    def setAllEmail():

        print "[" + time.asctime(time.localtime(time.time())) + "] Changing delivery setting to 'All Email' for internal solutions group member..."

        browser.get(info['linkOne'])
        wait = WebDriverWait(browser,5)

        selector = wait.until(
             EC.presence_of_element_located((By.ID, "gwt-uid-194")))
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
             EC.presence_of_element_located((By.ID, 'gwt-uid-180')))
        if "false" in selector.get_attribute('aria-checked'):
            selector.click()

            time.sleep(2)

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
             EC.presence_of_element_located((By.ID, 'gwt-uid-281')))
        if "true" in enable.get_attribute('aria-checked'):
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
                step1 = setAllEmail()
            except:
                print "[" + time.asctime(time.localtime(time.time())) + "] Action failed. Will try again..."
                browser.refresh()
                time.sleep(5)

        # Do the second action
        step2 = False
        while not step2:
            try:
                step2 = enableModeration()
            except:
                print "[" + time.asctime(time.localtime(time.time())) + "] Action failed. Will try again..."
                browser.refresh()
                time.sleep(5)

        # Do the third action
        step3 = False
        while not step3:
            try:
                step3 = disableAutoReply()
            except:
                print "[" + time.asctime(time.localtime(time.time())) + "] Action failed. Will try again..."
                browser.refresh()
                time.sleep(5)

        print "[" + time.asctime(time.localtime(time.time())) + "] Closing browser..."

        browser.close()

        print "[" + time.asctime(time.localtime(time.time())) + "] Success!"

        print "[" + time.asctime(time.localtime(time.time())) + "] Email autoresponder turned off!"

        logs = open(info['logText'],'a')
        logs.write("[" + time.asctime(time.localtime(time.time())) + "] Process completed, email autoresponder disabled! Email automation successful! \n")
        logs.close()
    except:
        print "[" + time.asctime(time.localtime(time.time())) + "] Process error, email autoresponder not disabled! Email automation failed! \n"
        logs = open(info['logText'],'a')
        logs.write("[" + time.asctime(time.localtime(time.time())) + "] Process error, email autoresponder not disabled! Email automation failed! \n")
