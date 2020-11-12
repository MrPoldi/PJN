import re


emailRegex = "[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}"

emails = list()

with open("website.html", "r", encoding="utf-8") as file:
    for line in file:
        temp = re.findall(emailRegex, line, flags=re.I)
        if len(temp) != 0:
            s = set(temp)   #Remove duplicates
            temp = list(s)
            emails.extend(temp)

print(emails)
