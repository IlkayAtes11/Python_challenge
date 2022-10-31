import os, csv

total_votes = 0

candidates = []

c_1 = 0
c_2 = 0
c_3 = 0

csvpath = r"C:\Users\AdminLocal\Desktop\Bootcamp\Python_challenge\PyPoll\Resources\election_data.csv"

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csvheader = next(csvreader)

    for row in csvreader:

        total_votes = total_votes + 1


        if row[2] not in candidates:
            candidates.append(row[2])


        if row[2] == candidates[0]:
            c_1 = c_1 + 1
        elif row[2] == candidates[1]:
            c_2 = c_2 + 1
        elif row[2] == candidates[2]:
            c_3 = c_3 +1


percentage_1 = "%.3f%%" % ((c_1/total_votes)*100)
percentage_2 = "%.3f%%" % ((c_2/total_votes)*100)
percentage_3 = "%.3f%%" % ((c_3/total_votes)*100)

votes = [c_1, c_2, c_3]

winner = max(votes)

winner_index = votes.index(winner)

# create variable of output

output =(
f'Election Results\n'
f'-------------------------\n'
f'Total Votes: {total_votes}\n'
f'-------------------------\n'
f'{candidates[0]}:    {percentage_1}    ({c_1}) \n'
f'{candidates[1]}:    {percentage_2}    ({c_2}) \n'
f'{candidates[2]}:    {percentage_3}    ({c_3}) \n'
f'-------------------------\n'
f'Winner: {candidates[winner_index]}\n'
f'-------------------------\n'
)

print(output)

outputpath = r"C:\Users\AdminLocal\Desktop\Bootcamp\Python_challenge\PyPoll\analysis\poll_analysis.txt"

with open(outputpath, "w") as outputfile:
    outputfile.write(output)

# A complete list of candidates who received votes

# The percentage of votes each candidate won

# The total number of votes each candidate won

# The winner of the election based on popular vote.