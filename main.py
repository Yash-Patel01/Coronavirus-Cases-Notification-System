from plyer import notification
import requests
from datetime import datetime
# from bs4 import BeautifulSoup
import json
from datetime import date
import time 

def notifyme(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = "C:\\Users\\yashk\\Videos\\work\\CoronaVisrus Notification System\\icon.ico",
        timeout = 20
    )

def getData(url):
    r = requests.get(url)
    return r.json()

if __name__ == "__main__":
    while True:
        myJSONdata = getData("https://api.covid19india.org/states_daily.json")
        datetime = datetime.now()
        today = date.today()
        today= str(today)
        print(type(today))
        for i in myJSONdata.get("states_daily")[-3:]:
            # print(i.get('date'))
            # print("\ntoday date is : ",today) 
            # print('\n')
            # print('\n')
            # if i.get('date')=="07-Aug-20":
            date = i.get('date')
            if i.get('status')=="Recovered":
                Recovered = i.get('gj')
            if i.get('status')=="Confirmed":
                Confirmed = i.get('gj')
            if i.get('status')=="Deceased":
                Deceased = i.get('gj')
        final_string = f"Confirmed : {Confirmed}\nRecovered : {Recovered}\nDeceased  :  {Deceased}\nDate  : {today}"

        notifyme("State : Gujrat",f"Last Update : {date}\n"+final_string)
        time.sleep(3600)