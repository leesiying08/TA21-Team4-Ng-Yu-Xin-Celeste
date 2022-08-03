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
    rows=row[4]
    #execute print
    print(rows)
