import csv 

thursday_file_input = input("Enter the full path to the file for Thursday's report: ")
saturday_file_input = input("Enter the full path to the file for Saturday's report: ")

thursday_file = open(thursday_file_input) 
saturday_file = open(saturday_file_input)

thursday_reader = csv.reader(thursday_file)
saturday_reader = csv.reader(saturday_file)

winners = [] 
thursday_numbers = [] 
saturday_numbers = [] 

thursday_fnames = [] 
saturday_fnames = [] 

thursday_lnames = [] 
saturday_lnames = [] 

header = next(saturday_reader)
header = next(thursday_reader)
for row in thursday_reader: 
    thursday_fnames.append(row[2]) 
    thursday_lnames.append(row[3])
    thursday_numbers.append(row[10])

for row in saturday_reader: 
    saturday_fnames.append(row[2])
    saturday_lnames.append(row[3])
    saturday_numbers.append(row[10])

for i in range(len(saturday_fnames)): 
    if i < len(thursday_fnames):  
        if float(saturday_numbers[i]) - float(thursday_numbers[i]) >= 48.00: 
            if thursday_fnames[i] == saturday_fnames[i] and thursday_lnames[i] == saturday_lnames[i]: 
                name = thursday_fnames[i] + " " + thursday_lnames[i] 
                winners.append(name)
    else:  
        if float(saturday_numbers[i]) >= 48.00: 
            name = saturday_fnames[i] + " " + saturday_lnames[i]
            winners.append(name)

for name in winners: 
    print(name)
