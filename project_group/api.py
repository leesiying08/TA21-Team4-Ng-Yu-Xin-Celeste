import requests
# from pathlib import Path 
url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=RV2RECVPN6VF1SHS"
response = requests.get(url)
#print(response)
data = response.json()
print(data)

exchange_rate = data
exchange_rate_list = []
for value in exchange_rate:
    exchange_rate_list.append(exchange_rate[value]["5. Exchange Rate"])

statement=(f"[REAL TIME CURRENCY CONVERSION RATE] USD1 - SGD{exchange_rate_list[0]}")
print (statement)
# file_path=Path.cwd()/"summary_report.txt"
# file_path.touch()

# with file_path.open(mode="w") as file:
#     for value_1 in exchange_rate_list:
#         file.write(f"[REAL TIME CURRENCY CONVERSION RATE] USD1 - SGD{value_1}")
