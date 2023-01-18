import csv
import os
import traceback
from pathlib import Path

# Set path for budget_data.csv file
election_data = os.path.join(".", "Resources", "election_data.csv")

# Lists to store data from the first and second column of the csv
ballotid = []
county = []
candidate = []

with open(election_data) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Start count at 0
    count = 0
    currentcandidate = 0
    currentcanvotes = 0

    # Declare unique candidate
    uniquecandidate = []
    uniquecanvotes = []

    # # Read each row of data after the header
    for row in csvreader:
        count += 1
        currentcanvotes += 1

        # Add Ballot Id
        ballotid.append(row[0])

        # Add County
        county.append(row[1])

        # Add Candidate if unique to uniquecandidate list
        candidate.append(row[2])
        if row[2] not in uniquecandidate:
            uniquecandidate.append(row[2])
            currentcandidate += 1
            currentcanvotes = 1
            uniquecanvotes.append(0)

        # Add votes for candidates
        uniquecanvotes[currentcandidate - 1] = int(currentcanvotes)

    # Create first text list with Title and Total vote count
    text1 = ["Election Results",
             "----------------------------",
             f"Total Votes: {count}",
             "----------------------------"]

    # Create second text list that will adjust number of lines based on number of unique candidates
    # Each line includes the candidates name, their percentage share of the votes and their vote count
    text2 = []
    winnervotes = 0
    numcan = len(uniquecandidate)

    for j in range(numcan):
        votepercent = "{:.3f}%".format(uniquecanvotes[j] / (count / 100))
        text2.append(
            f'{uniquecandidate[j]}: {votepercent} ({uniquecanvotes[j]})')
        if uniquecanvotes[j] > winnervotes:
            winner = uniquecandidate[j]
        winnervotes = uniquecanvotes[j]

    # Create third text list
    text3 = ["----------------------------",
             f"Winner: {winner}",
             "----------------------------"]

    # Combine all three text lists
    [text1.extend(q) for q in (text2, text3)]

# Print combined output as per instructions
for outputline in text1:
    print(outputline)

# Export a text file with the results
outputpathdir = '/Analysis'
outputpathf = os.path.join(outputpathdir, '/Output.txt')

# Try to create the file in the Analysis folder within this directory.
try:
    with open('./Analysis/Output.txt', 'w') as f:
        f.writelines('\n'.join(text1))
        f.close()
# If the folder does not yet exist, create the folder and then create the file
except FileNotFoundError:
    os.mkdir('./Analysis')
    with open('./Analysis/Output.txt', 'w') as f:
        f.writelines('\n'.join(text1))
        f.close()
