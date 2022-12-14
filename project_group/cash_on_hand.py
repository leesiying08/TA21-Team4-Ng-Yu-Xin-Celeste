# import Path method from pathlib
from pathlib import Path
#import csv function
import csv,requests
#cash on hand function
# instantiate an file path object to current working directory
  
def coh_function(forex):
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
    #appending exchange rate into empty list
    exchange_rate_list.append(exchange_rate['Realtime Currency Exchange Rate']["5. Exchange Rate"])
    #access index position 0
    forex=(exchange_rate_list[0])
    # extend to file name 'csv_reports'/'Cash on Hand.csv'
    file_p=Path.cwd()/'csv_reports'/'Cash on Hand.csv'
    # 3. Open file using `with` and `open` keyword in 'read' mode.
    # Include one more parameter, newline="".
    with file_p.open('r', encoding = 'UTF-8', newline = '') as file1:
        # instantiate a reader object
        list= csv.reader(file1)
        # use `next()` to skip the header.
        next(list)
        #empty list for appending
        empty_list=[]
        #empty list for appending
        empty_list1=[]
        #using for loop find line in list
        for line in list:
            #access index 0
            lines=line[0]
            #converting string into integer
            lines4=int(lines)
            #access index 1
            lines2=line[1]
            #append the value to the empty_list.
            empty_list.append(lines2)
            #append the value to the empty_list1.
            empty_list1.append(lines4)
         #create a path object with file name "summary_report.txt"
    file_path_1= Path.cwd()/"summary_report.txt"
    #create the file "summary_report.txt" in current working directory
    file_path_1.touch()
    #open "summary_report.txt" file in write mode 
    with file_path_1.open(mode="a") as file:
        #number of variables in list
        count=len(empty_list1)
        #using for loop in enumerate empty list, starting from index 0
        for count, cash_on_hand in enumerate(empty_list, start=0):
            #find difference between each index within range
            cash_on_hand=[int(empty_list[data+1])-int(empty_list[data]) for data in range(len(empty_list1)-1)]
        #using for loop find n in cash_on_hand
        for n in cash_on_hand:
            #check if it meets condition of n is less than or equal to 0
            if n<=0:
                #check if it meets condition of all values in list are positive
                if all(n >=0 for n in cash_on_hand):
                    #statement to be written in txt if scenario is fulfilled
                   file.write('[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY \n')
                #other condition if above is not applicable    
                elif any(n<=0 for n in cash_on_hand): 
                    #statement to write on txt if condition is fulfilled
                    file.write(f"[CASH DEFICIT] DAY: {empty_list1[cash_on_hand.index(n)]} , AMOUNT: SGD{round((abs(n)*float(forex)),2)} \n")
