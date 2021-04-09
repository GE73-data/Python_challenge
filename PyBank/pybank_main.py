#Part 1 import modules / dependencies
import csv
import os

csv_file_path = os.path.join(".", "Resources", "budget_data.csv")

file_to_output = os.path.join("Analysis", "Budgetanalysis.txt")

total_months = 0 
total_profit_losses = 0
value = 0
average_change = 0
count = 0
greatest_increase = ["", 0]  #positive change
greatest_decrease = ["", 0]  #negative change
dates = []
profits = []
monthly_change = 0


#opening csv_file
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    #Read the header
    csv_header = next(csv_reader)

    #read first row
    column_names = next(csv_reader)
    total_months += 1
    total_profit_losses += int(column_names[1])
    value = int(column_names[1])

    #go thru each row
    for row in csv_reader:
        count = count + 1

        #keep track of dates
        dates.append(row[0])


        #change & then add to the list of changes
        average_change = int(row[1])-value
        profits.append(average_change)
        value = int(row[1])

        
        #number of months
        total_months += 1

        #total profit losses
        total_profit_losses = total_profit_losses + int(row[1])

    #Increase in profits
        greatest_increase = max (profits)
        greatest_index = profits.index(greatest_increase)
        greatest_date = dates[greatest_index]

    #Decrease in profits
        greatest_decrease = min (profits)
        decrease_index = profits.index(greatest_decrease)
        decrease_date = dates[decrease_index]

    #Average change in profit losses
        average_change = sum(profits)/len(profits)
       
#......................................................................

#Create summary table
print("........................................")
print("Financial Analysis")   
print("...........................................")
print(f"Total Months: {str(total_months)}")
print(f"Total profit losses: ${str(total_profit_losses)}")
print(f"Average Change: ${str(round(average_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {decrease_date} (${str(greatest_decrease)})")


with open (file_to_output, "w") as text:

    text.write(f"Financial Analysis \n")
    text.write(f"........................................... \n")
    text.write(f"Total Months: {str(total_months)} \n")
    text.write(f"Total profit losses: ${str(total_profit_losses)} \n")
    text.write(f"Average Change: ${str(round(average_change,2))} \n")
    text.write(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)}) \n")
    text.write(f"Greatest Decrease in Profits: {decrease_date} (${str(greatest_decrease)}) \n")
