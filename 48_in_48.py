import csv 

thursday_file = open('C:/Users/emily/Downloads/Thursday_Report.csv')
friday_file = open('C:/Users/emily/Downloads/SatReport.csv')

thursday_reader = csv.reader(thursday_file)
friday_reader = csv.reader(friday_file)

winners = [] 
thursday_numbers = [] 
friday_numbers = [] 

thursday_fnames = [] 
friday_fnames = [] 

thursday_lnames = [] 
friday_lnames = [] 

line = 0 
header = next(friday_reader)
header = next(thursday_reader)
for row in thursday_reader: 
    thursday_fnames.append(row[2]) 
    thursday_lnames.append(row[3])
    thursday_numbers.append(row[10])

for row in friday_reader: 
    friday_fnames.append(row[2])
    friday_lnames.append(row[3])
    friday_numbers.append(row[10])

'''
abc = 0 
for abc in range(10): 
    print(thursday_fnames[abc])
    print(friday_fnames[abc])
    print(thursday_lnames[abc])
    print(friday_lnames[abc])
    print(thursday_numbers[abc])
    print(friday_numbers[abc])
    print(str(float(friday_numbers[abc]) - float(thursday_numbers[abc])))'
'''

x = 0
for i in range(len(thursday_fnames)): 
    if thursday_fnames[x] != friday_fnames[x] or thursday_lnames[x] != friday_lnames[x]: 
        print("you fucked up")
    x += 1 

y = 0 
for j in range(len(thursday_numbers)): 
    if float(friday_numbers[y]) - float(thursday_numbers[y]) >= 48.00: 
        #print(str(float(friday_numbers[y]) - float(thursday_numbers[y])))
        if thursday_fnames[y] == friday_fnames[y] and thursday_lnames[y] == friday_lnames[y]: 
            name = thursday_fnames[y] + thursday_lnames[y] 
            winners.append(name)
    y += 1 

for name in winners: 
    print(name)
