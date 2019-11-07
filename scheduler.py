import schedule
import time
from ip_chk import ip_chk
from gcal import getlatestevnt

schedule.every().day.at("02:29").do(getlatestevnt)
while True:
    schedule.run_pending()
    time.sleep(1)