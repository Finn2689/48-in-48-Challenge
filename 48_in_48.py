import csv 

thursday_file = open('C:/Users/emily/Downloads/Thursday_Report.csv')
saturday_file = open('C:/Users/emily/Downloads/SatReport.csv')

thursday_reader = csv.reader(thursday_file)
saturday_reader = csv.reader(saturday_file)

winners = [] 
thursday_numbers = [] 
saturday_numbers = [] 

thursday_fnames = [] 
saturday_fnames = [] 

thursday_lnames = [] 
saturday_lnames = [] 

line = 0 
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
    if thursday_fnames[x] != saturday_fnames[x] or thursday_lnames[x] != saturday_lnames[x]: 
        print("you fucked up")
    x += 1 

y = 0 
for j in range(len(thursday_numbers)): 
    if float(saturday_numbers[y]) - float(thursday_numbers[y]) >= 48.00: 
        #print(str(float(friday_numbers[y]) - float(thursday_numbers[y])))
        if thursday_fnames[y] == saturday_fnames[y] and thursday_lnames[y] == saturday_lnames[y]: 
            name = thursday_fnames[y] + thursday_lnames[y] 
            winners.append(name)
    y += 1 

for name in winners: 
    print(name)
