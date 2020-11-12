import re

#Uznałem, że białe znaki zaliczają się jako dowolny ciąg znaków. Jeżeli miałyby się nie zaliczać to musiałby być taki regex
#validPattern = "^[^;\s]+[^;]*;[0-9]+;[0-9]+$"
validPattern = "^[^;]+;[0-9]+;[0-9]+$"

invalidLines = dict()
lineNum = 1

with open("toBeValidated.csv", "r", encoding="utf-8") as f:
    for line in f:
        if not re.match(validPattern, line):
            invalidLines[lineNum] = line
        lineNum += 1

if not invalidLines:
    print("Plik csv jest zapisany w poprawnym formacie")
else:
    print("Plik CSV jest zapisany niepoprawnie.\nNiepoprawne linie: ")
    for key in invalidLines:
        print(key, " : ", invalidLines[key])
