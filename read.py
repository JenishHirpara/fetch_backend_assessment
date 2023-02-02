import csv
import sys


# Keep this file and the transactions.csv in the same folder
# to run the file and to set spending limit as 5000 type python read.py 5000 in the terminal


# Reading the file
with open('transactions.csv', 'r') as fin:
    csv_reader = csv.reader(fin, delimiter=',')
    # ignoring the first line in the csv file which contains "payer","points","timestamp" header
    next(csv_reader)
    # sorting the rows by timestamp so that oldest points will be spent first
    sort_value = sorted(csv_reader, key=lambda x:x[2])

    # if the user did not enter the amount of points to enter then default value taken will be 5000
    if(len(sys.argv) == 1):
        x = 5000
    # x is the spending limit which the user will pass as argument while running python file
    else:
        x = int(sys.argv[1])
    dict = {}
    # iterating through each sorted row 
    for row in sort_value:
        # case where points are being spent
        if int(row[1]) >= 0:
            # if the spending limit is greater than or equal to the points being spent, then deduct the points from the spending limit
            if x >= int(row[1]):
                x -= int(row[1])
                if row[0] not in dict:
                    dict[row[0]] = 0
            # if the spending limit is less than the points being spent, then set spending limit to 0 and set the payer's points to the difference of points and spending limit
            else:
                p = int(row[1]) - x
                x = 0
                if row[0] not in dict:
                    dict[row[0]] = p
                else:
                    dict[row[0]] += p
        # case where points are being earned
        else:
            # if the value of payer in the dictionary is more than points being earned, then subtract that points from the payer, else add those points to the spending limit
            if row[0] not in dict:
                x += abs(int(row[1]))
                dict[row[0]] = 0
            else:
                if dict[row[0]] >= abs(int(row[1])):
                    dict[row[0]] -= abs(int(row[1]))
                else:
                    dict[row[0]] = 0
                    x += abs(int(row[1])) - dict[row[0]]
    print(dict)