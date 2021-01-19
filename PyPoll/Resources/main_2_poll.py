#2 Code 
import os 
import csv

csvpath = os.path.join("..", "resources", "election_data.csv")
csvpath_txt = ("python-challenge/PyPoll/election_data.txt")

total_votes = 0 
khan_votes = 0 
correy_votes = 0 
li_votes = 0 
otooley_votes = 0 
with open (csvpath, "r") as cvsfile: 
    csvreader = csvreader(cvsfile, delimiter=",")
    
    csvreader = next(csvreader)

 #Dictonaries: in which keys are the names and the values are the number of votes was another option. 
candidates = ["Khan", "Correy", "Li", "O'Tooley"]
votes = [khan_votes, correy_votes, Li_votes, otooley_votes]

 for row in csvreader: 
       total_votes = total_votes + 1

               if row[2] == "Khan": 
                khan_votes = khan_votes + 1
               elif row[2] == "Correy": 
                correy_votes = correy_votes + 1
               elif row[2] == "Li": 
                Li_votes = Li_votes + 1
               elif row[2] == "O'Tooley"
                otooley_votes= otooley_votes + 1 

Khan_final_results = ((khan_votes/total_votes) * 100) + "%")
correy_final_results = ((correy_votes/total_votes) * 100) + "%")
li_final_results = ((li_votes/total_votes)* 100) + "%")
otooley_final_results = ((otooley_votes/total_votes)*100) + "%")

print ("Election Results")
print("--------------------")
print(f'Total Votes : + {total_votes}')
print("----------------------")
print(f'Khan : + {Khan_final_results} + {khan_votes}')
print(f'Correy : + {correy_final_results} + {correy_votes}')
print(f'Li : + {li_final_results} + {Li_votes}')
print(f'Otooley : + {otooley_final_results} + {otooley_votes}')

with open (csvpath_txt, ".") as txt_file: 
    txt_file.write ("Election Results")
    txt_file.write ("---------------------")
    txt_file.write (f'Total Votes : + {total_votes}')
    txt_file.write ("----------------------")
    txt_file.write (f'Khan : + {Khan_final_results} + {khan_votes}')
    txt_file.write (f'Correy : + {correy_final_results} + {correy_votes}')
    txt_file.write (f'Li : + {li_final_results} + {Li_votes}')
    txt_file.write (f'Otooley : + {otooley_final_results} + {otooley_votes}')
    txt_file.write ("---------------------")
    txt_file.write ("Winner: Khan")
