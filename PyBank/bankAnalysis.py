#importing modules
import os
import csv

#defining pathway
csvpath = os.path.join('Resources', 'budget_data.csv')

def bankTotals(bankData)
    months = int(bankData[0])
    gainsLosses = int(bankData[1])

    

with open(csvpath) as bankRecords

    csvreader = csv.reader(bankRecords, delimiter = ',')

