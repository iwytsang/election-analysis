#The data we need to retrieve
#1. The total number of votes cas
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote

# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#1. Initalize a total vote counter
total_votes = 0

#Declare a new list for Candidate Options and candidate votes
candidate_options = []

#Declare empty dictionary
candidate_votes = {}

#Winning Candidate and Winning Count track
winning_candidate = ""
winning_count = 0
winning_percentage = 0


# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        #2. Add to total vote count.
        total_votes +=1

        #Print the candidate name from each row
        candidate_name = row[2]

        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

            #Add it to the list of candidates
            candidate_options.append(candidate_name)

            #Begin tracking cadidate's vote count
            candidate_votes[candidate_name] = 0 

        #Add a vote to candidates count
        candidate_votes[candidate_name] += 1 

#Determine percentage of votes by looping through counts

#Iterate through candidate list
for candidate_name in candidate_votes:
    #2. retreive vote count of candidate
    votes = candidate_votes[candidate_name]
    #3 calculatoe
    vote_percentage = float(votes) / float(total_votes) * 100
    #4. print candidate name and % of votes
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #if true then set winning_count = votes and winning_ percent = vote percnetage

        winning_count = votes
        winning_percentage = vote_percentage

        #set winning candidate equal to candidates name
        winning_candidate = candidate_name

winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)
 
