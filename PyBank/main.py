import csv
months = ('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec')
total_months = 0
sum = 0
profitLossList = []
Dates = []
textFile = open("analysis/analysis.txt", "w")

with open("resources/budget_data.csv","r") as csv_file:
    mycsv_reader = csv.reader(csv_file,delimiter=",")
    header = next(mycsv_reader)

    # To find the total no. of months
    for row in mycsv_reader:
# to open the file once and refernce it at different lines in the code
        tmpRow = row
        list = tmpRow[0].split('-')
        if list[0] in months:
            total_months += 1
     # To find the total profit/loss
        sum += int(tmpRow[1])
        profitLossList.append(tmpRow[1])
        Dates.append(tmpRow[0])
    
    textFile.write("Financial Analysis\n")
    textFile.write("-------------------------\n")
    textFile.write("\n")
    textFile.write("\n")
    textFile.write(f"Total months : {total_months}\n")
    textFile.write("\n")
    textFile.write (f"Total:  $ {sum}\n")
    textFile.write("\n")
    total_change = 0
    greatest_increase = 0
    greatest_decrease = 0
    indx = 0
    # To find the average of changes
    for i in  range(0,len(profitLossList)-1):
        change = int(profitLossList[i+1]) - int(profitLossList[i])
        total_change += change
        if change > greatest_increase:
            indx = i+1
            greatest_increase = change 
        elif change < greatest_decrease:
            indx = i+1
            greatest_decrease = change

    average_change = total_change/(total_months-1)
    textFile.write(f'Average change: $ { average_change:.2f}\n')        
    textFile.write("\n")
    textFile.write(f'Greatest change in profit:  {Dates[indx]} $ {greatest_increase}\n')
    textFile.write("\n")
    textFile.write(f'Greatest decrease in profits: {Dates[indx]} $ {greatest_decrease}\n')

    

    textFile.close