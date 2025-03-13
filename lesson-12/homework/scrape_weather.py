from bs4 import BeautifulSoup

with open("weather.html", "r", encoding="utf-8") as file:
    soup = BeautifulSoup(file, "html.parser")

forecast_data = []
rows = soup.find("tbody").find_all("tr")

for row in rows:
    cols = row.find_all("td")
    day = cols[0].text
    temperature = int(cols[1].text.replace("°C", ""))
    condition = cols[2].text
    forecast_data.append({"Day": day, "Temperature": temperature, "Condition": condition})

print("Weather Forecast:")
for data in forecast_data:
    print(f"{data['Day']}: {data['Temperature']}°C, {data['Condition']}")

highest_temp = max(forecast_data, key=lambda x: x["Temperature"])
sunny_days = [d["Day"] for d in forecast_data if d["Condition"] == "Sunny"]

print("\nHottest Day:", highest_temp["Day"], f"({highest_temp['Temperature']}°C)")
print("Sunny Days:", ", ".join(sunny_days))

average_temp = sum(d["Temperature"] for d in forecast_data) / len(forecast_data)
print("\nAverage Temperature:", round(average_temp, 2), "°C")
