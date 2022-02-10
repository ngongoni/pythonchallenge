#Imported dependencies
import os
import csv

#Established variables
profit_losses = []

csvpath = os.path.join('budget_data.csv')

month_total = 0
net_total = 0
profit_change = 0
prev_profit = 0
max_profit = 0
min_profit = 0
max_day = " "
min_day = " "

#Calculate Total Months, Total Profit/Losses, Average of the changes, and greatest increase/decrease in profits
with open(csvpath) as budget_file:
    csv_reader = csv.reader(budget_file, delimiter = ',')
    
    csv_header = next(budget_file)

    for row in csv_reader:
        month_total = (month_total + 1)
        net_total = (net_total + int(row[1]))
        if prev_profit != 0:
            profit_change = int(row[1]) - prev_profit
            profit_losses.append(profit_change)
            prev_profit = int(row[1])
            if profit_change > max_profit:
                max_profit = profit_change
                max_day = str(row[0])
            elif profit_change < min_profit:
                min_profit = profit_change
                min_day = str(row[0])
        else: 
            prev_profit = int(row[1])

    average_change = round((sum(profit_losses) / len(profit_losses)), 2)

#Printed Finacial Analysis results
print(
    f"Financial Analysis\n"
    f"------------------------------------------\n"
    f"Total Months: {month_total}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change}\n"
    f"Greatest Increase in Profits: {max_day} (${max_profit})\n"
    f"Greatest Decrease in Profits: {min_day} (${min_profit})\n"
)

#Exported txt file
output_file = os.path.join('budget_data_results.txt')

final_file = open(output_file, "w+")
final_file.writelines(
    f"Financial Analysis\n"
    f"------------------------------------------\n"
    f"Total Months: {month_total}\n"
    f"Total: ${net_total}\n"
    f"Average Change: ${average_change}\n"
    f"Greatest Increase in Profits: {max_day} (${max_profit})\n"
    f"Greatest Decrease in Profits: {min_day} (${min_profit})\n"
    )
final_file.close()