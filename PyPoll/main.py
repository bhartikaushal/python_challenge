import csv

candidate_votes = {}
total_votes = 0
max_votes = 0

textFile = open("analysis/analysis.txt","w")
with open ("resources/election_data.csv","r") as csvFile:
    csv_reader = csv.reader(csvFile, delimiter = ",")
    header = next(csv_reader)

    for row in csv_reader:
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

textFile.write("Election Result\n")
textFile.write("---------------------------------------------\n")


for key in candidate_votes:
    total_votes = total_votes + candidate_votes[key]
    
textFile.write(f"Total votes =  {total_votes}\n")


for key in candidate_votes:
    percentage = (candidate_votes[key]/total_votes * 100)
    if percentage > max_votes:
        max_votes = percentage
        winning_candidate = key

 
    textFile.write(f"{key} :  {percentage:.2f} % ({candidate_votes[key]})\n")
textFile.write("----------------------------------------------\n")
textFile.write(f"Winner: {winning_candidate}")
