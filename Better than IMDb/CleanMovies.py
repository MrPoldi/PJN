import json


idList = set()
with open("intersectedIds.txt") as idFile:
    for line in idFile:
        idList.add(line.rstrip("\n"))


with open("movies.json") as file:
    movies = json.load(file)

result = dict()
result["movies"] = []
i = 1
for m in movies["movies"]:
    print(str(i) + " / 556612")
    i += 1
    if m["id"] in idList:
        result["movies"].append({
            "movieId": m["id"],
            "primaryTitle": m["primaryTitle"],
            "startYear": m["startYear"],
            "runtime": m["runtime"],
            "genres": m["genres"],
        })

with open('Clean/cleanMovies.json', 'w') as outfile:
    json.dump(result, outfile, indent=4)
