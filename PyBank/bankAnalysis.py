#importing modules
import os
import csv

#defining pathway
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath) as bankRecords:

    csvreader = csv.reader(bankRecords)
 #skipping header row   
    header = next(csvreader)
#defiining variables
    months = len(list(csvreader)) #reads all the rows in the csv and outputs that number
    dates = []
    profitLoss = []
    change = []
    

#For loop to cycle through each column of data and assign the column to the variable array
    for row in bankRecords:
        dates.append(row[0])
        profitLoss.append(float(row[1]))
    
    totalProfit = sum(profitLoss)

    
#For loop to compare the dates between the one before and figure out the profits gained or lost
    for i in range(1, len(profitLoss)):
        change.append(profitLoss[i+1] - profitLoss[i])
        avgProfitLoss = sum(change)/len(change)
        maxProfit = max(change)
        minProfit = min(change)
        maxDate = str(dates[profitLoss.index(maxProfit)])
        minDate = str(dates[profitLoss.index(minProfit)])


#Outputting results

    print(f"Financial Analysis")
    print("---------------------------")
    print(f"Total Months: {months}")
    print(f"Total: ${totalProfit}")
    print(f"Avereage Change: ${avgProfitLoss}")
    print(f"Greatest Increase in Profits: {maxDate} (${maxProfit})")
    print(f"Greatest Decrease in Profits: {minDate} (${minProfit})")


    

