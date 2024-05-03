#Här är en metod som använder k-means klusteranalys för att upptäcka likheter i prisdata över månaderna för de fem åren:

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Anta att vi har en DataFrame 'data' som innehåller normaliserade priser för varje månad över fem år
# Varje rad representerar en observation (månad) och innehåller normaliserade priser för varje år

# Exempel på data
data = pd.DataFrame({
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']*5,  # Månad
    'Year': np.repeat(np.arange(2018, 2023), 12),  # År
    'Price': np.random.rand(60)  # Normaliserade priser (exempeldata)
})
print(data)
# Konvertera månader till numeriska värden (för enkelhets skull)
data['Month'] = pd.to_datetime(data['Month'], format='%b').dt.month

# Skapa en array av normaliserade priser för varje månad över fem år
X = data.pivot_table(index='Month', columns='Year', values='Price').values

# Använd k-means för att klustra månader baserat på prisdata
kmeans = KMeans(n_clusters=3, n_init='auto', random_state=42)

#kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(X)

cluster_centers = kmeans.cluster_centers_
print(cluster_centers)

labels = kmeans.labels_
print(labels)


print("Förbereder för plottning...")
# Din plottkod här


# Plotta klustren
plt.figure(figsize=(8, 6))
for i in range(3):
    plt.plot(X[clusters == i].T, label=f'Cluster {i+1}')

plt.xlabel('Månad')
plt.ylabel('Normaliserad Pris')
plt.title('Kluster av Normaliserade Priser för Månader över Fem År')
plt.legend()
plt.savefig('Kluster av Normaliserade Priser för Månader över Fem År.png')
print("Plottkoden har körts.")
print("====")
#plt.show()


# Plotta klustren med scatterplot
plt.figure(figsize=(8, 6))  # Specificera figurens storlek
for i in range(3):
    cluster_data = X[clusters == i]
    plt.scatter(cluster_data[:, 0], cluster_data[:, 1], label=f'Cluster {i+1}')

plt.xlabel('Månad')
plt.ylabel('Normaliserad Pris')
plt.title('Kluster av Normaliserade Priser för Månader över Fem År')
plt.legend()
plt.savefig('Kluster_av_Normaliserade_Priser.png')  # Spara plotten som en bildfil
#plt.show()  # Visa plotten
print("Plottkoden har körts.")
print("====")
