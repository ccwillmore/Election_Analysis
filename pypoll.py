#The data we need to retrieve
# 1. Total number of votes cast
# 2. Complete list of candidates that received votes
# 3. % of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election by popular vote
# add out dependencies
import csv
import os
# set the total_vote variable to 0
total_votes = 0
# create a empty list for the candidates
candidate_name = []
# create a dictionary for the candidate votes
candidate_votes = {}
# create variables to hold the winning candidate, winning count, and the winning percentage
winning_candidate = ""
winning_count = 0
winning_percentage = 0
#assign a name to the path to the source data
file_to_load = os.path.join('Resources','election_results.csv')
# assign a name to the path to the file to write the analysis
file_to_save = os.path.join('analysis','election_analysis.txt')
# open the source data to read
with open(file_to_load,'r') as election_data:
    # read the file
    file_reader = csv.reader(election_data)
    # read and print header row
    headers = next(file_reader)
    print(headers)
    # loop through the rows in the file_reader to collect data
    for row in file_reader:
        total_votes += 1
        candidate = row[2]
        # check if the candidate name is in the candidate name list.  If no then add it
        # increase the number of votes in the candidate_votes dictionary by 1 by using the candidate name as the key
        if candidate not in candidate_name:
            candidate_name.append(candidate)
            candidate_votes[candidate] = 0
        candidate_votes[candidate] += 1
#print(candidate_votes)
#print(f"The total number of votes cast is {total_votes}")
# loop through the candidate_votes dictionary to print out the election returns, determine the winner, and print the winner

with open(file_to_save,'w') as election_output:
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes:  {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    election_output.write(election_results)
    for candidate in candidate_votes:
        election_output.write(f"{candidate}: {(float(candidate_votes[candidate])/float(total_votes)*100.0):,.1f}% ({candidate_votes[candidate]:,})\n")
        if candidate_votes[candidate] > winning_count:
            winning_candidate = candidate
            winning_count = candidate_votes[candidate]
            winning_percentage = float(candidate_votes[candidate])/total_votes*100
    election_output.write(f"-------------------------\n")
    winning_candidate_summary = (
        f"-----------------------\n"
        f"Winner:  {winning_candidate}\n"
        f"Winning vote count:  {winning_count:,}\n"
        f"Winning percentage:  {winning_percentage:.1f}%\n"
        f"------------------------\n")
    election_output.write(winning_candidate_summary)



# perform the analysis
