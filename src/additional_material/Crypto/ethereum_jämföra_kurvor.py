import numpy as np
import matplotlib.pyplot as plt


# Generera två slumpmässiga kurvor för demonstration
x = np.linspace(0, 10, 100)
y1 = np.sin(x) + np.random.normal(0, 0.1, size=len(x))  # Kurva 1
y2 = np.sin(x + 0.5) + np.random.normal(0, 0.1, size=len(x))  # Kurva 2

# Plotta de två kurvorna för att visualisera dem
plt.figure(figsize=(8, 6))
plt.plot(x, y1, label='Kurva 1')
plt.plot(x, y2, label='Kurva 2')
plt.xlabel('Tid')
plt.ylabel('Värde')
plt.title('Jämförelse av två kurvor')
plt.legend()
plt.savefig('jämförelse_kurvor.png') 
#plt.show()

# Korrelationsanalys
correlation = np.corrcoef(y1, y2)[0, 1]
print("Korrelationskoefficienten mellan kurva 1 och kurva 2:", correlation)

# MSE (Mean Squared Error)
mse = np.mean((y1 - y2)**2)
print("Mean Squared Error mellan kurva 1 och kurva 2:", mse)

import numpy as np
import matplotlib.pyplot as plt

# Generera två slumpmässiga kurvor för demonstration
x = np.linspace(0, 10, 100)
y1 = np.sin(x) + np.random.normal(0, 0.1, size=len(x))  # Kurva 1
y2 = np.sin(x + 0.5) + np.random.normal(0, 0.1, size=len(x))  # Kurva 2

# Fourier-transform av tidsseriedata
fft_y1 = np.fft.fft(y1)
fft_y2 = np.fft.fft(y2)

# Skapa frekvensaxel
N = len(x)
freq = np.fft.fftfreq(N, d=(x[1]-x[0]))

# Plotta amplitudspektrum för de två kurvorna
plt.figure(figsize=(10, 6))
plt.plot(freq[:N//2], np.abs(fft_y1)[:N//2], label='Kurva 1')
plt.plot(freq[:N//2], np.abs(fft_y2)[:N//2], label='Kurva 2')
plt.xlabel('Frekvens')
plt.ylabel('Amplitud')
plt.title('Frekvensanalys av två kurvor')
plt.legend()
plt.savefig('Frekvensanalys.png') 
#plt.show()


import numpy as np
import matplotlib.pyplot as plt

# Skapa en sinusliknande tidsserie
t = np.linspace(0, 10, 1000)
y = np.sin(2 * np.pi * 1 * t) + 0.5 * np.sin(2 * np.pi * 2 * t) + 0.3 * np.sin(2 * np.pi * 5 * t)

# Utför Fourier-transformen
fft_y = np.fft.fft(y)
N = len(y)
freq = np.fft.fftfreq(N, d=(t[1]-t[0]))

# Plotta frekvensspektrumet
plt.figure(figsize=(10, 6))
plt.plot(freq[:N//2], np.abs(fft_y)[:N//2])
plt.xlabel('Frekvens')
plt.ylabel('Amplitud')
plt.title('Frekvensspektrum')
plt.grid(True)
plt.savefig('exempel_Frekvensanalys.png') 
#plt.show()
