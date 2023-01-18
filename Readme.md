# python-challenge
Module 3 Challenge: Financial and Polling Data Analysis

## Summarizing Financial and Polling Data using Python

For this challenge, two separate scripts were created in order to analyze two unique datasets:
1. [budget_data.csv](https://github.com/zmoloci/python-challenge/blob/main/PyBank/Resources/budget_data.csv)
  - Monthly profit/loss records for a company. Organized into two columns: "Date" (mmm-yy), "Profit/Losses" (int)
2. [election_data.csv](https://github.com/zmoloci/python-challenge/blob/main/PyPoll/Resources/election_data.csv)
  - Election data for a number of counties organized into three columns: "Voter ID", "County", and "Candidate"



### PyBank - Analyzing Monthly Profit/Loss Records

This script reads the two columns from the source csv data file [budget_data.csv](https://github.com/zmoloci/python-challenge/blob/main/PyBank/Resources/budget_data.csv) and creates the following financial analysis:
  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $22564198
  Average Change: $262374.40
  Greatest Increase in Profits: Mar-13 ($1141840)
  Greatest Decrease in Profits: Dec-10 ($-1194133)
  ```
This script not only prints this analysis to the terminal, but it also generates a text file in the same format into the folder "./Analysis/Output.txt".

If the "./Analysis" folder does not exist, it will be created.

If the "./Analysis/Output.txt" file does not exist, it will be created.

If the "./Analysis/Output.txt" file does exist, it will be replaced.




### PyPoll - Analyzing Election Data

This script reads the two columns from the source csv data file [election_data.csv](https://github.com/zmoloci/python-challenge/blob/main/PyPoll/Resources/election_data.csv) and creates the following election analysis, which includes the total number of votes cast, a list of candidates including their percentage share of the vote, the actual number of votes they received and a final line indicating the winning candidate's name:
  ```text
  Election Results
  ----------------------------
  Total Votes: 369711
  ----------------------------
  Charles Casper Stockham: 5.335% (19723)
  Diana DeGette: 4.859% (17963)
  Raymon Anthony Doane: 89.807% (332025)
  ----------------------------
  Winner: Raymon Anthony Doane
  ----------------------------
  ```
The script features unique functionality that will adjust to show the above data for any number of unique candidates in similarly formated election data.

This script not only prints this analysis to the terminal, but it also generates a text file in the same format into the folder "./Analysis/Output.txt".

If the "./Analysis" folder does not exist, it will be created.

If the "./Analysis/Output.txt" file does not exist, it will be created.

If the "./Analysis/Output.txt" file does exist, it will be replaced.


## Repo File Contents
- [Readme.md](https://github.com/zmoloci/python-challenge/blob/main/Readme.md)
  - This file.
- [PyBank/main.py](https://github.com/zmoloci/python-challenge/blob/main/PyBank/main.py)
  - Script that provides financial analysis for monthly profit/loss data   
- [Pybank/Analysis/Output.txt](https://github.com/zmoloci/python-challenge/blob/main/PyBank/Analysis/Output.txt)
  - Output as per above (Lines 18-24).
- [PyBank/Resources/budget_data.csv](https://github.com/zmoloci/python-challenge/blob/main/PyBank/Resources/budget_data.csv)
  - Monthly profit/loss records for a company. Organized into two columns: "Date" (mmm-yy), "Profit/Losses" (int)
- [PyPoll/main.py](https://github.com/zmoloci/python-challenge/blob/main/PyPoll/main.py)
  - Script that provides election analysis for vote count data 
- [PyPoll/Analysis/Output.txt](https://github.com/zmoloci/python-challenge/blob/main/PyPoll/Analysis/Output.txt)
  - Output as per above (Lines 41-50).
- [PyPoll/Resources/election_data.csv](https://github.com/zmoloci/python-challenge/blob/main/PyPoll/Resources/election_data.csv)
  - Election data for a number of counties organized into three columns: "Voter ID", "County", and "Candidate"
