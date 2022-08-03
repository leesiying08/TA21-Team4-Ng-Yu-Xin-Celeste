# import Path method from pathlib
from pathlib import Path
#import csv function
import csv
file=Path.cwd()/'csv_report'/'profit & loss.csv'
emptylist=[]
emptylist1=[]
#read and open csv file 
with file.open('r', encoding = 'UTF-8', newline = '') as file1:
    # instantiate a reader object
    list= csv.reader(file1)
    # use `next()` to skip the header.
    next(list)
    for stats in list:
        stats1=stats[0]
        stats2=stats[4]
        emptylist.append(stats1)
        emptylist1.append(stats2)
    #number of variables in list
    count=len(emptylist)
    #using for loop in enumerate empty list, starting from index 0
    for count, profit_and_loss in enumerate(emptylist1, start=0):
        #find difference between each index within range
        profit_and_loss=[int(emptylist1[data+1])-int(emptylist1[data]) for data in range(len(emptylist)-1)]
        #using for loop find x in cash_on_hand
        for x in profit_and_loss:
            #create scenario for when x negative
            if x<0:
                #execute print when x is negative
                print(f"[PROFIT DEFICIT] DAY: {emptylist[profit_and_loss.index(x)]} , AMOUNT: SGD{abs(x)}")
        #to break loop
        break
