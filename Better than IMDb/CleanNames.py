import json


ids = set()
with open("nameIds.txt") as file:
    for line in file:
        ids.add(line.rstrip("\n"))
# with open("actorIds.txt") as file:
#     for line in file:
#         ids.add(line.rstrip("\n"))


with open("names.json") as file:
    data = json.load(file)


out = dict()
out["names"] = []
i = 1
with open("namesShorter.json", "w") as outfile:
    for name in data["names"]:
        if name["nameId"] in ids:
            out["names"].append(name)
            i += 1
    json.dump(out, outfile, indent=4)
    print(i)
