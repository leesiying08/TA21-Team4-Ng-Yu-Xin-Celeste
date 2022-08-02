from pathlib import Path
import csv, copy
file_path=Path.cwd()/"csv_reports"/"cash-on-hand-usd.csv"
empty_list=[]
empty_list_1 = []
empty_list_2=[]
with file_path.open(mode="r", encoding="UTF-8", newline="") as file:
    reader=csv.reader(file)
    next(reader)
    for value in reader:
        for coh in value:
            empty_list.append(coh)#obtain all value in single list
    for line in reader:
        empty_list_1.append(float(line[1])) #obtain coh value
        empty_list_2 = copy.deepcopy(empty_list_1)
        empty_list_2.sort()
        if empty_list_1 == empty_list_2:
            print("correct")
        else:
            option=3
            option_1=1
            day=2
            while option<len(empty_list):
                diff=empty_list(option)-empty_list(option_1)
                if diff <=0:
                    diff_1=abs(diff)
                    print(f"{day}, {diff_1}")
                    option=option+2
                    option_1=option_1+2
                    day=day+2
                else:
                    option=option+2
                    option_1=option_1+2
                    day=day+2

        
            
                

        
