with open("uncensored.txt", "r", encoding="utf-8") as uncLetter:
    uncLines = uncLetter.readlines()

cenLines = list()
i = 1

for line in uncLines:
    if ("kocham" in line.lower()) or (i % 3 == 0):
        cenLines.append("*****\n")
    else:
        cenLines.append(line)
    i += 1

with open("censored.txt", "w", encoding="utf-8") as cenLetter:
    cenLetter.writelines(cenLines)
