import requests
from datetime import datetime
from dateutil.parser import isoparse
import time as t
import smtplib

def datetime_from_utc_to_local(utc_datetime):
    now_time = t.time()
    offset = datetime.fromtimestamp(now_time) - datetime.utcfromtimestamp(now_time)
    return utc_datetime + offset

My_LAT = 43.731548
MY_LNG = -79.762421

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

iss_longitude = float(response.json()['iss_position']['longitude'])
iss_latitude = float(response.json()['iss_position']['latitude'])

iss_pos = (iss_latitude, iss_longitude)
print(iss_pos)

parameters = {
    "lat": My_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = isoparse(data['results']['sunrise'])
sunset = isoparse(data['results']['sunset'])

sunrise = datetime_from_utc_to_local(sunrise).hour
sunset = datetime_from_utc_to_local(sunset).hour

time_now = datetime.now().hour

# if iss close to my position +- 5 degrees and night, send email. Run every 60 seconds
if (abs(iss_longitude - My_LAT) <= 5 or abs(iss_latitude - My_LAT) <= 5) and (time_now >= sunset or time_now <= sunrise):
    sender = "bobjohnson@gmail.com"
    receiver = "barackobama@gmail.com"
    message = """
    Subject: International Space Station!\n\n
    The ISS is currently in your vicinity! Look up!
    """
    with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
        server.starttls()
        server.login("e15c7327a57750", "********dbe8")
        server.sendmail(from_addr=sender, to_addrs=receiver, msg=message)
        print("Message sent!")
