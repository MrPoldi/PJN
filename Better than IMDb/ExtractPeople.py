import json
import csv


data = dict()
data['names'] = []

nameIds = set()

print("Reading data...")

with open("nameIds.txt", 'r') as infile:
    for nameId in infile:
        nameIds.add(nameId.rstrip('\n'))

with open("actorIds.txt", 'r') as infile:
    for nameId in infile:
        nameIds.add(nameId.rstrip('\n'))

with open('names.tsv', 'r', encoding='utf-8') as infile:
    read_tsv = csv.reader(infile, delimiter='\t')
    for row in read_tsv:
        if row[0] in nameIds:
            data['names'].append({
                'nameId': row[0],
                'name': row[1],
                'birth': row[2],
                'death': row[3]
            })
print("Data successfully read!")
print("Number of people: " + str(len(data['names'])))
print("Writing data to JSON file...")
with open('names.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)

print("Data successfully written!")

# 1003166
