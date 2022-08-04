# import Path method from pathlib
from pathlib import Path
#import csv function
import csv,requests
#create function for profit_loss
def profitloss_function():
    # instantiate an file path object to current working directory
    """
    -This function finds whether there is a surplus or deficit of cash on hand and convert the cash on hand to SGD
    -This function also finds the day where the deficit happened.
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
        forex=(exchange_rate_list[0])
    file=Path.cwd()/'project_group'/'csv_reports'/'profit-and-loss-usd .csv'
    #read and open csv file 
    with file.open('r', encoding = 'UTF-8', newline = '') as file1:
    # instantiate a reader object
        list= csv.reader(file1)
        # use `next()` to skip the header.
        next(list)
        emptylist=[]
        emptylist1=[]
        for stats in list:
            stats1=stats[0]
            stats2=stats[4]
            emptylist.append(stats1)
            emptylist1.append(stats2)
    file_path_1= Path.cwd()/'project_group'/'summary_report2.txt'
    #create the file "summary_report.txt" in current working directory
    file_path_1.touch()
    #open "summary_report.txt" file in write mode     
    with file_path_1.open(mode="w") as file:
        #number of variables in list
        count=len(emptylist)
        #using for loop in enumerate empty list, starting from index 0
        for count, cash_on_hand in enumerate(emptylist1, start=0):
            #find difference between each index within range
            profit_and_loss=[int(emptylist1[data+1])-int(emptylist1[data]) for data in range(len(emptylist)-1)]
             #using for loop find x in cash_on_hand
        for n in profit_and_loss:
            #check if it meets condition of n is less than or equal to 0
            if n<=0:
                #check if it meets condition of all values in list are positive
                if all(n >=0 for n in profit_and_loss):
                   #statement to be written in txt if scenario is fulfilled
                   file.write('[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY \n')
                 #other condition if above is not applicable      
                elif any(n<=0 for n in profit_and_loss): 
                    #statement to write on txt if condition is fulfilled
                    file.write(f"[PROFIT DEFICIT] DAY: {emptylist[profit_and_loss.index(n)]} , AMOUNT: SGD{round((abs(n)*float(forex)),2)} \n")
#execute function                
print(profitloss_function())
