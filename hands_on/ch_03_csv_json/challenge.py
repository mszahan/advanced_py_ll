import json
import csv

## this dictionary should contain all the laureat
# laureates = {}
with open('laureates.csv', 'r') as l_file:
    reader = csv.DictReader(l_file)
    laureates = list(reader)

laureates_with_a = []

for lareate in laureates:
    if lareate['name'][0] == 'A':
        laureates_with_a.append(lareate)

with open('laureat_with_a.json', 'w') as f:
    json.dump(laureates_with_a, f, indent=2)