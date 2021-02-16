import json


idList = set()
with open("intersectedIds.txt") as idFile:
    for line in idFile:
        idList.add(line.rstrip("\n"))


with open("crew.json") as crew_file:
    crew = json.load(crew_file)


print("Building dict")
nameDict = dict()
with open("namesShorter.json") as names_file:
    names = json.load(names_file)
    for name in names["names"]:
        nameDict[name["nameId"]] = name
print("Dict built")

result = dict()
result["crew"] = []
i = 1
for c in crew["crew"]:
    print(str(i) + " / 556606")
    i += 1
    if c["movieId"] in idList:
        directorIds = c["directorIds"].split(',')
        writerIds = c["writerIds"].split(',')
        director = nameDict.get(directorIds[0], None)
        writer = nameDict.get(writerIds[0], None)
        if director is not None and writer is not None:
            result["crew"].append({
                "movieId": c["movieId"],
                "dirName": director["name"],
                "dirBirth": director["birth"],
                "dirDeath": director["death"],
                "wrName": writer["name"],
                "wrBirth": writer["birth"],
                "wrDeath": writer["death"]
            })
        else:
            print("Data was None")

with open('Clean/cleanCrew.json', 'w') as outfile:
    json.dump(result, outfile, indent=4)
