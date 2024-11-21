import csv
import json
from datetime import datetime
from pprint import pprint


einstein_csv = 'Albert,Einstein,1879-03-14,1955-04-18,Germany,"for his services to Theoretical Physics, and especially for his discovery of the law of the photoelectric effect",physics,1921'
einstein = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}


einstein_json = json.dumps(einstein)
back_to_dict = json.loads(einstein_json)
pprint(einstein_json)
print('===================')
pprint(back_to_dict)
print('===================')

# use with - it keeps file open only for the codeblock then closes it

with open('laureates.csv', 'r') as l_file:
    reader = csv.DictReader(l_file)
    laureates = list(reader)

#creating json file from the csv file
with open('laureates.json', 'w') as f:
    reader = csv.DictReader(f)
    json.dump (laureates, f, indent=2)

for laureate in laureates:
    if laureate['surname'] == 'Einstein':
        pprint(laureate)
        print('=============')
        year_date = datetime.strptime(laureate['year'], '%Y')
        #the %Y-%m-%d was written since the csv is like that
        born_date = datetime.strptime(laureate['born'], '%Y-%m-%d')
        #we took only the year from datetime
        print('nobel age',  year_date.year - born_date.year)
        break
