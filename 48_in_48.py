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

x = 0
for i in range(len(saturday_fnames)): 
    if x < len(thursday_fnames) and (thursday_fnames[x] != saturday_fnames[i] or thursday_lnames[x] != saturday_lnames[i]):
        print(f"Mismatch or new entry found: {saturday_fnames[i]} {saturday_lnames[i]}")
    elif x >= len(thursday_fnames): 
        print(f"New entry found: {saturday_fnames[i]} {saturday_lnames[i]}")
        '''
        if float(saturday_numbers[x]) - float(thursday_numbers[x]) >= 48.00: 
            if thursday_fnames[x] == saturday_fnames[x] and thursday_lnames[x] == saturday_lnames[x]: 
                name = thursday_fnames[x] + thursday_lnames[x] 
                winners.append(name)'
        '''
    x += 1 

y = 0 
for j in range(len(saturday_numbers)): 
    if y < len(thursday_numbers) and float(saturday_numbers[j]) - float(thursday_numbers[y]) >= 48.00: 
        if thursday_fnames[y] == saturday_fnames[j] and thursday_lnames[y] == saturday_lnames[j]: 
            name = thursday_fnames[y] + " " + thursday_lnames[y] 
            winners.append(name)
    elif y >= len(thursday_numbers):  # Handle new entries in Saturday report
        if float(saturday_numbers[j]) >= 48.00: 
            name = saturday_fnames[j] + " " + saturday_lnames[j]
            winners.append(name)
    y += 1 

'''
y = 0 
for j in range(len(saturday_numbers)): 
    if float(saturday_numbers[y]) - float(thursday_numbers[y]) >= 48.00: 
        if thursday_fnames[y] == saturday_fnames[y] and thursday_lnames[y] == saturday_lnames[y]: 
            name = thursday_fnames[y] + thursday_lnames[y] 
            winners.append(name)
    y += 1 
'''

for name in winners: 
    print(name)
