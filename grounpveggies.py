#Jose and Karishma

import csv
import json
from pprint import pprint

#Read vegetables.csv
with open('veggies.csv', 'r') as f:
    reader = csv.DictReader(f)
    vegetables = list(reader)

for row in vegetables:
    item = dict(row) # Convert Ordered Dict to regular dict (python 3.6 or higher)
    print(item)




#Group by color
vegetable_by_color = {}
for vegetable in vegetables:
    color = vegetable['color']
    if color in vegetable_by_color:
        vegetable_by_color [color].append(vegetable)
    else:
        vegetable_by_color[color] = [vegetable]

#PRint to terminal
pprint(vegetable_by_color)

#Output Json 

with open('veggies.json', 'w') as f:
    json.dump(vegetable_by_color, f, indent=2)

