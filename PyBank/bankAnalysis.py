#importing modules
import os
import csv

#defining pathway
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, 'r+') as bankRecords:

    csvreader = csv.reader(bankRecords)
 #skipping header row   
    header = next(csvreader)
#defiining variables
    dates = []
    profitLoss = []
    change = []
    


#For loop to cycle through each column of data and assign the column to the variable array
    for row in csvreader:
        dates.append(row[0])
        profitLoss.append(float(row[1]))
    
    months = len(dates)
    totalProfit = sum(profitLoss)

    
#For loop to compare the dates between the one before and figure out the profits gained or lost
    for i in range(1, len(profitLoss)):
        change.append(profitLoss[i] - profitLoss[i-1])

        avgProfitLoss = (sum(change)/len(change))
        maxProfit = max(change)
        minProfit = min(change)
        maxDate = str(dates[change.index(maxProfit)])
        minDate = str(dates[change.index(minProfit)])


#Outputting results

    print(f"Financial Analysis")
    print("---------------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${totalProfit}")
    print(f"Average Change: ${round(avgProfitLoss)}")
    print(f"Greatest Increase in Profits: {maxDate} (${maxProfit})")
    print(f"Greatest Decrease in Profits: {minDate} (${minProfit})")

#writing my results to a .txt file
with open("bankOutput.txt", "w") as f:
    print(f"Financial Analysis", file=f)
    print("---------------------------", file=f)
    print(f"Total Months: {months}", file=f)
    print(f"Total: ${totalProfit}", file=f)
    print(f"Average Change: ${round(avgProfitLoss)}", file=f)
    print(f"Greatest Increase in Profits: {maxDate} (${maxProfit})", file=f)
    print(f"Greatest Decrease in Profits: {minDate} (${minProfit})", file=f)