import requests
# from pathlib import Path 
url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=RV2RECVPN6VF1SHS"
response = requests.get(url)
#retrieve data with .json from response 
data = response.json()
#Save data as exchange_rate
exchange_rate = data
#create empty list for appending
exchange_rate_list = []
#Use for loop to iterate over a range object.
for value in exchange_rate:
    #appending exchange rate into empty list
    exchange_rate_list.append(exchange_rate[value]["5. Exchange Rate"])
#access index position 0
statement=(exchange_rate_list[0])
#print statement
print (statement)
# file_path=Path.cwd()/"summary_report.txt"
# file_path.touch()

# with file_path.open(mode="w") as file:
#     for value_1 in exchange_rate_list:
#         file.write(f"[REAL TIME CURRENCY CONVERSION RATE] USD1 - SGD{value_1}")
