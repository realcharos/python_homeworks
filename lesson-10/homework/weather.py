import requests

API_KEY = "3204f2af8b9a7746aafd6630e626989c"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter city name: ")

try:
    response = requests.get(BASE_URL, params={"q": city, "appid": API_KEY, "units": "metric"})
    response.raise_for_status()
    data = response.json()

    if data.get("cod") == "404":
        print("City not found! Please check the spelling.")
    else:
        weather = data["weather"][0]["description"]
        temp = data["main"]["temp"]
        print(f"Weather in {city}: {weather}, {temp}°C")
except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error: {http_err}")
except requests.exceptions.RequestException as req_err:
    print(f"Request error: {req_err}")
except ValueError:
    print("Error parsing weather data!")
