import pandas as pd
import csv
import matplotlib.pyplot as plt

# Läs in CSV-filen
data = pd.read_csv('prices_2018.csv')
print(data)

# Skapa glidande medelvärden för stängningspriset över 20 och 50 dagar
data['SMA_20'] = data['Price'].rolling(window=20).mean()
data['SMA_50'] = data['Price'].rolling(window=50).mean()

# Beräkna RSI (Relativa styrkeindex)
delta = data['Price'].diff()
gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
rs = gain / loss
rsi = 100 - (100 / (1 + rs))
data['RSI'] = rsi

# Beräkna volatiliteten över de senaste 30 dagarna
data['Volatility_30'] = data['Price'].rolling(window=30).std()

# Spara den uppdaterade datan med de nya attributen till en ny CSV-fil
data.to_csv('uppdaterad_borsdata.csv', index=False)

# Skriv ut den uppdaterade datan med de nya attributen
#print(data)

# Beräkna de tre komponenterna i MACD
shortEMA = data['Price'].ewm(span=12, adjust=False).mean() # Kort EMA
longEMA = data['Price'].ewm(span=26, adjust=False).mean() # Lång EMA
MACD = shortEMA - longEMA # MACD-linjen
signal = MACD.ewm(span=9, adjust=False).mean() # Signal-linjen
macd_histogram = MACD - signal # MACD Histogram

# Lägg till MACD-komponenterna som nya kolumner
data['MACD'] = MACD
data['Signal'] = signal
data['MACD_Histogram'] = macd_histogram

# Skriv ut den uppdaterade datan med MACD-komponenterna
print(data)

# Spara den uppdaterade datan med de nya attributen till en ny CSV-fil
data.to_csv('uppdaterad_borsdata.csv', index=False)

# Skapa plotten för MACD och dess komponenter
plt.figure(figsize=(14,7))
plt.plot(data['Date'], data['MACD'], label='MACD', color='blue')
plt.plot(data['Date'], data['Signal'], label='Signal', color='red')
plt.bar(data['Date'], data['MACD_Histogram'], label='MACD Histogram', color='gray')
plt.title('MACD Plot')
plt.xlabel('Date')
plt.ylabel('MACD')
plt.legend()
plt.savefig('MACD_graf.png')  # Spara diagrammet som en bildfil
plt.show()



