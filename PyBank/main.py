import csv
import os
import traceback
from pathlib import Path

# Set path for budget_data.csv file
budget_data = os.path.join(".", "Resources", "budget_data.csv")

# Lists to store data from the first and second column of the csv
dates = []
profitloss = []

with open(budget_data) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)

    # Declare greatprofit and greatloss
    greatprofit = 0
    greatloss = 0
    count = 0

    # Read each row of data after the header
    for row in csvreader:
        count += 1

        # Add dates
        dates.append(row[0])

        # Add profit/losses
        profitloss.append(float(row[1]))

        # Calculate greatest profit value and store corresponding date value in greatprofitdate
        if int(row[1]) > int(greatprofit):
            greatprofit = row[1]
            greatprofitdate = row[0]

        # Calculate greatest loss value and store corresponding date value in greatlossdate
        if int(row[1]) < int(greatloss):
            greatloss = row[1]
            greatlossdate = row[0]


# Create variables for analysis outputs

# Since each row contains a unique value (i.e. unique month/year combination) we can count
# the months by taking the length of the 'dates' list that we have created above
months = len(dates)

# Find total profit by summing column 2 (profitloss)
totalprofit = 0
for pl in range(len(profitloss)):
    totalprofit = totalprofit + profitloss[pl]

# Find average profit/loss by dividing the total profit by the number of entries
avgprofloss = int(totalprofit) / int(months)


# Added formatting to Avg Change to fix trailing zero disappearing on whole tenth rounding result
text = ["Financial Analysis",
        "----------------------------",
        f"Total Months: {months}",
        f'Total: ${round(totalprofit)}',
        f'Average Change: ${"{:.2f}".format(round(avgprofloss,2))}',
        f'Greatest Increase in Profits: {greatprofitdate} (${greatprofit})',
        f"Greatest Decrease in Profits: {greatlossdate} (${greatloss})"]

for outputline in text:
    print(outputline)

# Export a text file with the results
outputpathdir = '/Analysis'
outputpathf = os.path.join(outputpathdir, '/Output.txt')

# Try to create the file in the Analysis folder within this directory.
try:
    with open('./Analysis/Output.txt', 'w') as f:
        f.writelines('\n'.join(text))
        f.close()
# If the folder does not yet exist, create the folder and then create the file
except FileNotFoundError:
    os.mkdir('./Analysis')
    with open('./Analysis/Output.txt', 'w') as f:
        f.writelines('\n'.join(text))
        f.close()
