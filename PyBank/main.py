import csv

totalMonths = 0
totalPL = 0
changePL = 0
averagePL = 0

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

    print(totalPL)
    #print(totalMonths)
        