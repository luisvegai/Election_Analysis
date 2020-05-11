# Add our dependencies.
# import random
# import numpy
import os
import csv

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Using the open() function with the "w" mode we will write data to the file.
# Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#     # Write some data to the file.
#     txt_file.write("Counties in the Election\n------------------")
#     txt_file.write("\nArapahoe\nDenver\nJefferson")

# The data we need to retrieve.
# Assign a variable for the file to load and the path.
# file_to_load = 'Resources/election_results.csv'
file_to_load = os.path.join("Resources", "election_results.csv")
# election_data = open(file_to_load, 'r')

# 1. Initialize a total vote counter.
total_votes = 0
# Candidate Options
candidate_options = []
# County Options
county_options = []
# Declare the empty dictionary.
candidate_votes = {}
county_votes = {}
largest_county_voting = ""
largest_county_count = 0
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file
with open(file_to_load) as election_data:
# To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    # Print each row in the CSV file.
    headers = next(file_reader)
    # print(headers)
    for row in file_reader:
        # print(row)
        # Add to the total vote count.
        total_votes += 1
        # Print the candidate name from each row.
        county_name = row[1]
        candidate_name = row[2]
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0
             # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        if county_name not in county_options:
            # Add it to the list of candidates.
            county_options.append(county_name)
            # Begin tracking that candidate's vote count. 
            county_votes[county_name] = 0
             # Add a vote to that candidate's count.
        county_votes[county_name] += 1
with open(file_to_save, "w") as txt_file:
# Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)

    for county_name in county_votes:
        # 2. Retrieve vote count in county.
        votes_c = county_votes[county_name]
        # 3. Calculate the percentage of votes.
        vote_c_percentage = int(votes_c) / int(total_votes) * 100
        # The percentage of votes each candidate won
        # print(f"{candidate}: received {vote_percentage:.1f}% of the vote.") 
        # print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        county_results = (f"{county_name}: {vote_c_percentage:.1f}% ({votes_c:,})\n")
        if (county_name == county_options[0]):
            county_summary = (
                f"\n"
                f"County Votes\n"
                f"{county_results}")
            print(county_summary)
            txt_file.write(county_summary)
        elif (county_name == county_options[-1]):
            county_summary = (
                f"{county_results}\n")
            print(county_summary)
            txt_file.write(county_summary)
        else:
            print(county_results)
            txt_file.write(county_results)
        if (votes_c > largest_county_count):
            largest_county_count = votes_c
            largest_county_voting = county_name
    county_voting_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {largest_county_voting}\n"
        f"-------------------------\n")
    print(county_voting_summary)
    txt_file.write(county_voting_summary)
# Determine the percentage of votes for each candidate by looping through the counts.
# 1. Iterate through the candidate list.
    for candidate in candidate_votes:
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate]
        # 3. Calculate the percentage of votes.
        vote_percentage = int(votes) / int(total_votes) * 100
        # The percentage of votes each candidate won
        # print(f"{candidate}: received {vote_percentage:.1f}% of the vote.") 
        # print(f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
        txt_file.write(candidate_results)
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate  
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
# print(winning_candidate_summary)


# print(total_votes)
# print(candidate_options)

# Print the candidate vote dictionary.
# print(candidate_votes)


