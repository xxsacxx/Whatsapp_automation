from apiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from msgg import whtsapp_cal_alert_msg
import pickle
def initalize():
    scopes = ['https://www.googleapis.com/auth/calendar']

    flow = InstalledAppFlow.from_client_secrets_file("client_secret.json", scopes=scopes)
    credentials = flow.run_console()


    pickle.dump(credentials, open("token.pkl", "wb")) 
    
def getlatestevnt():
    credentials = pickle.load(open("token.pkl", "rb"))
    print(credentials)
    service = build('calendar', 'v3', credentials=credentials)

    result = service.calendarList().list().execute()
    calendar_id = result['items'][0]['id']


    result = service.events().list(calendarId=calendar_id).execute()
    whtsapp_cal_alert_msg(msg=result['items'][-1]['summary'],tme = result['items'][-1]['start']['dateTime'])
    

getlatestevnt()

