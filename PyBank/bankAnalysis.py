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

#For loop to cycle through each column of data and assign the column to the variable array
    for row in bankRecords:
        dates.append(row[0])
        profitLosses.append(row[1])

    for i in range(1, len(minMax)):







    



    print("Financial Analysis")
    print("----------------------")
    print(f"Total Months: {months}")
    

