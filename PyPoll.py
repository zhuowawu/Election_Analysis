# The data we need to retrieve.
# 1. The total number of votes cast.
# 2. A complete list of candidates who received votes.
# 3. The percentage of votes each candidate won.
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.

# Import yje datetime class from the datetime module
import datetime as dt

# Use the now() attribute on the datetime class to get the present time.
now  = dt.datetime.now()

# Print the present time.
print ("The time right now is", now)

# Add our dependencies

import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Candidate options
candidate_options = []

# Declare the empty dictionary
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.

    # Read the file object with the reader funciton.
    file_reader  = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    
    # Add vote counts.
    for row in file_reader:
        # Add to the total voe count
        total_votes += 1

        # Print the candidate ame from each row
        candidate_name  = row[2]

        # If the candidate does not mateh any existing candidate
        if candidate_name not in candidate_options:

            # Add it to the list of candidate
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0

        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

# Determine thw percentage of votes for each candidate by looping through the counts.
# Iterate through the candidate list.  
for candidate_name in candidate_votes:

    # Retrieves vote count of a cnadidate.
    votes = candidate_votes[candidate_name]

    # Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes)* 100

    print (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    
    # Determine winning vote count and candidate
    # Determine if the votes is greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-----------------------------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning vote count: {winning_count:,}\n"
    f"Winning percentage: {winning_percentage:.1f}%\n"
    f"-----------------------------------------------\n")

print (winning_candidate_summary)

#Print the total votes, candidate names, and candidate votes.
#print ("The total number of vote is: ", total_votes)
#print (candidate_options)
#print (candidate_votes)












