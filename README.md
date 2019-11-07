# WhatsApp Automation #
![Whatsapp](https://i.imgur.com/Ej4d4WA.jpg)

1 - Use this to get alerts of events from Google Calendar on your WhatsApp

2- External Ip change notification on WhatsApp

3- Schedule your whatsapp message delivery for certain time (don't miss anniversaries,birthdays,follow ups)


 ## File description :
 
 gcal.py : initalize() will get you credentials and store it in token.pkl
            getlatestevnt() will use the creds and fetch the last event added in the google calendar
            
 ip_chk.py : ip_chk() will check if the ip in the file is same as the current ip if not add it
 
 msgg.py : whtsapp_ip_msg()  Ip change notification on WhatsApp
           whtsapp_cal_alert_msg() alerts of events from Google Calendar on your WhatsApp

scheduler.py  : for scheduling any fn at any defined time







![Adding My salt](https://i.imgur.com/uT1QqZj.png)

[TODO: Scrape Fb friends birthdays and send them birthday wishes via whatsapp]

Inspiration credit :

![I Wrote a Script to WhatsApp My Parents Every Morning in Just 20 Lines of Python Code](https://medium.com/better-programming/i-wrote-a-script-to-whatsapp-my-parents-every-morning-in-just-20-lines-of-python-code-5d203c3b36c1)
![IP_CHANGE](https://github.com/coconauts/IP-change/blob/master/ip_change.py)
![Accessing Google Calendar Events Data using Python](https://towardsdatascience.com/accessing-google-calendar-events-data-using-python-e915599d3ae2)

