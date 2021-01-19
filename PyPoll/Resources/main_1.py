import os 
import csv

csvpath = os.path.join("..", "resources", "election_data.csv")
csvpath_txt = ("python-challenge/PyPoll/election_data.txt")

#Calling the variables I need
list_candidates = []
votes_candidates = []
votes = []

first_place = 0 
second_place = 0 
third_place = 0 
fourth_place = 0



with open (csvpath, "r") as cvsfile: 
    csvreader = csvreader(cvsfile, delimiter=",")
    
    csvreader = next(csvreader)

for row in csvreader: 
    votes.append(row["Candidate"])
    votes = row["Candidate"]

#Every new candidate that is not a top 4 candidate

    if row["Candidate"] not in list_candidates: 
        list_candidates.append(row["Candidate"])
        list_candidates [row["Candidate"]] = 1

    else 
    votes_candidates[row["Candidate"]] = votes_candidates[row["Candidate"]] + 1 
      

#Determine the winner candidate
    for row in votes: 
        if row["Candidate"] == list_candidates[0]:
            first_place = first_place + 1
        
        elif row["Candidate"] == list_candidates[1]:
            second_place = second_place + 1

        elif row["Candidate"] == list_candidates[2]:
            third_place = third_place + 1

        elif row["Candidate"] == list_candidates[3]:
            fourth_place = fourth_place + 1 

winner = str(first_place)

print (f'The Election results are: {len(votes)}')
print("------------------------------------")
print (votes_candidates)
print("------------------------------------")
print (f'Khan: {int(first_place)} + {str(((votes_candidates[first_place])/votes)*100)) + "%"}')
print (f'Correy: {int(second_place)} + {str(((votes_candidates[second_place])/votes)*100))) + "%"}')
print (f'Li: {int(third_place)} + {str(((votes_candidates[third_place])/votes)*100))) + "%"}')
print (f' O´Tolley:{int(fourth_place)} + {str(((votes_candidates[fourth_place])/votes)*100))) + "%"}')
print("------------------------------------")
print("" + first_place)

#I was not sure about the declaration of the variables in here. 

#2 Code 
#import os 
#import csv

#csvpath = os.path.join("..", "resources", "election_data.csv")
#csvpath_txt = ("python-challenge/PyPoll/election_data.txt")

#total_votes = 0 
#khan_votes = 0 
#correy_votes = 0 
#li_votes = 0 
#otooley_votes = 0 
#with open (csvpath, "r") as cvsfile: 
 #   csvreader = csvreader(cvsfile, delimiter=",")
    
  #  csvreader = next(csvreader)


#For row in csvreader: 
#total_votes = total_votes + 1

  #if row[2] == "Khan": 
      #khan_votes = khan_votes + 1
  #elif row[2] == "Correy": 
      #correy_votes = correy_votes + 1
  #elif row[2] == "Li": 
      #Li_votes = Li_votes + 1
  #elif row[2] == "O'Tooley"
      #otooley_votes= otooley_votes + 1 

# Dictonaries: in which keys are the names and the values are the number of votes was another option. 
#candidates = ["Khan", "Correy", "Li", "O'Tooley"]
#votes = [khan_votes, correy_votes, Li_votes, otooley_votes]

#Khan = ((khan_votes/total_votes) + "%")
#correy = ((correy_votes/total_votes) + "%")
#li = ((li_votes/total_votes) + "%")
#otooley = ((otooley_votes/total_votes) + "%")

#Print Results and so on.... 

#Which one is the correct one?

# Results in txt
with open (csvpath_txt, ".") as txt_file: 
    txt_file.write ("Election Results")
    txt_file.write ("---------------------")
    txt_file.write (f'The total votes are: {len(votes)}'))
    txt_file.write ("---------------------")
    txt_file.write (list_candidates + "" + int((votes_candidates[first_place])/votes)*100)) + "%")
    txt_file.write (list_candidates + "" + int((votes_candidates[second_place])/votes)*100)) + "%")
    txt_file.write (list_candidates + "" + int((votes_candidates[third_place])/votes)*100)) + "%")
    txt_file.write (list_candidates + "" + int((votes_candidates[fourth_place])/votes)*100)) + "%")
    txt_file.write ("---------------------")
    txt_file.write ("Winner: Khan")
