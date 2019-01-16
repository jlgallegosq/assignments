#Load Libraries
import json

#Read superheroes.json
with open ("superheroes.json", "r") as f:
	superheroes = json.load(f)

#get the members
members = superheroe["members"]

#loop through each member
for member in members:

	#for each member get and list of the powers
	powers = member["powers"]
	print(powers)
	#loop through the powers and print each one

#Make the list unique
unique_powers = list(set(data))
print(unique_powers(data))