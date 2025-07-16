import requests
import csv
from datetime import datetime
import time

url = "https://open.er-api.com/v6/latest/USD"
filename = "usd_exchange_rates.csv"
currencies = ["PKR", "EUR", "INR", "GBP", "AUD", "CAD", "SAR"]

# Write header only once at start
with open(filename, "w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp"] + currencies)

# Loop 5 times to log rates
for i in range(5):
    try:
        response = requests.get(url)
        data = response.json()

        if data["result"] == "success":
            rates = {cur: data["rates"].get(cur, "N/A") for cur in currencies}
            now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(filename, "a", newline='') as file:
                writer = csv.writer(file)
                writer.writerow([now] + [rates[cur] for cur in currencies])

            print(f"[{i+1}/5] Logged at {now}")

        else:
            print(" API Error:", data.get("error-type"))

    except Exception as e:
        print(" Error:", e)

    time.sleep(2)  # Add a 2-second delay between requests (optional)
