# Dependencies
import os
import csv
# Specify the file to read from
budget_data = os.path.join("Resources", "budget_data.csv")
# Open the file using "read" mode. Specify the variable to hold the contents
with open(budget_data) as csvfile:
    # Initialize csv.
    csvreader = csv.reader(csvfile, delimiter=',')
    # skip the header of the file 
    csv_header = next(csvreader)
     # Initialize valuable.
    total_number_months = 0
    greatest_decrease = 0
    greatest_increase = 0 
    increase_index = 0
    decrease_index = 0
    currentRowValue = 0
    lastRowValue = 0
    
    budget_data_list = []
    budget_diff_list = []
    budget_date_list = []   

    
    #read each line from the file
    for row in csvreader:
            currentDate = row[0] # get the date from list
            currentRowValue = int(row[1]) # get the value from list
            currentDiff = 0 
            if total_number_months!=0:
                currentDiff = currentRowValue-lastRowValue # get the diff from list
            budget_date_list.append(currentDate) # append to date list
            budget_data_list.append(currentRowValue)# append to data list
            budget_diff_list.append(currentDiff)# append to diff list
            lastRowValue = currentRowValue # save the current value
            total_number_months += 1
    #close file         
    csvfile.close()
    
    # get the number of month
    total_number_months = len(budget_date_list)
    
    # get average changes
    average_changes_ProfitLosses = round(sum(budget_diff_list)/(total_number_months-1),2)
    
    # get max value changes
    greatest_increase = max(budget_diff_list)
    # the index of max value
    increase_index = budget_diff_list.index(greatest_increase)
    # the max value 
    greatest_increase_date = budget_date_list[increase_index]
    
    # get the greatest decrease value changes
    greatest_decrease = min(budget_diff_list)
    # the index of max decrease value
    decrease_index = budget_diff_list.index(greatest_decrease)
    # the max decrease value 
    greatest_decrease_date = budget_date_list[decrease_index]
    
    output_String= "```text\nFinancial Analysis\n----------------------------\n"
    
    #format total number months
    output_String = output_String + "Total Months: {0}\n".format(total_number_months)
    #format sum value 
    output_String = output_String + "Total: ${0}\n".format(sum(budget_data_list))
    #format Average  Change
    output_String = output_String + "Average  Change: ${0}\n".format(round(average_changes_ProfitLosses,2))
    #Greatest Increase in Profits
    output_String = output_String + "Greatest Increase in Profits:{0} (${1})\n".format(greatest_increase_date, greatest_increase )
    #Greatest Decrease in Profits
    output_String = output_String + "Greatest Decrease in Profits:{0} (${1})\n".format(greatest_decrease_date, greatest_decrease )
    print(output_String)

    # Specify the file to write to
    output = open("PyBankoutput.txt", "w")
    # write to file 
    output.write(output_String)
    # close file 
    output.close()