import json
import csv


data = dict()
data['actors'] = []

movieIds = set()

print("Reading data...")

with open("movieIds.txt", 'r') as infile:
    for movieId in infile:
        movieIds.add(movieId.rstrip('\n'))

with open('principals.tsv', 'r', encoding='utf-8') as infile:
    read_tsv = csv.reader(infile, delimiter='\t')
    for row in read_tsv:
        if row[0] in movieIds and (row[3] == 'actor' or row[3] == 'actress' or row[3] == 'self'):
            data['actors'].append({
                'movieId': row[0],
                'nameId': row[2],
                'category': row[3],
                'job': row[4],
                'characters': row[5]
            })
print("Data successfully read!")
print("Number of movie-actor pairs: " + str(len(data['actors'])))
print("Writing data to JSON file...")
with open('actors.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)

with open('actorIds.txt', 'w') as outfile:
    names = set()

    for crew in data['actors']:
        names.update(crew['nameId'].split(','))

    for name in names:
        outfile.write(name + '\n')

print("Data successfully written!")

# 1876463
