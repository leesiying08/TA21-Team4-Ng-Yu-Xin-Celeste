# import Path method from pathlib
from pathlib import Path
#import csv function
import csv,re
file=Path.cwd()/'csv_report'/'profit & loss.csv'
#read and open csv file 

with file.open(mode="r",encoding="UTF-8") as file2:
          #using .read to read file
          text = file2.read()
          # findall() function scans the string from left to right and finds all the matches of the pattern in the string
          add = re.findall(pattern ="Net Profit", string=text)

print(add)

