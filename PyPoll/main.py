import csv

candidate_votes = {}
total_votes = 0
max_votes = 0
# to create a new text file 
textFile = open("analysis/analysis.txt","w")
# to open a file to read the given data
with open ("resources/election_data.csv","r") as csvFile:
    csv_reader = csv.reader(csvFile, delimiter = ",")
    header = next(csv_reader)
# to find the different candidates in the given data
    for row in csv_reader:
        candidate = row[2]
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

textFile.write("Election Result\n")
textFile.write("---------------------------------------------\n")
# to find the total votes cast 

for key in candidate_votes:
    total_votes = total_votes + candidate_votes[key]
    
textFile.write(f"Total votes =  {total_votes}\n")
# to find the percentage of votes for different candidates and decide the winner

for key in candidate_votes:
    percentage = (candidate_votes[key]/total_votes * 100)
    if percentage > max_votes:
        max_votes = percentage
        winning_candidate = key

 
    textFile.write(f"{key} :  {percentage:.2f} % ({candidate_votes[key]})\n")
textFile.write("----------------------------------------------\n")
textFile.write(f"Winner: {winning_candidate}")
