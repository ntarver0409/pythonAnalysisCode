#importing modules
import os
import csv

#defining pathway
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath) as electionData:

    csvreader = csv.reader(electionData)

     #skipping header row 
    header = next(csvreader)  
    votes = []
    canidates = []

    for row in electionData:
        votes.append(row[0])
        canidates.append(row[2])
    
    numVotes = len(votes)
     







