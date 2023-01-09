import csv

totalVotes = 0
stockhamVotes = 0
degetteVotes = 0
doaneVotes = 0
percentOfVotes = 0


fileName="C:/Users/ASROCK Z590M Phantom/Desktop/BootCamp/Challenges/python-challenge/PyPoll/Resources/election_data.csv"
exportName = "C:/Users/ASROCK Z590M Phantom/Desktop/BootCamp/Challenges/python-challenge/PyPoll/Analysis/results.txt"

with open(fileName) as csvfile:
    reader = csv.reader(csvfile)
    next(reader)

    for row in reader:
        #count total votes
        totalVotes = totalVotes +1

        if row[2] == "Charles Casper Stockham":
            stockhamVotes = stockhamVotes +1
        elif row[2] == "Diana DeGette":
            degetteVotes = degetteVotes +1
        else:
            doaneVotes = doaneVotes +1


    if (stockhamVotes > degetteVotes) and (stockhamVotes > doaneVotes):
        winner = "Charles Casper Stockham"
    elif (degetteVotes > stockhamVotes) and (degetteVotes > doaneVotes):
        winner = "Diana DeGette"
    else:
        winner = "Raymon Anthony Doane"


    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {totalVotes}") 
    print("-------------------------")   
    print(f"Charles Casper Stockham: {round((stockhamVotes/totalVotes)*100,3)}% ({stockhamVotes})")
    print(f"Diana DeGette: {round((degetteVotes/totalVotes)*100,3)}% ({degetteVotes})")
    print(f"Raymon Anthony Doane: {round((doaneVotes/totalVotes)*100,3)}%({doaneVotes})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

with open(exportName, "w") as f:
    f.write("Election Results\n")
    f.write("----------------------------\n")
    f.write(f"Total Votes: {totalVotes}\n")
    f.write(f"Charles Casper Stockham: {round((stockhamVotes/totalVotes)*100,3)}% ({stockhamVotes})\n")
    f.write(f"Diana DeGette: {round((degetteVotes/totalVotes)*100,3)}% ({degetteVotes})\n")
    f.write(f"Raymon Anthony Doane: {round((doaneVotes/totalVotes)*100,3)}%({doaneVotes})\n")  
    f.write("-------------------------\n") 
    f.write(f"Winner: {winner}\n")
    f.write("-------------------------\n")