from pathlib import Path
import csv, requests
#create a function
def overheads_function(forex):
    """
    -This function finds the highest overhead expense and convert the highest overhead expense to SGD
    -This function also finds the category with the highest overhead expense
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
    #create path to current working directory and extend to "csv_reports" where all csv reports are and then extend to "overheads-day-41.csv" file where csv files are 
    file_path=Path.cwd()/"csv_reports"/"overheads-day-41.csv"
    #create empty_list to store all the overhead expense from each category
    empty_list=[]
    #create empty_list_1 to store all the overhead categories and overhead expenses as a dictionary
    empty_list_1=[]
    #open "overheads-day-41.csv" file in read mode
    with file_path.open(mode="r", encoding="UTF-8", newline="")as file:
        #instantiate a reader object
        reader=csv.reader(file)
        #skip the header
        next(reader)
        #for loop to iterate the reader object
        for category in reader:
            #create a dictionary
            empty_dict=dict()
            #assign category as the key
            empty_dict["category"]=category
            #append the empty_dict to empty_list_1 
            empty_list_1.append(empty_dict)
    #open the "overheads-day-41.csv" file in read mode
    with file_path.open(mode="r", encoding="UTF-8", newline="")as file:
        #instantiate a reader object
        reader=csv.reader(file)
        #skip the header
        next(reader)
        #for loop to iterate over the reader object
        for row in reader:
            #obtain all overhead expenses and convert the values from string to float
            empty_list.append(float(row[1]))
            #arrange the values in descending order
            empty_list.sort(reverse=True)
            #obtain the highest value
            highest_overhead=empty_list[0]
    #create a path object with file name "summary_report.txt"
    file_path_1= Path.cwd()/"summary_report.txt"
    #create the file "summary_report.txt" in current working directory
    file_path_1.touch()
    #open "summary_report.txt" file in write mode 
    with file_path_1.open(mode="a") as file:
        #to store all the overhead expenses and overhead categories in a nested list 
        overhead_expense=[value.get('category') for value in empty_list_1]
        #for loop to iterate over the overhead_expense
        for amount in overhead_expense:
            #to find which sublist had the value of the highest overhead expenses
            if float(amount[1])== highest_overhead:
                #convert the highest overhead expense from USD to SGD
                highest_overhead_1= highest_overhead * float(forex)
                #round up the highest overhead expense in SGD to 1 decimal place
                highest_overhead_2=round(highest_overhead_1, 1)
                #to extract out the sub list that contain the highest overhead expenses
                statement_1=amount[0:2] 
                #assign statement_2 as the variable for the overhead category with the highest expense
                statement_2= statement_1[0]   
                #write the f string into the summary_report.txt file 
                file.write(f"[HIGHEST OVERHEADS] {statement_2}: SGD{highest_overhead_2} \n")
