import json


# movieIds = set()
# with open("movieIds.txt") as file:
#     for line in file:
#         movieIds.add(line.rstrip("\n"))

ratingIds = set()
with open("Clean/cleanRatings.json") as file:
    ratings = json.load(file)
    for rating in ratings["ratings"]:
        ratingIds.add(rating["movieId"].rstrip("\n"))

crewIds = set()
with open("Clean/cleanCrew.json") as file:
    crew = json.load(file)
    for c in crew["crew"]:
        crewIds.add(c["movieId"].rstrip("\n"))

actorIds = set()
with open("Clean/cleanActors.json") as file:
    actors = json.load(file)
    for actor in actors["actors"]:
        actorIds.add(actor["movieId"].rstrip("\n"))


ids = ratingIds & crewIds & actorIds

ids = list(ids)
ids.sort()

with open("Clean/intersectedIds.txt", "w") as file:
    for i in ids:
        file.write(i + "\n")


