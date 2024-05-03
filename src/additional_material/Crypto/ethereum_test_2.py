data = {
    'prices': [
        [1609459200000, 6077], [1609545600000, 6038], [1609632000000, 6431], [1609718400000, 7926], [1609804800000, 8449],
        [1609891200000, 9023], [1609977600000, 9862], [1610064000000, 10065], [1610150400000, 10087], [1610236800000, 10577],
        [1610323200000, 10470], [1610409600000, 9079], [1610496000000, 8619], [1610582400000, 9444], [1610668800000, 10116],
        [1610755200000, 9856], [1610841600000, 10363]
    ]
}

prices = [price[1] for price in data['prices']]
print(prices)

from datetime import datetime

formatted_data = []

for price_entry in data['prices']:
    epoch_time = price_entry[0] / 1000  # Convert milliseconds to seconds
    date = datetime.utcfromtimestamp(epoch_time).strftime('%Y-%m-%d %H:%M:%S')
    price = price_entry[1]
    formatted_data.append({'date': date, 'price': price})

print(formatted_data)

import csv

# Först skapar vi en lista av listor där varje underlista innehåller datum och pris
formatted_data = []

for price_entry in data['prices']:
    epoch_time = price_entry[0] / 1000  # Convert milliseconds to seconds
    date = datetime.utcfromtimestamp(epoch_time).strftime('%Y-%m-%d %H:%M:%S')
    price = price_entry[1]
    formatted_data.append([date, price])

# Sedan sparar vi datan till en CSV-fil
with open('prices.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date', 'Price'])  # Skriv headers
    writer.writerows(formatted_data)    # Skriv data