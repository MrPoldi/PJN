import json


idList = set()
with open("intersectedIds.txt") as idFile:
    for line in idFile:
        idList.add(line.rstrip("\n"))


with open("ratings.json") as ratings_file:
    ratings = json.load(ratings_file)


# print("Building dict")
# nameDict = dict()
# with open("namesShorter.json") as names_file:
#     names = json.load(names_file)
#     for name in names["names"]:
#         nameDict[name["nameId"]] = name
# print("Dict built")

result = dict()
result["ratings"] = []
i = 1
for r in ratings["ratings"]:
    print(str(i) + " / 254553")
    i += 1
    if r["movieId"] in idList:
        result["ratings"].append(r)


with open('Clean/cleanRatings.json', 'w') as outfile:
    json.dump(result, outfile, indent=4)
