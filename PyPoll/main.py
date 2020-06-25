# Dependencies
import os
import csv

# Specify the file to read from
election_data = os.path.join("Resources", "election_data.csv")

# Open the file using "read" mode. Specify the variable to hold the contents
with open(election_data) as csvfile:

    # Initialize csv.
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # skip the header of the file 
    csv_header = next(csvreader)
    
    # Initialize valuable.
    # total vote is the number of vote
    total_Vote = 0
    # The number of vote for four condidate
    KhanCount = 0
    CorreyCount = 0
    OTooleyCount = 0
    LiCount = 0
    # the valuable for the Winner Name 
    winnerName = ""
    # the number list for each condidate
    Pypoll_dict = {"Khan":0, "Correy":0, "Li":0, "O'Tooley":0  }
    
    #read each line from the file
    for row in csvreader:
            # get the number of total vote
            total_Vote = total_Vote + 1 
            # add the vote 
            Pypoll_dict[row[2]] += 1
#close file 
csvfile.close()
# The number of voter 
output_String = "```text\nElection Results\n-------------------------\nTotal Votes: {0}\n".format(total_Vote)
# format prepare 
output_String = output_String + "-------------------------\n"
# calculate the percentage
for key,value in Pypoll_dict.items():
    percentValue = Pypoll_dict[key]/total_Vote
    output_String = output_String + key + ": {:.3%}({b})\n".format( percentValue ,b = Pypoll_dict[key])
# format prepare 
output_String = output_String + "-------------------------\n"
# find the winner 
output_String = output_String + "Winner: {0}\n".format(max(Pypoll_dict, key=Pypoll_dict.get) )
# format prepare 
output_String = output_String + "-------------------------\n"
# result output
print(output_String)


# Specify the file to write to 
output = open("election_output.txt", "w")
#write to file 
output.write(output_String)
#close file 
output.close()