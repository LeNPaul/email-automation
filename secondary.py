from selenium import webdriver
import json
import time

def login():

    browser.get('https://accounts.google.com')

    email = browser.find_element_by_name('identifier')
    email.send_keys(info['username'])
    submitEmail = browser.find_element_by_id('identifierNext')
    submitEmail.click()

    time.sleep(1)

    password = browser.find_element_by_name('password')
    password.send_keys(info['password'])
    submitPassword = browser.find_element_by_id('passwordNext')
    submitPassword.click()

    time.sleep(1)

    return browser.find_element_by_link_text('About Google')

def firstAction():

    browser.get(info['linkOne'])

    time.sleep(2)

    selector = browser.find_element_by_id('gwt-uid-190')
    selector.click()

    time.sleep(1)

    save = browser.find_element_by_xpath('//div[@aria-label="Save"]')
    save.click()

    time.sleep(2)

    return browser.find_element_by_id('groups-banner-link')

def secondAction():

    browser.get(info['linkTwo'])

    time.sleep(2)

    selector = browser.find_element_by_id('gwt-uid-345')
    selector.click()

    time.sleep(1)

    save = browser.find_element_by_xpath('//div[@aria-label="Save"]')
    save.click()

    time.sleep(2)

    return browser.find_element_by_link_text('Groups')

def thirdAction():

    browser.get(info['linkThree'])

    time.sleep(2)

    enable = browser.find_element_by_id('gwt-uid-277') #gwt-uid-277
    enable.click()

    time.sleep(1)

    save = browser.find_element_by_xpath('//*[@data-title="Save"]')
    save.click()

    time.sleep(2)

    return browser.find_element_by_link_text('Groups')

# Read in credentials and chromedriver file path
file = open('credentials.json', 'r')
info = json.loads(file.read())

print "\nTurning off email autoresponder... \n"

# Log into Google account
loggedIn = None
while not loggedIn:
    try:
        # Set path to the chromedriver
        browser = webdriver.Chrome(info['cdPath'])
        print "Logging into Google account..."
        loggedIn = login()
        print "Login successful! \n"
    except:
        browser.quit()
        print "Failed to login - will try again..."

# Do the first action
step1 = None
while not step1:
    try:
        print "Setting 'All email' on internal solutions member to ensure internal members will receive support emails during office hours..."
        step1 = firstAction()
        print "Success! \n"
    except:
        print "Action failed - will try again..."

# Do the second action
step2 = None
while not step2:
    try:
        print "Check 'Moderate messages from non-members of group' to ensure approval process is enabled..."
        step2 = secondAction()
        print "Success! \n"
    except:
        print "Action failed - will try again..."

# Do the third action
step3 = None
while not step3:
    try:
        print "Disable autoresponder..."
        step3 = thirdAction()
        print "Success! \n"
    except:
        print "Action failed - will try again..."

print "Email autoresponder turned off!"
print "Closing browser..."
browser.close()
print "Browser turned off"
