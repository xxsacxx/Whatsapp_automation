import schedule
import time
from ip_chk import ip_chk
from gcal import getlatestevnt
#you will get last event added to your calendar at morning 7
schedule.every().day.at("07:00").do(getlatestevnt)
while True:
    schedule.run_pending()
    time.sleep(1)
