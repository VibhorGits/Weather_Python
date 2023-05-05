import requests
from twilio.rest import Client

open_weather_endpoint = "https://api.openweathermap.org/data/2.8/onecall"
api_key = "5269c17b1ac2399afab64422d37d2e39"
account_sid = "TWILIO ACCOUNT ID"
auth_token = "TWILIO AUTH_TOKEN"

parameters = {
    "lat": 30.316496,
    "lon": 78.032188,
    "appid": api_key,
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get(url=open_weather_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
rain = False

for hourly_data in weather_slice:
    rain_code = hourly_data["weather"][0]["id"]
    if rain_code < 700:
        rain = True

if rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                    .create(
                    body="It's going to rain today.Remember to bring an ☔️",
                    from_="YOUR TEMPORARY TWILIO NUMBER",
                    to="YOUR NUMBER WITH COUNTRY CODE"
                )
    print(message.status)

