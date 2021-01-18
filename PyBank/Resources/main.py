import os 
import csv

csvpath = os.path.join("..", "resources", "budget_data.csv")
csvpath_txt = ("python-challenge/PyBank/election_data.txt")

dates=[]
profit_loses=[]

total_months = 0
net_amount = 0
changes = 0
average_change = 0 
greatest_increase = 0 
greatest_decrease = 0 


with open (csvpath, "r") as cvsfile: 
    csvreader = csvreader(cvsfile, delimiter=",")

    
    csvreader = next(csvreader)

for row in csvreader: 
    #total dates
    dates = row(0)
    total_months = len(dates + 1) 
    
     #net total amount
    profit_loses = row[1]
    net_amount = profit_loses + row[1]

#changes of net_amount 
for i in range(len(row[1])- 1):
    changes = net_amount[i + 1] - net_amount
    average_change = round(sum(changes) / len(changes), 2)

for changes in row [1]: 
#Amount
greatest_increase = max(changes)
greatest_decrease = min(changes)

#Dates 
    if changes == greatest_increase:
        greatest_increase.month = row[i, greatest_increase]
    elif changes == greatest_decrease: 
        greatest_decrease.month = row[i, greatest_decrease]


#Print 

print ("Financial Analysis")
print("----------------------")
print(f'Total Months: {total_months}')
print(f'Total: {net_amount}')
print(f'Average change: {average_change})

print(f'Greatest increase: {total_months [greatest_increse.month]} {(greatest_increase) + "$"}') 
print(f'Greatest increase: {total_months [greatest_decrease.month]} {(greatest_decrease) + "$"}')


# Results in txt
with open (csvpath_txt, ".") as txt_file: 
    txt_file.write ("Financial Analysis")
    txt_file.write ("---------------------")
    txt_file.write (f'Total Months: {total_months}')
    txt_file.write (f'Total: {net_amount}')
    txt_file.write (f'Average change: {average_change})

    txt_file.write(f'Greatest increase: {total_months [greatest_increse.month]} {(greatest_increase) + "$"}')   
    txt_file.write(f'Greatest increase: {total_months [greatest_decrease.month]} {(greatest_decrease) + "$"}')


