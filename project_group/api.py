import requests
from pathlib import Path
#create function
def api_function():
    """
    -This function finds the real time exchange rate from api call
    -This function has no parameter.
    """
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
        #create a path object with file name "summary_report.txt" 
        file_path= Path.cwd()/"summary_report.txt"
        #create the file "summary_report.txt" in the current working directory
        file_path.touch()
        #open the "summary_report.txt" file in write mode
        with file_path.open(mode="w") as file:
            #write the f string into the "summary_report.txt" file
            file.write(f"[REAL TIME CURRENCY CONVERSION RATE] USD1 = SGD{float(statement)} \n")
#activate function
api_function()

