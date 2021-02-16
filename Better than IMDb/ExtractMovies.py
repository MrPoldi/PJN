import json
import csv


data = dict()
data['movies'] = []

print("Reading data...")

with open('movies.tsv', 'r', encoding='utf-8') as infile:
    read_tsv = csv.reader(infile, delimiter='\t')
    for row in read_tsv:
        if row[1] == "movie" and row[4] == '0':
            data['movies'].append({
                'id': row[0],
                'type': row[1],
                'primaryTitle': row[2],
                'originalTitle': row[3],
                'isAdult': row[4],
                'startYear': row[5],
                'endYear': row[6],
                'runtime': row[7],
                'genres': row[8],
            })
print("Data successfully read!")
print("Number of movies: " + str(len(data['movies'])))
print("Writing data to JSON file...")

with open('movies.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)

with open('movieIds.txt', 'w') as outfile:
    for movie in data['movies']:
        outfile.write(movie['id'] + '\n')

print("Data successfully written!")

# 556612
