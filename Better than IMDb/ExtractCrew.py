import json
import csv


data = dict()
data['crew'] = []

movieIds = set()

print("Reading data...")

with open("movieIds.txt", 'r') as infile:
    for movieId in infile:
        movieIds.add(movieId.rstrip('\n'))

with open('crew.tsv', 'r', encoding='utf-8') as infile:
    read_tsv = csv.reader(infile, delimiter='\t')
    for row in read_tsv:
        if row[0] in movieIds:
            data['crew'].append({
                'movieId': row[0],
                'directorIds': row[1],
                'writerIds': row[2]
            })
print("Data successfully read!")
print("Number of movies: " + str(len(data['crew'])))
print("Writing data to JSON file...")
with open('crew.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)

with open('nameIds.txt', 'w') as outfile:
    names = set()

    for crew in data['crew']:
        names.update(crew['directorIds'].split(','))
        names.update(crew['writerIds'].split(','))

    for name in names:
        outfile.write(name + '\n')

print("Data successfully written!")

# 556606
