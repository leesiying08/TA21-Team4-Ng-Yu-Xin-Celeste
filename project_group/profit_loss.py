# import Path method from pathlib
from pathlib import Path
#import csv function
import csv
file=Path.cwd()/'csv_report'/'profit & loss.csv'
#read and open csv file 
inputfile=csv.reader(open(file,'r'))
# use for loop to iterate over a range object.
for row in inputfile:
    #access index position 4
    net_profit=row[4]
    #execute print
    print(net_profit)
    # instantiate a reader object
    list= csv.reader(net_profit)
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
    #number of variables in list
    count=len(empty_list1)
    #using for loop in enumerate empty list, starting from index 0
    for count, cash_on_hand in enumerate(empty_list, start=0):
        #find difference between each index within range
        cash_on_hand=[int(empty_list[data+1])-int(empty_list[data]) for data in range(len(empty_list1)-1)]
        #using for loop find x in cash_on_hand
        for x in cash_on_hand:
            #create scenario for when x negative
            if x<0:
                #execute print when x is negative
                print(f"[CASH DEFICIT] DAY: {empty_list1[cash_on_hand.index(x)]} , AMOUNT: SGD{abs(x)}")
        #to break loop
        break
