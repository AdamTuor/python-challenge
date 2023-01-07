import csv

totalMonths = 0
totalPL = 0
changePL = 0
previousPL = 0
averagePL = 0
difference = 0

#these need to be date and amount
greatestProfit = 0
greatestLoss = 0

fileName= 'C:/Users/ASROCK Z590M Phantom/Desktop/BootCamp/Challenges/python-challenge/PyBank/Resources/budget_data.csv'

with open(fileName) as csvfile:
    reader = csv.reader(csvfile)

    next(reader)

    for row in reader:

        totalMonths = totalMonths +1

        totalPL= totalPL + int(row[1])
        
        if totalMonths <= 1:
            previousPL = int(row[1])
        else:
            difference = (int(row[1]) - previousPL)
            changePL =  changePL+ difference
            previousPL = int(row[1])
        #Need to get the date somehow
        if difference > greatestProfit:
            greatestProfit = difference
        if difference < greatestLoss:
            greatestLoss = difference

        #changePL= changePL + (int(row+1[1]) - int(row[1]))

    #how do I get the first month in
    #start on b3-b2=>++
    #add up all values and divide by 85.  first month x change so not 86
    
    #print(f"test {changePL}")
    print(f"Total Months: {totalMonths}")
    print(f"Total: ${totalPL}")
    print(f"Average Change: ${changePL/(totalMonths-1)}")
    print(f"Greatest Increase in Profits: ${greatestProfit}")  
    print(f"Greatest Decrease in Profits: ${greatestLoss}")   
   
        