# initialize modules
import os
import csv
import operator

# prompt user for budget data filename
poll_data = input("Welcome to your Election Results Tool.\nPlease type your filename without the extension (must be a .csv)")+".csv"

# set path to file
csvpath = os.path.join("..", "Resources", poll_data)

# use csv reader to read budget data
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
   
    # next skips the header
    next(csvreader)
   
    # define lists
    candidate=[]

    # define row and describe columns
    for row in csvreader:
    
        candidate.append(str(row[2]))
        
    #determine candidate names?
    #calculate total number of votes
    total_votes= len(candidate)

    #count number of votes for Khan, Correy, Li, O'Tooley by adding up all the votes corresponding to their names
    #used the map function and lambda function to find the values in the Candidate column
    Khan_count=sum(map(lambda x :x=="Khan",candidate))
    Correy_count=sum(map(lambda x:x=="Correy",candidate))
    Li_count=sum(map(lambda x:x=="Li",candidate))
    OTooley_count=sum(map(lambda x:x=="O'Tooley",candidate))

    #calculate percentage of vote received
    percent_Khan=round((Khan_count/total_votes)*100)
    percent_Correy=round((Correy_count/total_votes)*100)
    percent_Li=round((Li_count/total_votes)*100)
    percent_OTooley=round((OTooley_count/total_votes)*100)
    
    #create a list of candidate counts to search for maximum
    candidate_count_dict={"Khan":Khan_count,"Correy": Correy_count,"Li": Li_count, "O'Tooley": OTooley_count}
    winner_count=max(candidate_count_dict.values())
    
    #get the key from candidate count containing the `maximum`
    winner_name = list(candidate_count_dict.keys())[list(candidate_count_dict.values()).index(winner_count)]

    #print things to the terminal
    print("-------------------------------\n")
    print("-------Election Results--------\n")
    print("-------------------------------")
    print(f"Total Votes:{total_votes}\n")
    print("-------------------------------")
    print(f"Khan:{percent_Khan}% ({Khan_count})\n")
    print(f"Correy:{percent_Correy}% ({Correy_count})\n")
    print(f"Li:{percent_Li}% ({Li_count})\n")
    print(f"O'Tooley:{percent_OTooley}% ({OTooley_count})\n")
    print("-------------------------------\n")
    print(f"The winner is {winner_name}!\n")
    print("-------------------------------\n")
    
# write things to a .txt file in the Analysis folder
# define output path
output_file=os.path.join("Analysis","election_results.txt") 

# write to output file
try:
    with open(output_file,"x",newline='') as datafile:
        datafile.write("-------------------------------\n")
        datafile.write("-------Election Results--------\n")
        datafile.write(f"Total Votes:{total_votes}\n")
        datafile.write("-------------------------------")
        datafile.write(f"Khan:{percent_Khan}% ({Khan_count})\n")
        datafile.write(f"Correy:{percent_Correy}% ({Correy_count})\n")
        datafile.write(f"Li:{percent_Li}% ({Li_count})\n")
        datafile.write(f"O'Tooley:{percent_OTooley}% ({OTooley_count})\n")
        datafile.write("-------------------------------\n")
        datafile.write(f"The winner is {winner_name}!\n")
        datafile.write("-------------------------------\n")

# message below lets user know that they already have an analysis.txt file
except:
    print("Uh oh! You already have an election_results file!\n Please delete it and run again to get a new one.")

