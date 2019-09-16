# Dependencies
import csv
import os
from collections import OrderedDict
from operator import itemgetter

inputfile = os.path.join('Resources', 'election_data.csv')
outputfile = os.path.join('Resources', 'election_result_analysis.txt')

votes = 0
winning_votes = 0
total_candidates = 0
most_votes = ["", 0]
candidates = []
candidate_votes = {}


with open(inputfile) as election_data:
    csvreader = csv.DictReader(election_data)

    for row in csvreader:
        votes = votes + 1
        total_candidates = row["Candidate"]        

        if row["Candidate"] not in candidates:
            
            candidates.append(row["Candidate"])

            candidate_votes[row["Candidate"]] = 1
            
        else:
            candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1

    
    print()
    print()
    print()
    print("Election Results")
    print("-------------------------")
    print("Total Votes " + str(votes))
    print("-------------------------")
#results
    for candidate in candidate_votes:
        print(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
        candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
    
candidate_votes

winner = sorted(candidate_votes.items(), key=itemgetter(1), reverse=True)

#results
print("-------------------------")
print("Winner: " + str(winner[0]))
print("-------------------------")





# Output Files
with open(outputfile, "w") as txt_file:
    
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Total Votes " + str(votes))
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    for candidate in candidate_votes:
        txt_file.write(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) +  ")\n ")
    #txt_file.write(str(winner))
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Winner: " + str(winner[0]))
    txt_file.write("\n")
    