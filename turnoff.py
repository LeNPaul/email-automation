from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
import time

def disable():

    def login():

        browser.get('https://accounts.google.com')

        email = browser.find_element_by_css_selector('input[type=email]')
        email.send_keys(info['username'])

        time.sleep(2)

        email.send_keys(u'\ue007')

        time.sleep(2)

        password = browser.find_element_by_css_selector('input[type=password]')
        password.send_keys(info['password'])

        time.sleep(2)

        password.send_keys(u'\ue007')

        time.sleep(2)

        return browser.find_element_by_link_text('About Google')

    def firstAction():

        browser.get(info['linkOne'])

        time.sleep(2)

        selector = browser.find_element_by_id('gwt-uid-190')
        selector.click()

        time.sleep(2)

        save = browser.find_element_by_xpath('//div[@aria-label="Save"]')
        save.click()

        time.sleep(2)

        return browser.find_element_by_id('groups-banner-link')

    def secondAction():

        browser.get(info['linkTwo'])

        time.sleep(2)

        selector = browser.find_element_by_id('gwt-uid-345')
        selector.click()

        time.sleep(2)

        save = browser.find_element_by_xpath('//div[@aria-label="Save"]')
        save.click()

        time.sleep(2)

        return browser.find_element_by_link_text('Groups')

    def thirdAction():

        browser.get(info['linkThree'])

        time.sleep(2)

        enable = browser.find_element_by_id('gwt-uid-277')
        enable.click()

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

    print "\n[" + time.asctime(time.localtime(time.time())) + "] Turning off email autoresponder... "

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
            print "[" + time.asctime(time.localtime(time.time())) + "] Changing delivery setting to 'All Email' for internal solutions group member..."
            step1 = firstAction()
            print "[" + time.asctime(time.localtime(time.time())) + "] Success! "
        except:
            print "[" + time.asctime(time.localtime(time.time())) + "] Action failed - will try again..."

    # Do the second action
    step2 = None
    while not step2:
        try:
            print "[" + time.asctime(time.localtime(time.time())) + "] Checking 'Moderate messages from non-members of group' to enable approval process..."
            step2 = secondAction()
            print "[" + time.asctime(time.localtime(time.time())) + "] Success! "
        except:
            print "[" + time.asctime(time.localtime(time.time())) + "] Action failed - will try again..."

    # Do the third action
    step3 = None
    while not step3:
        try:
            print "[" + time.asctime(time.localtime(time.time())) + "] Disabling autoresponder..."
            step3 = thirdAction()
            print "[" + time.asctime(time.localtime(time.time())) + "] Success! "
        except:
            print "[" + time.asctime(time.localtime(time.time())) + "] Action failed - will try again..."

    print "[" + time.asctime(time.localtime(time.time())) + "] Closing browser..."
    browser.close()
    print "[" + time.asctime(time.localtime(time.time())) + "] Browser turned off"

    print "[" + time.asctime(time.localtime(time.time())) + "] Email autoresponder turned off!"
