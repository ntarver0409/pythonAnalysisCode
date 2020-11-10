#importing modules
import os
import csv

#defining pathway
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, 'r') as bankRecords:

    csvreader = csv.reader(bankRecords, delimiter = ',')
    header = next(csvreader)
    lines = len(list(csvreader))
    



    print("Financial Analysis")
    print("----------------------")
    print(f"Total Months: {lines}")
    print

