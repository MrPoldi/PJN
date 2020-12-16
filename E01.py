words = set()
tokens = list()

with open("PoliMorf-0.6.7.tab", "r", encoding="utf-8") as file:
    for line in file:
        words.add(line.split("\t")[0].lower())


def max_match(string):
    if string == "":
        return
    else:
        i = 0
        j = len(string)
        for j in range(j, i, -1):
            word = string[i:j]
            remainder = string[j:len(string)]
            if word.lower() in words:
                tokens.append(word)
                return max_match(remainder)
        word = string[0]
        remainder = string[1:len(string)]
        tokens.append(word)
        return max_match(remainder)


while True:
    sen = input("Podaj zdanie do podzielenia: ")
    tokens = list()
    max_match(sen)
    print(tokens)
