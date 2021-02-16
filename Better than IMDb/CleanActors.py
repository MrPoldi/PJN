import json


def get_name_data(name_id):
    for name in names["names"]:
        if name["nameId"] == name_id:
            return name
    return None


idList = set()
with open("intersectedIds.txt") as idFile:
    for line in idFile:
        idList.add(line.rstrip("\n"))


with open("actors.json") as actors_file:
    actors = json.load(actors_file)


print("Building dict")
nameDict = dict()
with open("namesShorter.json") as names_file:
    names = json.load(names_file)
    for name in names["names"]:
        nameDict[name["nameId"]] = name
print("Dict built")

result = dict()
result["actors"] = []
i = 1
for actor in actors["actors"]:
    print(str(i) + " / 1876463")
    i += 1
    if actor["movieId"] in idList:
        data = nameDict.get(actor["nameId"], None)
        if data is not None:
            result["actors"].append({
                "movieId": actor["movieId"],
                "name": data["name"],
                "birth": data["birth"],
                "death": data["death"]
            })
        else:
            print("Data was None for: " + actor['nameId'])

with open('Clean/cleanActors.json', 'w') as outfile:
    json.dump(result, outfile, indent=4)
