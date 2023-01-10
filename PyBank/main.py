import csv
import os

totalMonths = 0
totalPL = 0
changePL = 0
previousPL = 0
averagePL = 0
difference = 0
increaseList = ["",0]
decreaseList = ["",0]
greatestProfit = 0
greatestLoss = 0

fileName = os.path.join('Resources', 'budget_data.csv')
exportName = os.path.join('Analysis', 'results.txt')

with open(fileName) as csvfile:
    reader = csv.reader(csvfile)

    next(reader)

    for row in reader:
        #counter for months
        totalMonths = totalMonths +1

        #add what's in row[1] to the total each iteration
        totalPL= totalPL + int(row[1])
        
        #if it's the 1st iteration set the value of the first profit/loss
        if totalMonths <= 1:
            previousPL = int(row[1])
        #if it's not the 1st iteration, calculate the difference in profit/loss and add it to the changePL variable
        #changePL will be used to calculate the average change
        #difference will be used to help determine the greatest increase and decrease
        else:
            difference = (int(row[1]) - previousPL)
            changePL =  changePL+ difference
            previousPL = int(row[1])
        #conditions to find greatest profit/loss
        #stores the date from row[0] and puts the new difference in [1]
        if difference > greatestProfit:
            greatestProfit = difference
            increaseList[0] = row[0]
            increaseList[1] = greatestProfit
        if difference < greatestLoss:
            greatestLoss = difference
            decreaseList[0] = row[0]
            decreaseList[1] = greatestLoss
        
    #calculate/print the required values
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {totalMonths}")
    print(f"Total: ${totalPL}")
    print(f"Average Change: ${round(changePL/(totalMonths-1),2)}")
    print(f"Greatest Increase in Profits: {increaseList[0]} (${increaseList[1]})")  
    print(f"Greatest Decrease in Profits: {decreaseList[0]} (${decreaseList[1]})")   
   
with open(exportName, "w") as f:
    f.write("Financial Analysis\n")
    f.write("----------------------------\n")
    f.write(f"Total Months: {totalMonths}\n")
    f.write(f"Total: ${totalPL}\n")
    f.write(f"Average Change: ${round(changePL/(totalMonths-1),2)}\n")
    f.write(f"Greatest Increase in Profits: {increaseList[0]} (${increaseList[1]})\n")  
    f.write(f"Greatest Decrease in Profits: {decreaseList[0]} (${decreaseList[1]})\n")   
