# Dependecies
import csv
import os

# Files to input and output
inputfile = os.path.join('Resources', 'budget_data.csv')
outputfile = os.path.join('Resources', 'financial_analysis.txt')
# Tracking variables
total_months = 0
total = 0
change_in_rev = 0
previous_rev = 0
greatest_increase = ["",0]
greatest_decrease = ["", 0]
revenue_changes = []

# Read Files
with open(inputfile) as csv_file:
     csvread = csv.reader(csv_file)
     reader = csv.DictReader(csv_file)
     #Calculate The Totals
     for row in reader:
        total_months = total_months + 1
        total = total + int(row["Profit/Losses"])
     # Adjust for no previous revenue to calculate average change_in_rev
        if(previous_rev ==0):
           previous_rev = int(row["Profit/Losses"])
    # Keep track of changes
        change_in_rev = int(row["Profit/Losses"]) - previous_rev
    # Reset the value of previous_rev to current row read
        previous_rev = int(row["Profit/Losses"])
        print(change_in_rev)

    # Calculate the greatest increase
        if (change_in_rev > greatest_increase[1]):
            greatest_increase[1] = change_in_rev
            greatest_increase[0] = row["Date"]

        if (change_in_rev < greatest_decrease[1]):
            greatest_decrease[1] = change_in_rev
            greatest_decrease[0] = row["Date"]
    # Add to the revenue_changes list
        revenue_changes.append(int(change_in_rev))

    # Set the revenue average
     revenue_avg = sum(revenue_changes) / len(revenue_changes)

    # Show Output
     print("Financial Analysis")
     print("-------------------------")
     print("Total Months: " + str(total_months))
     print("Total Revenue: " + "$" + str(total))
     # We take 1 month out of the length of the frame to avoid month 0 with no previous data when calculating average
     print("Average Change: " + "$" + str(round(sum(revenue_changes) / (len(revenue_changes)-1),2)))
     print("Greatest Increase: " + str(greatest_increase[0]) + " ($" +  str(greatest_increase[1]) + ")") 
     print("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" +  str(greatest_decrease[1]) + ")")


     # Write output to file

     # Output Files
with open(outputfile, "w") as txt_file:
    txt_file.write("Total Months: " + str(total_months))
    txt_file.write("\n")
    txt_file.write("Total Revenue: " + "$" + str(total))
    txt_file.write("\n")
    txt_file.write("Average Change: " + "$" +  str(round(sum(revenue_changes) / (len(revenue_changes)-1),2)))
    txt_file.write("\n")
    txt_file.write("Greatest Increase: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")") 
    txt_file.write("\n")
    txt_file.write("Greatest Decrease: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")
