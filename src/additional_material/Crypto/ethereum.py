


import requests
from datetime import datetime
import csv
import datetime
import matplotlib.pyplot as plt

def calculate_epochtime_to_real_dates():

    # Replace 'epoch_time' with your actual epoch timestamp (in seconds)
    epoch_time_start =1609459200
    epoch_time_end=1640908800

    # Convert epoch time to a human-readable date
    human_readable_date_start = datetime.datetime.utcfromtimestamp(epoch_time_start).strftime('%Y-%m-%d %H:%M:%S')
    human_readable_date_end = datetime.datetime.utcfromtimestamp(epoch_time_end).strftime('%Y-%m-%d %H:%M:%S')
    print(f"Epoch timestamp {epoch_time_start} corresponds to: {human_readable_date_start}")
    print(f"Epoch timestamp {epoch_time_end} corresponds to: {human_readable_date_end}")
calculate_epochtime_to_real_dates()


def ethereum_2018():

    url = "https://api.coingecko.com/api/v3/coins/ethereum/market_chart/range?vs_currency=sek&from=1514764800&to=1546214400&precision=0"
    headers = {"x-cg-demo-api-key": "CG-TBP3YFKUuCXry1eazwmXUc7A"}

    response = requests.get(url, headers=headers)
    data=response.json()
    #print(data)

    #print("="*20)

    # Få ut enbart priser för ethereum. (datum och market-caps sollas bort)
    #prices = [price[1] for price in data['prices']]
    #print(prices)

    # Först skapar vi en lista av listor där varje underlista innehåller datum och pris
    formatted_data_2018 = []

    for price_entry in data['prices']:
        epoch_time = price_entry[0] / 1000  # Convert milliseconds to seconds
        date = datetime.datetime.utcfromtimestamp(epoch_time).strftime('%Y-%m-%d') #%H:%M:%S
        price = price_entry[1]
        formatted_data_2018.append([date, price])

    # Ta bort skottårsvärdet (29 februari)
    formatted_data_2018 = [data for data in formatted_data_2018 if not data[0].endswith('-02-29')]

    # Sedan sparar vi datan till en CSV-fil
    with open('prices_2018.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Price'])  # Skriv headers
        writer.writerows(formatted_data_2018)    # Skriv data

    import matplotlib.pyplot as plt

    # Spara ner en graf över pris

    dates_2018= [entry[0] for entry in formatted_data_2018]
    prices_2018 = [entry[1] for entry in formatted_data_2018]

       # Rensa den aktuella plotten
    plt.clf()  # Eller plt.close() för att stänga plottfönstret helt

    plt.plot(dates_2018, prices_2018)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Price over Time, 2018')
    # Visa endast var tionde datum på x-axeln
    plt.xticks(dates_2018[::10], rotation=45)
    plt.tight_layout()
    plt.savefig('graf_prices_2018.png')  # Spara diagrammet som en bildfil
    #plt.show(block=True)  # Använd block=True för att tvinga interaktivt läge
    #plt.show()

    print("="*20)
    return formatted_data_2018
ethereum_2018()

def ethereum_2019():

    url = "https://api.coingecko.com/api/v3/coins/ethereum/market_chart/range?vs_currency=sek&from=1546300800&to=1577750400&precision=0"
    headers = {"x-cg-demo-api-key": "CG-TBP3YFKUuCXry1eazwmXUc7A"}

    response = requests.get(url, headers=headers)
    data=response.json()
    #print(data)

    #print("="*20)

    # Få ut enbart priser för ethereum. (datum och market-caps sollas bort)
    #prices = [price[1] for price in data['prices']]
    #print(prices)

    # Först skapar vi en lista av listor där varje underlista innehåller datum och pris
    formatted_data_2019 = []

    for price_entry in data['prices']:
        epoch_time = price_entry[0] / 1000  # Convert milliseconds to seconds
        date = datetime.datetime.utcfromtimestamp(epoch_time).strftime('%Y-%m-%d') #%H:%M:%S
        price = price_entry[1]
        formatted_data_2019.append([date, price])

    # Ta bort skottårsvärdet (29 februari)
    formatted_data_2019 = [data for data in formatted_data_2019 if not data[0].endswith('-02-29')]

    # Sedan sparar vi datan till en CSV-fil
    with open('prices_2019.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Price'])  # Skriv headers
        writer.writerows(formatted_data_2019)    # Skriv data

    import matplotlib.pyplot as plt



    # Spara ner en graf över pris

    dates_2019 = [entry[0] for entry in formatted_data_2019]
    prices_2019 = [entry[1] for entry in formatted_data_2019]

    # Rensa den aktuella plotten
    plt.clf()  # Eller plt.close() för att stänga plottfönstret helt
    
    plt.plot(dates_2019, prices_2019)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Price over Time, 2019')
    # Visa endast var tionde datum på x-axeln
    plt.xticks(dates_2019[::10], rotation=45)
    plt.tight_layout()
    plt.savefig('graf_prices_2019.png')  # Spara diagrammet som en bildfil
    #plt.show(block=True)  # Använd block=True för att tvinga interaktivt läge
    #plt.show()

    print("="*20)
    return formatted_data_2019
ethereum_2019()

def ethereum_2020():

    url = "https://api.coingecko.com/api/v3/coins/ethereum/market_chart/range?vs_currency=sek&from=1577836800&to=1609372800&precision=0"
    headers = {"x-cg-demo-api-key": "CG-TBP3YFKUuCXry1eazwmXUc7A"}

    response = requests.get(url, headers=headers)
    data=response.json()
    #print(data)

    #print("="*20)

    # Få ut enbart priser för ethereum. (datum och market-caps sollas bort)
    #prices = [price[1] for price in data['prices']]
    #print(prices)

    # Först skapar vi en lista av listor där varje underlista innehåller datum och pris
    formatted_data_2020 = []

    for price_entry in data['prices']:
        epoch_time = price_entry[0] / 1000  # Convert milliseconds to seconds
        date = datetime.datetime.utcfromtimestamp(epoch_time).strftime('%Y-%m-%d') #%H:%M:%S
        price = price_entry[1]
        formatted_data_2020.append([date, price])

    # Ta bort skottårsvärdet (29 februari)
    formatted_data_2020 = [data for data in formatted_data_2020 if not data[0].endswith('-02-29')]

    # Sedan sparar vi datan till en CSV-fil
    with open('prices_2020.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Price'])  # Skriv headers
        writer.writerows(formatted_data_2020)    # Skriv data

    import matplotlib.pyplot as plt



    # Spara ner en graf över pris

    dates_2020 = [entry[0] for entry in formatted_data_2020]
    prices_2020 = [entry[1] for entry in formatted_data_2020]

    # Rensa den aktuella plotten
    plt.clf()  # Eller plt.close() för att stänga plottfönstret helt
    plt.plot(dates_2020, prices_2020)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Price over Time, 2020')
    # Visa endast var tionde datum på x-axeln
    plt.xticks(dates_2020[::10], rotation=45)
    plt.tight_layout()
    plt.savefig('graf_prices_2020.png')  # Spara diagrammet som en bildfil
    #plt.show(block=True)  # Använd block=True för att tvinga interaktivt läge
    #plt.show()

    print("="*20)
    return formatted_data_2020
ethereum_2020()

def ethereum_2021():

    url = "https://api.coingecko.com/api/v3/coins/ethereum/market_chart/range?vs_currency=sek&from=1609459200&to=1640908800&precision=0"
    headers = {"x-cg-demo-api-key": "CG-TBP3YFKUuCXry1eazwmXUc7A"}

    response = requests.get(url, headers=headers)
    data=response.json()
    #print(data)

    #print("="*20)

    # Få ut enbart priser för ethereum. (datum och market-caps sollas bort)
    #prices = [price[1] for price in data['prices']]
    #print(prices)

    # Först skapar vi en lista av listor där varje underlista innehåller datum och pris
    formatted_data_2021 = []

    for price_entry in data['prices']:
        epoch_time = price_entry[0] / 1000  # Convert milliseconds to seconds
        date = datetime.datetime.utcfromtimestamp(epoch_time).strftime('%Y-%m-%d') #%H:%M:%S
        price = price_entry[1]
        formatted_data_2021.append([date, price])

    # Sedan sparar vi datan till en CSV-fil
    with open('prices_2021.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Price'])  # Skriv headers
        writer.writerows(formatted_data_2021)    # Skriv data

    import matplotlib.pyplot as plt



    # Spara ner en graf över pris

    dates_2021 = [entry[0] for entry in formatted_data_2021]
    prices_2021 = [entry[1] for entry in formatted_data_2021]

    # Rensa den aktuella plotten
    plt.clf()  # Eller plt.close() för att stänga plottfönstret helt
    plt.plot(dates_2021, prices_2021)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Price over Time, 2021')
    # Visa endast var tionde datum på x-axeln
    plt.xticks(dates_2021[::10], rotation=45)
    plt.tight_layout()
    plt.savefig('graf_prices_2021.png')  # Spara diagrammet som en bildfil
    #plt.show(block=True)  # Använd block=True för att tvinga interaktivt läge
    #plt.show()

    print("="*20)
    return formatted_data_2021
ethereum_2021()


def ethereum_2022():

    url = "https://api.coingecko.com/api/v3/coins/ethereum/market_chart/range?vs_currency=sek&from=1640995200&to=1672444800&precision=0"
    headers = {"x-cg-demo-api-key": "CG-TBP3YFKUuCXry1eazwmXUc7A"}

    response = requests.get(url, headers=headers)
    data=response.json()
    #print(data)

    #print("="*20)

    # Få ut enbart priser för ethereum. (datum och market-caps sollas bort)
    prices = [price[1] for price in data['prices']]
    #print(prices)

    # Först skapar vi en lista av listor där varje underlista innehåller datum och pris
    formatted_data_2022 = []

    for price_entry in data['prices']:
        epoch_time = price_entry[0] / 1000  # Convert milliseconds to seconds
        date = datetime.datetime.utcfromtimestamp(epoch_time).strftime('%Y-%m-%d') #%H:%M:%S
        price = price_entry[1]
        formatted_data_2022.append([date, price])

    # Sedan sparar vi datan till en CSV-fil
    with open('prices_2022.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Price'])  # Skriv headers
        writer.writerows(formatted_data_2022)    # Skriv data

 



    # Spara ner en graf över pris

    dates = [entry[0] for entry in formatted_data_2022]
    prices = [entry[1] for entry in formatted_data_2022]

    # Rensa den aktuella plotten
    plt.clf()  # Eller plt.close() för att stänga plottfönstret helt
    plt.plot(dates, prices)
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Price over Time, 2022')
    # Visa endast var tionde datum på x-axeln
    plt.xticks(dates[::10], rotation=45)
    plt.tight_layout()
    plt.savefig('graf_prices_2022.png')  # Spara diagrammet som en bildfil
    #plt.show(block=True)  # Använd block=True för att tvinga interaktivt läge
    #plt.show()

    print("="*20)
    return formatted_data_2022
ethereum_2022()


def ethereum_2018_2022():
    import os
    import glob
    import pandas as pd

 # Ange sökvägarna till CSV-filerna
    file_paths = ['prices_2018.csv', 'prices_2019.csv', "prices_2020.csv", 'prices_2021.csv', 'prices_2022.csv']


    # Lista alla CSV-filer i mappen
    csv_files = glob.glob(os.path.join(file_paths, '*.csv'))

    # Skapa en tom DataFrame för att hålla den sammanslagna datan
    combined_data = pd.DataFrame()

    # Loopa igenom varje CSV-fil och lägg till dess innehåll till den sammanslagna DataFramen
    for file in csv_files:
        df = pd.read_csv(file)
        combined_data = combined_data.append(df, ignore_index=True)

    # Skriv den sammanslagna datan till en ny CSV-fil
    combined_data.to_csv('sammanslagen_data.csv', index=False)
ethereum_2018_2022()


def plotta_kurvor_i_samma_graf():
    
    hämta_lista_2020= ethereum_2020()
    dates = [entry[0] for entry in hämta_lista_2020]
    prices_2020 = [entry[1] for entry in hämta_lista_2020]

    hämta_lista_2021= ethereum_2021()
    dates = [entry[0] for entry in hämta_lista_2021]
    prices_2021 = [entry[1] for entry in hämta_lista_2021]

    hämta_lista_2022= ethereum_2022()
    dates = [entry[0] for entry in hämta_lista_2022]
    prices_2022 = [entry[1] for entry in hämta_lista_2022]

    x=dates
    y1=prices_2020
    y2=prices_2021
    y3=prices_2022

    # Rensa den aktuella plotten
    plt.clf()  # Eller plt.close() för att stänga plottfönstret helt
    # Plotta kurvorna för att visualisera dem
    plt.figure(figsize=(8, 6))
    plt.plot(x, y1, label='Kurva 2020')
    plt.plot(x, y2, label='Kurva 2021')
    plt.plot(x, y3, label='Kurva 2022')
    #plt.yticks([0, 2000, 3000, 4000, 5000])
    plt.xlabel('Dates')
    plt.ylabel('prices')
    plt.title('Jämförelse 2020, 2021,2022')
    plt.legend()
    plt.savefig('jämförelse_kurvor_2020_2021_2022.png') 
    #plt.show()
plotta_kurvor_i_samma_graf()


def normalisera_yaxel_jämföra_kurvor():
    import numpy as np
    import matplotlib.pyplot as plt

    # # Skapa data för kurva 1
    # x1 = np.linspace(0, 10, 100)
    # y1 = np.sin(x1)

    # # Skapa data för kurva 2
    # x2 = np.linspace(0, 20, 200)
    # y2 = np.cos(x2)

    # # Normalisera x-värdena för kurvorna
    # x1_normalized = (x1 - min(x1)) / (max(x1) - min(x1))
    # x2_normalized = (x2 - min(x2)) / (max(x2) - min(x2))

    # plt.clf()  # Eller plt.close() för att stänga plottfönstret helt

    # # Skapa plot
    # plt.plot(x1_normalized, y1, label='Sin(x)')
    # plt.plot(x2_normalized, y2, label='Cos(x)')

    # # Lägg till titel och labels
    # plt.title('Jämförelse av Sin(x) och Cos(x)')
    # plt.xlabel('Normaliserad x')
    # plt.ylabel('y')

    # Visa legenden
    #plt.legend()
    #Spara ner kurvorna i fil
    #plt.savefig('normaliserade_kurvor_2020_2021_2022.png') 

    # Visa plot
   # plt.show()
    
    hämta_lista_2018= ethereum_2018()
    dates = [entry[0] for entry in hämta_lista_2018]
    prices_2018= [entry[1] for entry in hämta_lista_2018]

    hämta_lista_2019= ethereum_2019()
    dates = [entry[0] for entry in hämta_lista_2019]
    prices_2019 = [entry[1] for entry in hämta_lista_2019]

    hämta_lista_2020= ethereum_2020()
    dates = [entry[0] for entry in hämta_lista_2020]
    prices_2020 = [entry[1] for entry in hämta_lista_2020]

    hämta_lista_2021= ethereum_2021()
    dates = [entry[0] for entry in hämta_lista_2021]
    prices_2021 = [entry[1] for entry in hämta_lista_2021]

    hämta_lista_2022= ethereum_2022()
    dates = [entry[0] for entry in hämta_lista_2022]
    prices_2022 = [entry[1] for entry in hämta_lista_2022]

    x=dates
   
    y1=prices_2020
    y2=prices_2021
    y3=prices_2022
    y4=prices_2019
    y5=prices_2018

    # Rensa den aktuella plotten
    plt.clf()  # Eller plt.close() för att stänga plottfönstret helt

    # Konvertera till numpy-arrayer
    y1 = np.array(y1)
    y2 = np.array(y2)       
    y3 = np.array(y3)
    y4 = np.array(y4)
    y5 = np.array(y5)

    # Normalisera y-värdena för kurvorna
    y1_normalized = (y1 - min(y1)) / (max(y1) - min(y1))
    y2_normalized = (y2 - min(y2)) / (max(y2) - min(y2))
    y3_normalized = (y3 - min(y3)) / (max(y3) - min(y3))
    y4_normalized = (y4 - min(y4)) / (max(y4) - min(y4))
    y5_normalized = (y5 - min(y5)) / (max(y5) - min(y5))


    # Skapa plot
    plt.figure(figsize=(8, 6))
    plt.plot(x, y1_normalized, label='Kurva 2020')
    plt.plot(x, y2_normalized, label='Kurva 2021')
    plt.plot(x, y3_normalized, label='Kurva 2022')
    plt.plot(x, y4_normalized, label='Kurva 2019')
    plt.plot(x, y5_normalized, label='Kurva 2018')

    # Lägg till titel och labels
    plt.title('Jämförelse av 2018 - 2022')
    plt.xlabel('Dates')
    plt.ylabel('Normaliserad y')
    plt.legend()
    plt.savefig('jämförelse_normaliserade_kurvor_2018_till_2022.png') 

    # # Plotta kurvorna för att visualisera dem
    # plt.figure(figsize=(8, 6))
    # plt.plot(x, y1, label='Kurva 2020')
    # plt.plot(x, y2, label='Kurva 2021')
    # plt.plot(x, y3, label='Kurva 2022')
    # #plt.yticks([0, 2000, 3000, 4000, 5000])
    # plt.xlabel('Dates')
    # plt.ylabel('prices')
    # plt.title('Jämförelse 2020, 2021,2022')
    # plt.legend()
    # plt.savefig('jämförelse_kurvor_2020_2021_2022.png') 
    # #plt.show()
normalisera_yaxel_jämföra_kurvor()


def prova_modell_linjär():
    from sklearn.linear_model import LinearRegression
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt



    # Läs in datan
    data = {
        'Date': ['2021-01-01', '2021-01-02', ..., '2021-12-30', '2021-12-31'],
        'Price': [6077, 6038, ..., 32909, 33613]
    }

    df = pd.DataFrame(data)

    # Konvertera 'Date' till datetime-format
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

    # Ta bort rader med ogiltiga datum
    df.dropna(subset=['Date'], inplace=True)

    # Konvertera datum till numerisk representation
    df['Numeric Date'] = df['Date'].apply(lambda x: x.timestamp())

    # Skapa en linjär regressionsmodell
    model = LinearRegression()

    # Omvandla datat till numeriskt format
    X = np.array(df['Numeric Date']).reshape(-1, 1)
    y = np.array(df['Price'])

    # Anpassa modellen till datan
    model.fit(X, y)

    # Förutsäg priser med hjälp av modellen
    predicted_prices = model.predict(X)

    # Plotta den ursprungliga datan och den anpassade linjära modellen
    plt.figure(figsize=(10, 6))
    plt.plot(df['Date'], df['Price'], marker='o', linestyle='-', label='Original Data')
    plt.plot(df['Date'], predicted_prices, linestyle='--', color='red', label='Linear Regression Model')
    plt.title('Price Over Time with Linear Regression Model')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('jämföra_med_linjära_modellen.png')
    #plt.show()

   #plt.show()
prova_modell_linjär()

