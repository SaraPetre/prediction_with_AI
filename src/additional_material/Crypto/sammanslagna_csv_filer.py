def ethereum_2018_2022():
    import pandas as pd

    # Ange sökvägarna till CSV-filerna
    file_paths = ['prices_2018.csv', 'prices_2019.csv', "prices_2020.csv", 'prices_2021.csv', 'prices_2022.csv']

    # Skapa en tom DataFrame för att hålla den sammanslagna datan
    combined_data = pd.DataFrame()

    # Loopa igenom varje sökväg och lägg till dess innehåll till den sammanslagna DataFramen
    for file_path in file_paths:
        df = pd.read_csv(file_path)
        combined_data = pd.concat([combined_data, df], ignore_index=True)

    # Skriv den sammanslagna datan till en ny CSV-fil
    combined_data.to_csv('sammanslagen_data.csv', index=False)

    print("Sammanslagen data har sparats till sammanslagen_data.csv")

ethereum_2018_2022()

