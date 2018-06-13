import turnon
import turnoff
import time
import schedule

def job():

    print '\nStarting test 1...'

    #turnon.enable()
    turnoff.disable()

    print '\nTest 1 complete. Starting test 2...'

    turnon.enable()
    #turnoff.disable()

    print '\nTest 2 complete. Testing complete.'

#schedule.every().tuesday.at("14:00").do(job)
schedule.every(3).minutes.do(job)

print 'Initializing tests...'

print 'Tests starting, please stand by.'

#job()

while True:
    schedule.run_pending()
    time.sleep(1)
