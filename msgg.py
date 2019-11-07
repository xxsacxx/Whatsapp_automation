from twilio.rest import Client
import logging
import os
from datetime import datetime

#logging
logger = logging.getLogger(__name__)  
here = os.path.dirname(os.path.abspath(__file__))
#here = os.path.dirname(os.path.abspath(__file__))
log_file = os.path.join(here, 'ip_chkr.log')
# set log level
logger.setLevel(logging.DEBUG)
# define file handler and set formatter
file_handler = logging.FileHandler(log_file)
formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


twilio_sid = 'ACb9ed233b3bf68750f92f519d751a3e2a'
auth_token = '5852af92fa65660da6369c76f588faec'
whatsapp_client = Client(twilio_sid, auth_token)

def whtsapp_ip_msg(ip,event=None, context=None):

    # get your sid and auth token from twilio


    

    # keep adding contacts to this dict to send
    # them the message
    contact_directory = {'Shashi':'+919440585819'}

    for key, value in contact_directory.items():
        
        people = whatsapp_client.messages.create(
                body = 'ip has changed to  {} '.format(ip),
                from_= 'whatsapp:+14155238886',
                to='whatsapp:' + value,

            )

        logger.info(people.sid)

def whtsapp_cal_alert_msg(msg,tme,event=None, context=None):
    tme = (tme.split('T'))[0]
    tme = datetime.strptime(tme, '%Y-%m-%d')
    contact_directory = {'Sachin':'+918840372022'}
    logger.info('sending message as {0}'.format(msg))
    for key, value in contact_directory.items():
            
            people = whatsapp_client.messages.create(
                    body = 'your recent event is {0} which is starting at {1}'.format(msg,tme),
                    from_= 'whatsapp:+14155238886',
                    to='whatsapp:' + value,

                )

            logger.info(people.sid)

