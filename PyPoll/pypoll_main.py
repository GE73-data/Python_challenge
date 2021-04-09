#Import modules
import csv
import os

csv_file_path = os.path.join(".", "Resources", "election_data.csv")

file_to_output = os.path.join("Analysis", "Electionanalysis.txt")

#Variables
total_votes = 0 
count = 0
percentage_votes = []
candidates_votes = {}
votes = []

#opening csv_file
with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ",")

    #Read the header
    csv_header = next(csv_reader)

     #go thru each row
    for row in csv_reader: 
        candidate_name = row[2]
        total_votes += 1

        #Votes by Person
        if candidate_name in candidates_votes.keys():
            candidates_votes[candidate_name] += 1
                    
        else:
            candidates_votes[candidate_name] = 1
            

   #......................................................................
output_list = []
#Create summary table
output_list.append("Election Results \n")
output_list.append("........................................ \n")
output_list.append(f"Total votes: {str(total_votes)} \n")
output_list.append("....................................... \n")
for candidate in candidates_votes:
    candidate_percentage = round(candidates_votes[candidate]/total_votes * 100, 2)
    output_list.append(f"{candidate}: {candidate_percentage}% ({candidates_votes[candidate]}) \n") 
output_list.append("..................................... \n")
output_list.append(f"Winner: Khan")
#to text file
with open(file_to_output, "w") as text:
    for item in output_list:
        print(item) 
        text.write(item)
