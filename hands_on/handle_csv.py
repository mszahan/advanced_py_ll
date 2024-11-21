import csv
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


# use with - it keeps file open only for the codeblock then closes it

with open('laureates.csv', 'r') as l_file:
    reader = csv.DictReader(l_file)
    laureates = list(reader)

for laureate in laureates:
    if laureate['surname'] == 'Einstein':
        pprint(laureate)
        break
