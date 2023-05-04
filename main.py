import requests

open_weather_endpoint = "https://api.openweathermap.org/data/2.8/onecall"

parameters = {
    "lat": 30.316496,
    "lon": 78.032188,
    "appid": "5269c17b1ac2399afab64422d37d2e39",
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get(url=open_weather_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
print(weather_slice)
rain = False

for hourly_data in weather_slice:
    rain_code = hourly_data["weather"][0]["id"]
    print(rain_code)
    if rain_code < 700:
        rain = True

if rain:
    print("Bring an Umbrella")