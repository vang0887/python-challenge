import os
import csv

pypoll_csv = os.path.join('..', 'Resources', 'PyPollData.csv')


total_votes = 0
votes = []
candidates = []
percent_votes = []

with open(pypoll_csv, 'r') as csvfile:
   
    pypoll_csvreader = csv.reader(csvfile, delimiter=',')

    header = next(pypoll_csvreader)

    for row in pypoll_csvreader:
        
        total_votes = total_votes + 1

        if row[2] in candidates:
            find_candidates = candidates.index(row[2])
            votes.append(1)
            votes[find_candidates] += 1
        else:
            candidates.append(row[2])
            find_candidates = candidates.index(row[2])
            votes.append(1)

    for vote in votes:
        percentage_vote = (vote/total_votes) * 100
        percentage_vote = round(percentage_vote)
        percentage_vote = "%.3f%%" % percentage_vote
        percent_votes.append(percentage_vote)
     

    winner = max(votes)
    find_winner = votes.index(winner)
    candidates_winner = candidates[find_winner]

    #loser = min(votes)
    #find_loser = votes.index(loser)
    #candidates_loser = candidates(find_loser)


    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(total_votes))
    for i in range(len(candidates)):
        print(f"{candidates[i]}: {str(percent_votes[i])} ({str(votes[i])})")
    print("-------------------------")
    print("Winner: " + str(candidates_winner))
    print("-------------------------")



with open ("pypoll_results.txt", 'w') as text: 
    text.write("Election Results\n")
    text.write("-------------------------\n")
    text.write("Total Votes: " + str(total_votes) + "\n")
    for i in range(len(candidates)):
        text.write(f"{candidates[i]}: {str(percent_votes[i])} ({str(votes[i])})" + "\n")
    text.write("-------------------------\n")
    text.write("Winner: " + str(candidates_winner) + "\n")
    text.write("-------------------------\n")