#TODO pseudo code befor I begin

# import modules / dependencies
import csv   #read csv file using .reader methong
import os   #os to join elements of the file path for PC

csv_file_path = os.path.join(",", "Resources", "budget_date.csv")

file_to_output = os.path.join("Analysis", "test.txt")
# print(csv_file_path)

#Initialize variables

#......................................................................
#Open and read the csv_file called budget_data.csv
# with open("Resources/budget_data.csv","r") as budgetDatacsv:
#     reader = csv.reader(budgetDatacsv)
    # column_names = next(reader)
    # total_months = 0

    #Part 2 make calculations
#     for row in reader:
#         print(row)
#         total_months = total_months + 1
#         print(total_months)
# #Part 3 save calculations to a txt file
# output=(
#     f'Total_Months = {total_months}'
#     )

# with open("Budgetanalysis.txt","w") as budgetDatatxt:
#     budgetDatatxt.write(output)