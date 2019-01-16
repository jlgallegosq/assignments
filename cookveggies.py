#Read veggies.csv into a variable "vegetables"
import csv
import json

with open('veggies.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

for row in rows:
    print(row)

#Print the variable "vegetables"
print(vegetables)


#Save to JSON as vegetables.json