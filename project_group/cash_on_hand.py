from pathlib import Path
import csv
file_p=Path.cwd()/'project_group'/'csv_reports'/'cash-on-hand-usd.csv'
inputfile=csv.reader(open(file_p,'r'))
for row in inputfile:
    rows=row[1]
    print(rows)
        
            
                

        
