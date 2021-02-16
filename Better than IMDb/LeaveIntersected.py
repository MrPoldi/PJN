import json


idList = set()
with open("intersectedIds.txt") as idFile:
    for line in idFile:
        idList.add(line.rstrip("\n"))


with open("cleanRatings.json") as ratings_file:
    data = json.load(ratings_file)

name = "ratings"

result = dict()
result[name] = []

for d in data[name]:
    if d["movieId"] in idList:
        result[name].append(d)

print(len(result[name]))

with open('cleanRatingsSmall.json', 'w') as outfile:
    json.dump(result, outfile, indent=4)
