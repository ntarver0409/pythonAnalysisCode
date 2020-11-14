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
    khanCount = 0
    correyCount = 0
    liCount = 0
    tooleyCount = 0

    for row in csvreader:
        votes.append(row[0])
        canidates.append(row[2])
        #Counting the number of votes of each canidate
        if row[2] == "Khan":
            khanCount = khanCount + 1
        elif row[2] == "Correy":
            correyCount = correyCount + 1
        elif row[2] == "Li":
            liCount = liCount + 1
        else:
            tooleyCount = tooleyCount + 1
            
    
    numVotes = len(votes)
#Finding the canidates vote percentage and formatting it 
    khanPercent = "{:.3%}".format(khanCount/numVotes)
    correyPercent = "{:.3%}".format(correyCount/numVotes)
    liPercent = "{:.3%}".format(liCount/numVotes)
    tooleyPercent = "{:.3%}".format(tooleyCount/numVotes)









print(f"Election Results")
print("-------------------------")
print(f"Total Votes: {numVotes}")
print("-------------------------")
print(f"Khan: {khanPercent} ({khanCount})")


     







