

# The net total amount of "Profit/Losses" over the entire period

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

# The greatest increase in profits (date and amount) over the entire period

# The greatest decrease in profits (date and amount) over the entire period

import os, csv

def print_budgetdata(budget_data):

    months=str(budget_data[0])
    profit_lost=int(budget_data[1])
    
# The total number of months included in the dataset
    total_months=len(months)

# The net total amount of "Profit/Losses" over the entire period
    net_profit_lost=0

    for data in budget_data:

        net_profit_lost=net_profit_lost+data

# print out the results

    print(months)
    print(net_profit_lost)


csvpath=r"C:\Users\AdminLocal\Desktop\Bootcamp\Python_challenge\PyBank\Resources\budget_data.csv"

with open(csvpath) as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader)
    for row in csvreader:
        print_budgetdata(row)