import re

regexes = [
    "\\b(po|wy|za|do|roz|prze)*rucha\S*",
    "\\b(wy|prze|do|za|pod|w|s|roz|od)*kurw\S*",
    "\\b(po|wy|za|prze|do|u|w|z|roz|od|o|na)*jeb\S*",
    "\\b(o)*cip\S*",
    "\\b(o|wy)*chuj\S*", #podsłuchuj
    "\\bkutas\S*",
    "\\b(w)*pizd\S*",
    "\\b(po|wy|za|prze|do|u|w|s|roz|od|pod|na|przy)*pierd(o|a)\S*",
    "\\bsuk(a|ą|ę|i|ami|om)*",
    "\\bsuce"
    "\\bsukin\S*"
    "\\bfiut\S*"
]
regexCombined = "(" + ")|(".join(regexes) + ")"

replace = "---"

with open("bluzgi.txt", "r", encoding="utf-8") as fRead:
    with open("unbluzged.txt", "w", encoding="utf-8") as fWrite:
        for line in fRead:
            fWrite.write(re.sub(regexCombined, replace, line, flags=re.I))
