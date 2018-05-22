from selenium import webdriver
import json
import time

# Read in credentials and chromedriver file path
file = open('credentials.json', 'r')
info = json.loads(file.read())

# Set path to the chromedriver
browser = webdriver.Chrome(info['cdPath'])

browser.get('https://accounts.google.com')

time.sleep(1)

email = browser.find_element_by_name('identifier')
email.send_keys(info['username'])
submitEmail = browser.find_element_by_id('identifierNext')
submitEmail.click()

time.sleep(1)

password = browser.find_element_by_name('password')
password.send_keys(info['password'])
submitPassword = browser.find_element_by_id('passwordNext')
submitPassword.click()
