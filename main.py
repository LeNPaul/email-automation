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

    selector = browser.find_element_by_id('gwt-uid-184')
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

    text = '''Hello,

Thank you for reaching out to iNTERFACEWARE's support desk. Resolving your issues and answering your questions are a top priority for us. We have received your inquiry, and our support team will be in touch with you within one business day.

In the meantime, you may refer to our Help Center (http://help.interfaceware.com/) for more information.

Please note that our working hours are 9:00am to 5:00pm EST from Monday to Friday excluding Statutory Holidays recognized in the province of Ontario, Canada.

For customers with 24/7 Support, please use the emergency support channels provided for immediate assistance.

Thank you,

Client Solutions Team'''

    textBox = browser.find_element_by_xpath("//textarea[@id='gwt-uid-261']")
    textBox.send_keys(text)

    time.sleep(2)

    save = browser.find_element_by_xpath('//*[@data-title="Save"]')
    save.click()

    time.sleep(2)

    return browser.find_element_by_link_text('Groups')

# Read in credentials and chromedriver file path
file = open('credentials.json', 'r')
info = json.loads(file.read())

print "Initializing email autoresponder"

# Log into Google account
loggedIn = None
while not loggedIn:
    try:
        # Set path to the chromedriver
        browser = webdriver.Chrome(info['cdPath'])
        print "Logging into Google account"
        loggedIn = login()
        print "Log in successful"
    except:
        browser.quit()
        print "Failed to login - will try again"

# Do the first action
step1 = None
while not step1:
    try:
        print "Performing first action"
        step1 = firstAction()
        print "First action successful"
    except:
        print "First step failed - will try again"

# Do the second action
step2 = None
while not step2:
    try:
        print "Performing second action"
        step2 = secondAction()
        print "Second action successful"
    except:
        print "Second step failed - will try again"

# Do the third action
step3 = None
while not step3:
    try:
        print "Performaing third action"
        step3 = thirdAction()
        print "Third action successful"
    except:
        print "Third step failed - will try again"

print "Email autoresponder turned on, now closing browser"
browser.close()
print "Browser turned off"
