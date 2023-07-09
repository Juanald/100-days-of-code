"""
The following is the code for a telegram bot to send a message in the case of rain. It uses the openweathermap and telegram apis in order to do this. To use this for your own purposes, create an api key for openweather and your bot. Access bot chat_id, and get the longitude and latitude of your desired location (can be done via the geocoding api). It checks every three hours worth of weather data.
"""

import requests
api_key = ""
bot_token = ""
chat_id = ""
location = ()

def telegram_bot_sendtext(bot_message):
    global bot_token, chat_id
    token = bot_token
    bot_chatID = chat_id
    send_text = f"https://api.telegram.org/bot{token}/sendMessage?chat_id={bot_chatID}&parse_mode=Markdown&text={bot_message}"

    response = requests.get(send_text)
    response.raise_for_status()

    return response.json()

weather_params = {
    "lat" : location[0],
    "lon" : location[1],
    "appid" : api_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=weather_params)
response.raise_for_status()

data = response.json()['list'] # converted into a list

for i in range(4):
    id = data[i]['weather'][0]['id']
    time = data[i]['dt_txt']
    if id < 700:
        telegram_bot_sendtext(f"It's going to rain today at {time}! Bring an ☂️!") # Send a messsage to the desired chat