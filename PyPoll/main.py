import os
import csv
print("Election Results ")
print("------------------------------")
electionCSV = os.path.join("." , "Resources", "election_data.csv")
with open(electionCSV, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    count = 0
    votes = {}
    percentage = 0
    winner = 0
    for row in csvreader:
        count += 1
        candidates = row[2]
        if candidates in votes:
            votes[candidates] = votes[candidates]+1
        else:
            votes[candidates] = 1
    print(f"Total votes : {count}") 
    print("------------------------------")

    maxVote = max(votes.values())
    for x, y in votes.items():
        percentage = (y/count)
        if y == maxVote:
            winner = x 
        print(x,(" "+"{:.2%}".format(percentage)),"(", y, ")")
    print("------------------------------")
    print(f"Winner : {winner}")
    print("------------------------------")