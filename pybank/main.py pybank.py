import os
import csv

pybank_csv = os.path.join('..', 'Resources', 'PyBank_Budget_Data.csv')


month = 0
total_profit = 0
first_profit = 0
previous_profit = 0

change_profit = []
dates = []
total_profit_count = []


with open(pybank_csv, 'r') as csvfile:

    pybank_csvreader = csv.reader(csvfile, delimiter=',')

    header = next(pybank_csvreader)

    for row in pybank_csvreader:

        month = month + 1 

        total_profit = total_profit + int(row[1])

        total_profit_count.append(int(row[1]))
        
        previous_profit = int(row[1])
        new_profit = previous_profit - first_profit
        change_profit.append(new_profit)
        first_profit = int(row[1])
    
        avg_change_profits = sum(change_profit)/(month)

        greatest_increase = max(change_profit)
        greatest_decrease = min(change_profit)

        dates.append(row[0])

        search_date01 = change_profit.index(greatest_increase)
        greatest_increase_date = dates[search_date01]

        search_date02 = change_profit.index(greatest_decrease)
        greatest_decrease_date = dates[search_date02]



    print("Financial Analysis")
    print("-------------------------")
    print ("Total Months " + str(month))
    print("Average Change " + "$"  + str(round(avg_change_profits, 2)))
    print("Greatest Increase in Profits: $" + str(greatest_increase))
    print("Greatest Decrease in Profit: $" + str(greatest_decrease))   
  
    
with open("pybank_results.txt", "w") as text:

    text.write("Financial Analysis")
    text.write("-------------------------")
    text.write("Total Months " + str(month))
    text.write("Average Change " + "$"  + str(round(avg_change_profits, 2)))
    text.write("Greatest Increase in Profits: $" + str(greatest_increase))
    text.write("Greatest Decrease in Profit: $" + str(greatest_decrease))   

