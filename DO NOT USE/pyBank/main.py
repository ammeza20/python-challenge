import csv
import os

# Path to the budget data (update this with the correct file path)
file_to_load = os.path.join("Resources", "budget_data.csv")

# Initialize variables
total_months = 0
total_net = 0
previous_profit_loss = None
changes = []
dates = []
greatest_increase = {"date": "", "amount": 0}
greatest_decrease = {"date": "", "amount": 0}

# Open and read the CSV file
with open(file_to_load) as budget_data:
    reader = csv.reader(budget_data)
    
    # Read the header
    header = next(reader)
    
    # Loop through each row in the dataset
    for row in reader:
        date = row[0]
        profit_loss = int(row[1])
        
        # Increment total number of months
        total_months += 1
        
        # Add to the net total of profit/losses
        total_net += profit_loss
        
        # Calculate the change in profit/loss and store the date
        if previous_profit_loss is not None:
            change = profit_loss - previous_profit_loss
            changes.append(change)
            dates.append(date)
            
            # Check for greatest increase in profits
            if change > greatest_increase["amount"]:
                greatest_increase["amount"] = change
                greatest_increase["date"] = date
            
            # Check for greatest decrease in profits
            if change < greatest_decrease["amount"]:
                greatest_decrease["amount"] = change
                greatest_decrease["date"] = date
        
        # Update the previous profit/loss
        previous_profit_loss = profit_loss

# Calculate the average change
if changes:
    average_change = sum(changes) / len(changes)
else:
    average_change = 0

# Create the output summary
output = (
    "Financial Analysis\n"
    "----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Net Total Profit/Losses: ${total_net}\n"
    f"Average Change: ${average_change:.2f}\n"
    f"Greatest Increase in Profits: {greatest_increase['date']} (${greatest_increase['amount']})\n"
    f"Greatest Decrease in Profits: {greatest_decrease['date']} (${greatest_decrease['amount']})\n"
)

# Print the output
print(output)

# Optional: Write the output to a text file
file_to_output = os.path.join("analysis", "financial_analysis.txt")
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
