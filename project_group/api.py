import requests
# from pathlib import Path 
url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=RV2RECVPN6VF1SHS"
response = requests.get(url)
#print(response)
data = response.json()


exchange_rate = data
exchange_rate_list = []
for value in exchange_rate:
    exchange_rate_list.append(exchange_rate[value]["5. Exchange Rate"])

statement=(exchange_rate_list[0])
print (statement)
