import json
import csv


data = dict()
data['ratings'] = []

movieIds = set()

print("Reading data...")

with open("movieIds.txt", 'r') as infile:
    for movieId in infile:
        movieIds.add(movieId.rstrip('\n'))

with open('ratings.tsv', 'r', encoding='utf-8') as infile:
    read_tsv = csv.reader(infile, delimiter='\t')
    for row in read_tsv:
        if row[0] in movieIds:
            data['ratings'].append({
                'movieId': row[0],
                'rating': row[1],
                'numVotes': row[2]
            })
print("Data successfully read!")
print("Number of movies: " + str(len(data['ratings'])))
print("Writing data to JSON file...")

with open('ratings.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)

print("Data successfully written!")


# 254553
