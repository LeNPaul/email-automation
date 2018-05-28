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

# Read in credentials and chromedriver file path
file = open('credentials.json', 'r')
info = json.loads(file.read())

# Set path to the chromedriver
browser = webdriver.Chrome(info['cdPath'])

# Log into Google account
loggedIn = None
while not loggedIn:
    try:
        loggedIn = login()
    except:
        print "Failed to login - will try again"

#browser.get(info['linkOne'])

#time.sleep(10)

#browser.get(info['linkTwo'])

#time.sleep(10)

#browser.get(info['linkThree'])

# todo: add retry functionality on error
