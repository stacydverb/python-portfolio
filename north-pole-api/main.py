#This program connects to the openweathermap and twilio apis and will send a text if it's snowing at the North Pole.
import requests
from twilio.rest import Client

#Header
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "YOUR_API_KEY"
account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_ROKEN"

#lat/long for North Pole
weather_params = {
    "lat": 90.00,
    "lon": 0.00,
    "appid": api_key,
}

#call weather api, record weather data in json format
response = requests.get(OWM_Endpoint, params=weather_params)
weather_data = response.json()

#set default snow condition to false
will_snow = False

#Access the api data and see if the weather code for snow is between 600-622 (which means it's snowing)
condition_code = weather_data["weather"][0]["id"]
if 600 < int(condition_code) < 622:
    will_snow = True

#if it's snowing, use Twilio to send a text message notifying a user that it's snowing! 
if will_snow:
    print("It's snowing at the North Pole!")
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's snowing at the North Pole Today!",
        from_='OUTGOING_PHONE_NUMBER',
        to='INCOMING_PHONE_NUMBER'
    )
else:
    print("It's not snowing at the North Pole.")
