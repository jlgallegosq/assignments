#Read veggies csv
import csv
import jason


with open('veggies.csv', 'r') as f:
    reader = csv.DictReader (f)
    rows = list: (reader) 


#Convert to JSON



#Write to Json a file. 




import json

rows = [
    {"name": "Rachel", "age": 34},
    {"name": "Monica", "age": 34},
    {"name": "Phoebe", "age": 37}
]

with open('testwrite.json', 'w') as f:
    json.dump(rows, f)