import time
import schedule
import turnon
import turnoff

# Schedule turning on
schedule.every().monday.at("17:00").do(turnon.enable)
schedule.every().tuesday.at("17:00").do(turnon.enable)
schedule.every().wednesday.at("17:00").do(turnon.enable)
schedule.every().thursday.at("17:00").do(turnon.enable)
schedule.every().friday.at("17:00").do(turnon.enable)

# Schedule turning off
schedule.every().monday.at("9:00").do(turnon.disable)
schedule.every().tuesday.at("9:00").do(turnon.disable)
schedule.every().wednesday.at("9:00").do(turnon.disable)
schedule.every().thursday.at("9:00").do(turnon.disable)
schedule.every().friday.at("9:00").do(turnon.disable)

while True:
    schedule.run_pending()
    time.sleep(10)
