# Email Automation

Automating some workflows in Google Groups using the Selenium Python library.

### Installation

1. Download files

2. Create a file called `credentials.json` and provide the encrypted password and username, the file paths to the `email.txt` and `logs.txt` file, the path to the Chrome Driver, as well as the three links required:

```
{
  "cdPath"    : "",
  "emailText" : "",
  "logText"   : "",
  "username"  : "",
  "password"  : "",
  "linkOne"   : "",
  "linkTwo"   : "",
  "linkThree" : ""
}

```

3. Create a file called `email.txt` and provide the email response that will be sent when a support inquiry is made during off hours

4. Create a file called `logs.txt`, which will be used to store the logs for the automation script

### Dependencies

1. selenium

2. schedule

3. Chrome (59 and above)

4. chromedriver

5. flask

### Deployment

* Simply run the flask web server using `python app.py`

* The scripts are run depending on which API call is made:
  * `http://localhost:5000/enable` will enable the email automation workflow, and `http://localhost:5000/disable` will disable the email automation workflow

### To Do

* Implement as a production web server
* Refactor to improve readability and performance
