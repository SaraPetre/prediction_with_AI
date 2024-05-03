
import requests
from datetime import datetime
import csv
import datetime
import matplotlib.pyplot as plt
import pandas as pd


def ethereum_history_365_days():



    url = "https://api.coingecko.com/api/v3/coins/ethereum/ohlc?vs_currency=sek&days=365&precision=0"

    headers = {"x-cg-demo-api-key": "CG-TBP3YFKUuCXry1eazwmXUc7A"}

    response = requests.get(url, headers=headers)
    data=response.json()
   # print(data)

    # Skapa en DataFrame från JSON-data
    df = pd.DataFrame(data, columns=['timestamp', 'open', 'high', 'low', 'close'])


    # Konvertera timestamp till riktiga datum
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

    # Spara DataFrame till CSV-fil
    df.to_csv('ethereum_ohlc.csv', index=False)

    print("Data sparad till ethereum_ohlc.csv")



    url = "https://api.coingecko.com/api/v3/coins/ethereum/market_chart/range?vs_currency=sek&from=1680048000&to=1711411200"

    headers = {"x-cg-demo-api-key": "CG-TBP3YFKUuCXry1eazwmXUc7A"}

    response = requests.get(url, headers=headers)

    data=response.json()
    # Extrahera relevant data från JSON-svaret
    timestamps = [entry[0] for entry in data['prices']]
    prices = [entry[1] for entry in data['prices']]
    total_volumes = [entry[1] for entry in data['total_volumes']]

    # Skapa en DataFrame
    df = pd.DataFrame({'timestamp': timestamps, 'price': prices, 'total_volumes': total_volumes})

    # Konvertera timestamp till riktiga datum
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')

    # Spara DataFrame till CSV-fil
    df.to_csv('ethereum_market_data_subset.csv', index=False)


    # Läs in den första CSV-filen utan total_volumes
    df_without_volumes = pd.read_csv('ethereum_ohlc.csv')

    # Läs in den andra CSV-filen med total_volumes
    df_with_volumes = pd.read_csv('ethereum_market_data_subset.csv')

    # Slå ihop DataFrames baserat på timestamp
    df_merged = pd.merge(df_without_volumes, df_with_volumes, on='timestamp', how='inner')

    # Spara den sammanslagna DataFrame till en ny CSV-fil
    df_merged.to_csv('ethereum_combined_data.csv', index=False)

    print("Data sparad till ethereum_combined_data.csv")

    

# ethereum_history_365_days()

    