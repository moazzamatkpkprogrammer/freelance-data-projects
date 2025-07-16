import csv
import matplotlib.pyplot as plt

filename = "usd_exchange_rates.csv"
currencies = ["PKR","EUR","INR","GBP","AUD","CAD","SAR"]
latest_rates = {}

try:
    with open(filename, "r") as file:
        reader = list(csv.DictReader(file))
        if not reader:
            print("CSV is empty!")
            exit()

        last_row = reader[-1]
        for cur in currencies:
            latest_rates[cur] = float(last_row[cur])


        plt.figure(figsize=(10,6))
        plt.bar(latest_rates.keys(),latest_rates.values(), color="skyblue")

        plt.title("Latest Exchange Rates vs USD")
        plt.xlabel("Currency")
        plt.ylabel("Exchange Rate")
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        # Annotate values
        for i, (cur, val) in enumerate(latest_rates.items()):
            plt.text(i, val + 0.2, f"{val:.2f}", ha='center', fontsize=9)

        plt.tight_layout()
        plt.savefig("latest_exchange_rates.png")  # Save as image
        plt.show()

except Exception as e:
    print("Error:", e)