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

# Open the election results and read the file
with open(file_to_load) as election_data:
# To do: read and analyze the data here.
    file_reader = csv.reader(election_data)
    # Print each row in the CSV file.
    headers = next(file_reader)
    print(headers)
    # for row in file_reader:
    #     print(row)


# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.