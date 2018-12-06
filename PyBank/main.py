import os
import csv
print(" Financial Analysis ")
print("--------------------------------------")
budgetCSV = os.path.join("." , "Resources", "Budget_Data.csv")
with open(budgetCSV, newline='') as csvfile:
    count = 0
    Total = 0
    
    all_values = []
    profit_change = []
    greatest_increase = 0
    greatest_decrease = 0
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    firstItem = 0
    secondItem = 0
    
    for row in csvreader:
        all_values.append(row[1])
        count = count + 1
        Total = Total + int(row[1])  
        
    
    for index in range(len(all_values)-1):
        
        firstItem = int(all_values[index])
        secondItem = int(all_values[index+1])
        difference = secondItem - firstItem
        profit_change.append(difference)
    
        if difference > greatest_increase:
            greatest_increase = difference
        else:
            greatest_increase = greatest_increase
        
        if difference < greatest_decrease:
            greatest_decrease = difference
        else:
            greatest_decrease = greatest_decrease    
     
    average_Change = sum(profit_change)/(count-1)
    print(f"Total number of months : {count}")
    print(f"Total : {Total}")
    print(f"Average change : {round(average_Change,2)}")
    print(f"Greatest increase in profit : {greatest_increase}")
    print(f"Greatest decrease in profit : {greatest_decrease}")
    


