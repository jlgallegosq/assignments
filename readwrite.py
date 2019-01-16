import csv

vegetables = [
 {"name": "eggplant", "color": "purple"},
 {"name": "tomato", "color": "red"},
 {"name": "corn", "color": "yellow"},
 {"name": "okra", "color": "green"},
 {"name": "arugula", "color": "green"},
 {"name": "broccoli", "color": "green"},
]

# open a CsV file

with open('veggies.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['name', 'color'])
    #Loop through the veggies
    for vegetables in vegetables:
    	#Write each veggie to a CSV
		name = vegetables["name"]
		color = vegetables ["color"]
		row = [name, color]
		wirter.writerow(row)