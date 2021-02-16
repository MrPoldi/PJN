import json
from collections import defaultdict


idSet = set()
with open("intersectedIds.txt") as file:
    for line in file:
        idSet.add(line.rstrip("\n"))


# movie:
#   primaryTitle //string
#   startYear //int
#   runtime //int minutes
#   genres //array

# actors:
#   nameId -> select actor data from names.json
#   name //string "<name> <surname>"
#   birth //int year
#   death? //int year
#   isDead? //bool


# ratings:
#   rating  //float
#   numVotes //int

# crew:
#   directorIds -> names.json //array
#   writerIds -> names.json  //array
#   name //string "<name> <surname>"
#   birth //int year
#   death? //int year
#   isDead? //bool
# Select only one of each?

# Calculated
#   avgActorAge
#   directorAge
#   writerAge

with open("Clean/CleanMoviesSmall.json") as file:
    movies = json.load(file)
    movies = movies["movies"]

with open("Clean/cleanRatingsSmall.json") as file:
    ratings = json.load(file)
    ratings = ratings["ratings"]

with open("Clean/cleanCrewSmall.json") as file:
    crew = json.load(file)
    crew = crew["crew"]

with open("Clean/cleanActorsSmall.json") as file:
    actors = json.load(file)
    actors = actors["actors"]

actorDict = defaultdict(list)
for actor in actors:
    actorDict[actor["movieId"]].append(actor)


print(len(movies))
print(len(ratings))
print(len(crew))
print(len(actorDict))


with open("Training/trainingData10.txt", "w", encoding="utf-8") as file:
    for i in range(len(movies)):
        movieString = movies[i]["primaryTitle"] + " " + movies[i]["startYear"] + " " \
                      + movies[i]["runtime"] + " " + movies[i]["genres"]

        crewString = crew[i]["dirName"].replace(" ", "") + " " + crew[i]["wrName"].replace(" ", "")

        try:
            dirAge = str(int(movies[i]["startYear"]) - int(crew[i]["dirBirth"]))
        except:
            dirAge = "\\N"
        try:
            wrAge = str(int(movies[i]["startYear"]) - int(crew[i]["wrBirth"]))
        except:
            wrAge = "\\N"

        isDirDead = ""
        if crew[i]["dirDeath"] != "\\N":
            isDirDead = "1"
        else:
            isDirDead = "0"

        actorString = ""

        actAge = 0
        a = 0
        for actor in actorDict[movies[i]["movieId"]]:
            actorString += actor["name"].replace(" ", "") + " "
            try:
                actAge += int(movies[i]["startYear"]) - int(actor["birth"])
            except:
                a += 1
        actorString.rstrip(" ")
        try:
            actAge = str(int(actAge / (len(actorDict[movies[i]["movieId"]]) - a)))
        except:
            actAge = "\\N"

        agesString = dirAge + " " + wrAge + " " + actAge

        line = ratings[i]["rating"] + " | " + movieString + " " + crewString + " " + agesString +\
               " " + isDirDead + " " + actorString
        line = line.replace(":", "")

        if int(ratings[i]["numVotes"]) > 500 and ("\\N" not in line):
            file.write(line + "\n")

