# initialize modules
import os
import csv

# prompt user for budget data filename
budget_data = input("Welcome to your Budget Analysis Tool.\nPlease type your filename without the extension (must be a .csv)")+".csv"

# set path to file
csvpath = os.path.join("..", "Resources", budget_data)

# use csv reader to read budget data
with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
   
    # next skips the header
    next(csvreader)
   
    # define lists
    profit_losses=[]
    month=[]
    profit_delta=[]

    # define row and describe columns
    for row in csvreader:
    
        month.append(str(row[0]))
        profit_losses.append(float(row[1]))

    #calculate total profit/loss by summing profit/loss column
    total_profit_loss = sum(profit_losses)

    #determine profit/loss deltas per month by subtracting value from prior month's value
    #define profit_delta as list of profit/losses values from one month subtracted from prior month's value
    #range defines iterations, from one to the number of rows with data (using len()); each difference is appended to the profit_delta list
    for i in range(1,len(profit_losses)):
        profit_delta.append(profit_losses[i]-profit_losses[i-1])

        # use profit_delta info to calculate max, min, and average delta
        max_profit=max(profit_delta)
        min_profit=min(profit_delta)
        avg_delta=sum(profit_delta)/len(profit_delta)

        # determine min and max delta corresponding month via index
        max_profit_month=str(month[profit_delta.index(max(profit_delta))])
        min_profit_month=str(month[profit_delta.index(min(profit_delta))])
    
    #calculate total month count 
    month_count=len(month)
    
            
# print things to the terminal
print("------------------")
print("Financial Analysis")
print("------------------")
print(f"Total Months Analyzed:{month_count}\n")
print(f"Total Profit/Loss:${total_profit_loss}\n")
print(f"Average Change:${avg_delta}\n")
print(f"Greatest Increase:${max_profit} in {max_profit_month}\n")
print(f"Greatest Decrease:${min_profit} in {min_profit_month}\n")

# write things to a .txt file in the Analysis folder
# define output path
output_file=os.path.join("Analysis","analysis.txt") 

#write to output file
try:
    with open(output_file,"x",newline='') as datafile:
        datafile.write("------------------\n")
        datafile.write("Financial Analysis\n")
        datafile.write("------------------\n")
        datafile.write(f"Total Months Analyzed:{month_count}\n")
        datafile.write(f"Total Profit/Loss:${total_profit_loss}\n")
        datafile.write(f"Average Change:${avg_delta}\n")
        datafile.write(f"Greatest Increase:${max_profit} in {max_profit_month}\n")
        datafile.write(f"Greatest Decrease:${min_profit} in {min_profit_month}\n")

# message below lets user know that they already have an analysis.txt file
except:
    print("Uh oh! You already have an analysis file!\n Please delete it and run again to get a new one.")

