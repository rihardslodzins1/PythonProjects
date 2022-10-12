import requests

parameters = {
    "lat": 56.92,
    "lon": 24.075,
    "appid": "f14cd19a8ea335c9561b316f60c4d9d1",
}

response = requests.get("https://api.openweathermap.org/data/2.5/weather")

print(response.json())