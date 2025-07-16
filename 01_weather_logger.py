import requests
import csv
from datetime import datetime

city = input("Enter the name of your city: ")
url=f"https://wttr.in/{city}?format=j1"

try:
    response = requests.get(url)
    data = response.json()

    temp_c = data["current_condition"][0]["temp_C"]
    weather = data["current_condition"][0]["weatherDesc"][0]["value"]
    now = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

    # Write to CSV
    filename = "weather_log.csv"
    with open(filename, "a", newline='') as file:
        writer = csv.writer(file)
        if file.tell() == 0:
            writer.writerow(["Timestamp", "City", "Temperature(C)", "Condition"])
        writer.writerow([now, city, temp_c, weather])

    print(f"{city}: {weather}, {temp_c}°C logged at {now}")

except Exception as e:
    print("Error:", e)
