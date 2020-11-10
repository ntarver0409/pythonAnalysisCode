#importing modules
import os
import csv

#defining pathway
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, 'r') as bankRecords:

    csvreader = csv.reader(bankRecords, delimiter = ',')
 #skipping header row   
    header = next(csvreader)
#defiining variables 
    months = len(list(csvreader)) #reads all the rows in the csv and outputs that number
    dates = []
    profitLosses = []
    minMax = []
    totalProfit = sum(profitLosses)

#For loop to cycle through each column of data and assign the column to the variable array
    for row in bankRecords:
        dates.append(row[0])
        profitLosses.append(float(row[1])

    
#For loop to compare the dates between the one before and figure out the profits gained or lost
    for i in range(1, len(profitLosses)):
        minMax.append(profitLosses[i] - profitLosses[i-1])
        avgProfitLoss = sum(minMax)/months
        maxProfit = max(minMax)
        minProfit = min(minMax)
        maxDate = str(date[profitLosses.index(maxProfit)])
        minDate = str(date[profitLosses.index(minProfit)])


#Outputting results

    print("Financial Analysis")
    print("---------------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${totalProfit}")
    print(f"Average Change: ${avgProfitLoss}")
    print(f"Greatest Increase in Profits: {maxDate} (${maxProfit})")
    print(f"Greatest Decrease in Profits:  ")


    

