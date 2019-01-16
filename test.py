#Read vegetables.csv 
import csv

with open('veggies.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

for row in rows:
    item = dict(row) # Convert Ordered Dict to regular dict (python 3.6 or higher)
    print(item)

# filter whitelist colors

#green_vegetables = []
#vegetables = ['green']
#for row in rows:
    #if row['color'] in vegetables:
        #green_vegetables.append(row)


#Print to the terminal
#print(green_vegetables)
