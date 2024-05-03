import requests

#url = "https://api.coingecko.com/api/v3/coins/list"
#url = "https://api.coingecko.com/api/v3/coins/ethereum/market_chart/range?vs_currency=sek&from=1609459200&to=1640908800"
url = "https://api.coingecko.com/api/v3/coins/ethereum/market_chart/range?vs_currency=sek&from=1609459200&to=1640908800&precision=0"


headers = {"x-cg-demo-api-key": "CG-TBP3YFKUuCXry1eazwmXUc7A"}

response = requests.get(url, headers=headers)
data=response.json()
print(data)


print("="*20)

prices = [price[1] for price in data['prices']]
print(prices)

# # Extract prices from the data
# prices = [price for _, price in data]

# # Print the list of prices
# print("Bitcoin prices:")
# for price in prices:
#     print(f"${price}")


# daily_averages_list = [ ]
# for i in data:  
#     month_list = i[1]
# print(daily_averages_list)


# values = []
# contents = response['prices']
# for key, value in contents.items():
#      print(key, value['prices'])
#      values.append(value['prices'])
#      print(values)