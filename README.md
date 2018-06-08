# Email Automation

Automating some workflows in Google Groups using the Selenium Python library.

### Installation

1. Download files

2. Create a file called `credentials.json` and provide the encrypted password and username, as well as the three links required

3. Create a file called `email.txt` and provide the email response that will be sent when a support inquiry is made during off hours

4. Create a file called `logs.txt`, which will be used to store the logs for the automation script

### Dependencies

1. selenium

2. schedule

3. Chrome (59 and above)

4. chromedriver

### Windows

* Use `Start-Process <Python executable path> <main.py path>` to start the script as a background process that will run indefinitely.

### Linux
