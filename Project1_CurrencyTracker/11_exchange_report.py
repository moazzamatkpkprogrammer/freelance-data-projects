import csv

filename = "usd_exchange_rates.csv"
currencies = ["PKR","EUR","INR","GBP","AUD","CAD","SAR"]

last_row={}
totals={cur: 0 for cur in currencies}
count = 0

try:
    with open(filename,"r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            count +=1
            for cur in currencies:
                totals[cur] +=float(row[cur])
            last_row = row 
    
    print("\nLatest Exchange Rates( vs USD):")
    for cur in currencies:
        print(f"{cur}: {last_row[cur]}")

    print("\nAverage Exchange Rates (all logs):")
    for cur in currencies:
        avg=totals[cur] / count
        print(f"{cur}: {round(avg,2)}")

except Exception as e:
    print("Error reading file: ",e)