import re

capitalPattern = "^[A-ZŻŹĆĄŚĘŁÓŃ][a-zżźćńółęąś]+$"
phonePattern = "^\([0-9]{2}\) [0-9]{3}(-[0-9]{2}){2}$"
postPattern = "^[0-9]{2}-[0-9]{3}$"

flag = True
while flag:
    name = input("Imie: ")
    if re.match(capitalPattern, name):
        flag = False
    else:
        print("Błędny zapis")

flag = True
while flag:
    surname = input("Nazwisko: ")
    if re.match(capitalPattern, surname):
        flag = False
    else:
        print("Błędny zapis")

flag = True
while flag:
    phone = input("Telefon: ")
    if re.match(phonePattern, phone):
        flag = False
    else:
        print("Błędny zapis")

flag = True
while flag:
    postcode = input("Kod pocztowy: ")
    if re.match(postPattern, postcode):
        flag = False
    else:
        print("Błędny zapis")

flag = True
while flag:
    city = input("Miasto: ")
    if re.match(capitalPattern, city):
        flag = False
    else:
        print("Błędny zapis")