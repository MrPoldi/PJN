dictionary = {
    "kot": "cat",
    "pies": "dog",
    "ptak": "bird",
    "szynka": "ham",
    "słońce": "sun",
    "drewno": "wood",
    "stal": "steel",
    "gitara": "guitar",
    "szklanka": "glass",
    "drzwi": "door"
}

print("Podaj polskie słowo")
word = input()

translation = dictionary.get(word)

if translation is not None:
    print(word + " to po angielsku " + dictionary[word])
else:
    print("Nie znaleziono takiego słowa w słowniku")
