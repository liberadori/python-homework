import csv
from pathlib import Path

pybankcsv = Path("Resources/budget_data.csv")
output = Path("Resources/budget_output.txt")

pl = []
pl_changes = []
month = []

total_months = 0
total = 0
total_pl_change = 0
initial_pl = 0


with open(pybankcsv, newline="") as file_csv:
    csv_reader = csv.reader(file_csv, delimiter=",")
    csv_header = next(csv_reader)
    
    for row in csv_reader:
        total_months += 1
        
        month.append(row[0])
        
        pl.append(row[1])
        total = total + int(row[1])
        
        final_pl = int(row[1])
        monthly_pl_change = final_pl - initial_pl
        
        pl_changes.append(monthly_pl_change)
        
        total_pl_change = total_pl_change + monthly_pl_change
        initial_pl = final_pl
        
        average_change = (total_pl_change/total_months)
        
        max_pl = max(pl_changes)
        min_pl = min(pl_changes)
        
        max_pl_date = month[pl_changes.index(max_pl)]
        min_pl_date = month[pl_changes.index(min_pl)]
        
    
    print("--------------------------------------------------------------")
    print("Financial Analysis")
    print("--------------------------------------------------------------")
    print(f"Total Months: {total_months}")
    print(f"Total: ${total}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {max_pl_date} ${max_pl}")
    print(f"Greatest Decrease in Profits: {min_pl_date} ${min_pl}")
    print("--------------------------------------------------------------")
    
with open(output, 'w') as csvfile:
    csvfile.write("---------------------------------------------------------\n")
    csvfile.write(f"Financial Analysis\n")
    csvfile.write("---------------------------------------------------------\n")
    csvfile.write(f"Total Months: {total_months}\n")
    csvfile.write(f"Total: {total}\n")
    csvfile.write(f"Average Change: ${average_change}\n")
    csvfile.write(f"Greatest Increase in Profits: {max_pl_date} ${max_pl}\n")
    csvfile.write(f"Greatest Decrease in Profits: {min_pl_date} ${min_pl}\n")
    csvfile.write("---------------------------------------------------------")