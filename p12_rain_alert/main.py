# Using python-dotenv to store the environment variables
# - Install python-dotenv package using the following command: pip install python-dotenv
# - Create a .env file and store the environment variables in the .env file
# - Create API_KEY, ACCOUNT_SID, AUTH_TOKEN, FROM_ and PHONE_NUMBER variables in the .env file

# Using the openweather api to check the weather condition 
# - Signup to openweather and get the api key
# - Using latlong.net website to get the longitude and latitude of the location
# - Replace the LATITUDE, LONGITUDE and API_KEY with your values

# Using twilio api to send SMS notifications
# - Signup to twilio and get the account_sid and auth_token
# - Generate the twilio phone number
# - Replace the ACCOUNT_SID, AUTH_TOKEN, FROM_ with your values and PHONE_NUMBER with the phone number that you want to send the SMS to
# - Replace the to with the phone number you want to send the SMS to
# - Install twilio package using the following command: pip install twilio

# if the weather condition in the next 12 hours is going to rain, we will send SMS notifications to warn the user

import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast/hourly"
LATITUDE = 43.645031
LONGITUDE = -79.467583

API_KEY = os.getenv("API_KEY")
ACCOUNT_SID = os.getenv("ACCOUNT_SID")
AUTH_TOKEN = os.getenv("AUTH_TOKEN")
FROM_ = os.getenv("FROM_")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")

weather_params = {
    "lat": LATITUDE,
    "lon": LONGITUDE,
    "appid": API_KEY,
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["list"][:12]

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages.create(
            from_=FROM_,
            body='It is going to rain today. Remember to bring an umbrella.',
            to=PHONE_NUMBER
        )
        break