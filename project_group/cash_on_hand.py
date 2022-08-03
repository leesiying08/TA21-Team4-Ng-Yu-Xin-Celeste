# import Path method from pathlib
from pathlib import Path
#import csv function
import csv
# instantiate an file path object to current working directory
# extend to file name 'project_group'/'csv_reports'/'cash-on-hand-usd.csv'
file_p=Path.cwd()/'project_group'/'csv_reports'/'cash-on-hand-usd.csv'
#read and open csv file in file_p 
inputfile=csv.reader(open(file_p,'r'))
# use for loop to iterate over a range object.
for row in inputfile:
    #access index position 1
    rows=row[1]
    #execute print
    print(rows)
        
            
                

        
