import csv
import os

# Path to the election data (update this with the correct file path)
file_to_load = os.path.join("Resources", "election_data.csv")

# Variables to track the total votes and candidate votes
total_votes = 0
candidate_votes = {}

# Open and read the CSV file
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)
    
    # Read the header
    header = next(reader)
    
    # Process each row in the CSV file
    for row in reader:
        # Increment the total vote count
        total_votes += 1
        
        # Extract the candidate name from the row
        candidate = row[2]
        
        # If the candidate has received a vote before, increment their count
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            # If the candidate is not in the list, add them with 1 vote
            candidate_votes[candidate] = 1

# Calculate percentage of votes each candidate won and determine the winner
winner = None
max_votes = 0

# Prepare output
output = (
    "Election Results\n"
    "-------------------------\n"
    f"Total Votes: {total_votes}\n"
    "-------------------------\n"
)

# Loop through the candidates to calculate the percentage of votes and find the winner
for candidate, votes in candidate_votes.items():
    vote_percentage = (votes / total_votes) * 100
    output += f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
    
    # Determine the winner based on popular vote
    if votes > max_votes:
        max_votes = votes
        winner = candidate

# Add the winner to the output
output += (
    "-------------------------\n"
    f"Winner: {winner}\n"
    "-------------------------\n"
)

# Print the results
print(output)

# Optional: write the results to a text file
file_to_output = os.path.join("analysis", "election_results.txt")
with open(file_to_output, "w") as txt_file:
    txt_file.write(output)
