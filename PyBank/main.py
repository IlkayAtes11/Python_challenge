
import os, csv

# The total number of months included in the dataset

total_months=0

# The net total amount of "Profit/Losses" over the entire period

total_profit=0

# The changes in "Profit/Losses" over the entire period, and then the average of those changes

initial_profit=0

total_change_in_profit=0

current_profit=0

changes=[]
dates=[]

# The greatest increase in profits (date and amount) over the entire period

g_increase = 0

# The greatest decrease in profits (date and amount) over the entire period

g_decrease=0

# the path to data

csvpath = r"C:\Users\AdminLocal\Desktop\Bootcamp\Python_challenge\PyBank\Resources\budget_data.csv"

# opening and reading the csv file with python

with open(csvpath) as csvfile:
    csvreader= csv.reader(csvfile, delimiter=',')

# reading the header
    csv_header=next(csvreader)

# reading first row out of the loop to get the correct change of profits results over the months
    first_row=next(csvreader)

    total_months=total_months+1
    total_profit=total_profit+int(first_row[1])

    initial_profit=int(first_row[1])

    for row in csvreader:
       
        total_months=total_months+1
        dates.append(row[0])
    
  
        total_profit=total_profit+int(row[1])
        
        current_profit=row[1]
       
        change_in_profit=int(current_profit)-int(initial_profit)

        changes.append(change_in_profit)

        total_change_in_profit=sum(changes)

        initial_profit=row[1]

average_change=round(int(total_change_in_profit)/(int(total_months)-1),2)

g_increase=max(changes)
g_increase_index=changes.index(g_increase)
g_increase_month=dates[g_increase_index]
g_decrease=min(changes)
g_decrease_index=changes.index(g_decrease)
g_decrease_month=dates[g_decrease_index]

# create variable of output
output=(
f'Finacial Analysis\n'
f'----------------------------------\n'
f'Total Months: {total_months}\n'
f'Total: ${total_profit}\n'
f'Average Change: ${average_change}\n'
f'Greatest Increase in Profits: {g_increase_month}, (${g_increase})\n'
f'Greatest Decrease in Profits: {g_decrease_month}, (${g_decrease})\n'
)

print(output)

# create output and save to analysis folder

    # create path to analysis folder
outputpath="./analysis/budget_analysis.txt"

with open(outputpath, "w") as textfile:
    textfile.write(output)
