import requests
import time

url = 'https://api.binance.com/api/v3/ticker/price'

response = requests.get(url, params={'symbol': 'BTCUSDT'})

price_obj = response.json()

price = float(price_obj['price'])
print(price)

prices_list = []

for i in range(10):
    response = requests.get(url, params={'symbol': 'BTCUSDT'})
    price = float(response.json()['price'])
    prices_list.append(price)
    time.sleep(1)

print(prices_list)
print(max(prices_list))
