import requests

API_KEY = "3204f2af8b9a7746aafd6630e626989c"
CITY = "Tashkent"
URL = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
if response.status_code == 200:
    data = response.json()
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    description = data["weather"][0]["description"]

    print(f"Weather in {CITY}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {description.capitalize()}")
else:
    print("Error fetching weather data!")
