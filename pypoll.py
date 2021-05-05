#The data we need to retrieve
# 1. Total number of votes cast
# 2. Complete list of candidates that received votes
# 3. % of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election by popular vote
import csv
import os
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
    #for row in file_reader:

# perform the analysis
