# todo:
#   - Replace the time.sleep() functions with some kind of function that waits for the browser to finish loading before running the next action
#   - Need to action some kind of checking to make sure that actions aren't repeated (therefore cancelling each out) on a retry

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import json
import time

def enable():

    def login():

        browser.get('https://accounts.google.com')

        email = WebDriverWait(browser,5).until(
             EC.presence_of_element_located((By.CSS_SELECTOR, "input[type=email]")))
        email.send_keys(info['username'])
        email.send_keys(Keys.RETURN)

        password = WebDriverWait(browser,5).until(
             EC.presence_of_element_located((By.CSS_SELECTOR, "input[type=password]")))
        password.send_keys(info['password'])
        password.send_keys(Keys.RETURN)

        return WebDriverWait(browser,5).until(
             EC.presence_of_element_located((By.LINK_TEXT, "About Google")))

    def setNoEmail():

        browser.get(info['linkOne'])

        time.sleep(2)

        selector = browser.find_element_by_id('gwt-uid-184')
        selector.click()

        time.sleep(2)

        save = browser.find_element_by_xpath('//div[@aria-label="Save"]')
        save.click()

        time.sleep(2)

        return browser.find_element_by_id('groups-banner-link')

    def disableModeration():

        browser.get(info['linkTwo'])

        time.sleep(2)

        selector = browser.find_element_by_id('gwt-uid-345')
        selector.click()

        time.sleep(2)

        save = browser.find_element_by_xpath('//div[@aria-label="Save"]')
        save.click()

        time.sleep(2)

        return browser.find_element_by_link_text('Groups')

    def enableAutoReply():

        browser.get(info['linkThree'])

        time.sleep(2)

        enable = browser.find_element_by_id('gwt-uid-277') #gwt-uid-277
        enable.click()

        time.sleep(2)

        file = open('email.txt', 'r')
        email =file.read()

        textBox = browser.find_element_by_xpath("//textarea[@id='gwt-uid-261']")
        textBox.send_keys(email)

        time.sleep(2)

        save = browser.find_element_by_xpath('//*[@data-title="Save"]')
        save.click()

        time.sleep(2)

        return browser.find_element_by_link_text('Groups')

    # Read in credentials and chromedriver file path
    file = open('credentials.json', 'r')
    info = json.loads(file.read())
    file.close()

    # Instantiate a chrome options object so you can set the size and headless preference
    chrome_options = Options()
    chrome_options.set_headless(headless=True)

    print "\n[" + time.asctime(time.localtime(time.time())) + "] Initializing email autoresponder..."

    # Log into Google account
    loggedIn = None
    while not loggedIn:
        try:
            # Set path to the chromedriver
            browser = webdriver.Chrome(chrome_options=chrome_options, executable_path=info['cdPath'])
            print "[" + time.asctime(time.localtime(time.time())) + "] Logging into Google account..."
            loggedIn = login()
            print "[" + time.asctime(time.localtime(time.time())) + "] Success!"
        except:
            browser.quit()
            print "[" + time.asctime(time.localtime(time.time())) + "] Failed to login - will try again..."

    # Do the first action
    step1 = None
    while not step1:
        try:
            print "[" + time.asctime(time.localtime(time.time())) + "] Changing delivery setting to 'No Email' for internal solutions group member..."
            step1 = setNoEmail()
            print "[" + time.asctime(time.localtime(time.time())) + "] Success!"
        except:
            print "[" + time.asctime(time.localtime(time.time())) + "] Action failed - will try again..."

    # Do the second action
    step2 = None
    while not step2:
        try:
            print "[" + time.asctime(time.localtime(time.time())) + "] Unchecking 'Moderate messages from non-members of group' to disable approval process..."
            step2 = disableModeration()
            print "[" + time.asctime(time.localtime(time.time())) + "] Success!"
        except:
            print "[" + time.asctime(time.localtime(time.time())) + "] Action failed - will try again..."

    # Do the third action
    step3 = None
    while not step3:
        try:
            print "[" + time.asctime(time.localtime(time.time())) + "] Enabling autoresponder with default message..."
            step3 = enableAutoReply()
            print "[" + time.asctime(time.localtime(time.time())) + "] Success!"
        except:
            print "[" + time.asctime(time.localtime(time.time())) + "] Action failed - will try again..."

    print "[" + time.asctime(time.localtime(time.time())) + "] Closing browser..."
    browser.close()
    print "[" + time.asctime(time.localtime(time.time())) + "] Browser turned off"

    print "[" + time.asctime(time.localtime(time.time())) + "] Email autoresponder turned on!"

    print "[" + time.asctime(time.localtime(time.time())) + "] Email automation successful!"
