import re


# Checks if letter is a vowel
def is_vowel(letter):
    vowels = {"a", "e", "i", "o", "u"}
    if letter in vowels:
        return True
    else:
        return False


# Checks if letter at ith position of word is a consonant
# 'y' counts as a consonant if it's preceded by a vowel
def is_consonant(word, i):
    if is_vowel(word[i]):
        return False
    else:
        if word[i] == "y":
            if i-1 >= 0 and is_vowel(word[i-1]):
                return True
            else:
                return False
        else:
            return True


# Gets the number of vowel-consonant repetitions
def get_word_m(word):
    # Get the word form (C - consonant, V - vowel)
    form = ""
    for i in range(len(word)):
        if is_consonant(word, i):
            form += "C"
        else:
            form += "V"

    return form.count("VC")


# Checks if a word contains a vowel
def contains_vowel(word):
    for letter in word:
        if is_vowel(letter):
            return True
    return False


# Checks if the last chars of a word are repeating consonants
def is_double_consonant(word):
    if len(word) < 2:
        return False
    else:
        if is_consonant(word, -1) and word[-1] == word[-2]:
            return True
        else:
            return False


# Checks if words ends with consonant-vowel-consonant
def is_cvc(word):
    if len(word) < 3:
        return False
    else:
        if is_consonant(word, -3) and is_vowel(word[-2]) and is_consonant(word, -1) and re.search(r"[^wxy]$", word):
            return True
        else:
            return False


def step1a(word):
    if re.search(r"sses$", word):
        word = re.sub(r"sses$", "ss", word)
    elif re.search(r"ies$", word):
        word = re.sub(r"ies$", "i", word)
    elif re.search(r"sses$", word):
        word = re.sub(r"sses$", "ss", word)
    elif re.search(r"s$", word) and not re.search(r"ss$", word):
        word = re.sub(r"s$", "", word)
    return word


def step1b(word):
    if re.search(r"eed$", word):
        stem = re.sub(r"eed$", "", word)
        if get_word_m(stem) > 0:
            word = stem + "ee"
    elif re.search(r"ed$|ing$", word):
        stem = re.sub(r"ed$|ing$", "", word)
        if contains_vowel(stem):
            if re.search(r"at$|bl$|iz$", stem):
                word = stem + "e"
            elif is_double_consonant(stem) and re.search(r"[^lsz]$", stem):
                word = stem[:-1]
            elif get_word_m(stem) == 1 and is_cvc(stem):
                word = stem + "e"
            else:
                word = stem
    return word


def step1c(word):
    if re.search(r"y$", word):
        stem = re.sub(r"y$", "", word)
        if contains_vowel(stem):
            word = stem + "i"
    return word


def step1(word):
    word = step1a(word)
    word = step1b(word)
    word = step1c(word)
    return word


def step2(word):
    if re.search(r"ational$|ator$", word):
        stem = re.sub(r"ational$|ator$", "", word)
        if get_word_m(stem) > 0:
            word = stem + "ate"
    elif re.search(r"tional$", word):
        stem = re.sub(r"tional$", "", word)
        if get_word_m(stem) > 0:
            word = stem + "tion"
    elif re.search(r"enci$", word):
        stem = re.sub(r"enci$", "", word)
        if get_word_m(stem) > 0:
            word = stem + "ence"
    elif re.search(r"anci$", word):
        stem = re.sub(r"anci$", "", word)
        if get_word_m(stem) > 0:
            word = stem + "ance"
    elif re.search(r"izer$", word):
        stem = re.sub(r"izer$", "", word)
        if get_word_m(stem) > 0:
            word = stem + "ize"
    elif re.search(r"abli$", word):
        stem = re.sub(r"abli$", "", word)
        if get_word_m(stem) > 0:
            word = stem + "able"
    elif re.search(r"alli$", word):
        stem = re.sub(r"alli$", "", word)
        if get_word_m(stem) > 0:
            word = stem + "al"
    elif re.search(r"entli$", word):
        stem = re.sub(r"entli$", "", word)
        if get_word_m(stem) > 0:
            word = stem + "ent"
    elif re.search(r"eli$", word):
        stem = re.sub(r"eli$", "", word)
        if get_word_m(stem) > 0:
            word = stem + "e"
    elif re.search(r"ousli$|ousness$", word):
        stem = re.sub(r"ousli$|ousness$", "", word)
        if get_word_m(stem) > 0:
            word = stem + "ous"
    elif re.search(r"ization$", word):
        stem = re.sub(r"ization$", "", word)
        if get_word_m(stem) > 0:
            word = stem + "ize"
    elif re.search(r"ation$", word):
        stem = re.sub(r"ation$", "", word)
        if get_word_m(stem) > 0:
            word = stem + "ate"
    elif re.search(r"alism$|aliti$", word):
        stem = re.sub(r"alism$|aliti$", "", word)
        if get_word_m(stem) > 0:
            word = stem + "al"
    elif re.search(r"iveness$|iviti$", word):
        stem = re.sub(r"iveness$|iviti$", "", word)
        if get_word_m(stem) > 0:
            word = stem + "ive"
    elif re.search(r"fulness$", word):
        stem = re.sub(r"fulness$", "", word)
        if get_word_m(stem) > 0:
            word = stem + "ful"
    elif re.search(r"biliti$", word):
        stem = re.sub(r"biliti$", "", word)
        if get_word_m(stem) > 0:
            word = stem + "ble"
    return word


def step3(word):
    if re.search(r"icate$|iciti$|ical$", word):
        stem = re.sub(r"icate$|iciti$|ical$", "", word)
        if get_word_m(stem) > 0:
            word = stem + "ic"
    elif re.search(r"ative$|ful$|ness$", word):
        stem = re.sub(r"ative$|ful$|ness$", "", word)
        if get_word_m(stem) > 0:
            word = stem
    elif re.search(r"alize$", word):
        stem = re.sub(r"alize$", "", word)
        if get_word_m(stem) > 0:
            word = stem + "al"
    return word


def step4(word):
    regex = r"al$|ance$|ence$|er$|ic$|able$|ible$|ant$|" \
            r"ement$|ment$|ent$|ou$|ism$|ate$|iti$|ous$|ive$|ize$"
    if re.search(regex, word):
        stem = re.sub(regex, "", word)
        if get_word_m(stem) > 1:
            word = stem
    elif re.search(r"ion$", word):
        stem = re.sub(r"ion$", "", word)
        if get_word_m(stem) > 1 and (stem[-1] == "s" or stem[-1] == "t"):
            word = stem
    return word


def step5a(word):
    if re.search(r"e$", word):
        stem = re.sub(r"e$", "", word)
        if get_word_m(stem) > 1:
            word = stem
        elif get_word_m(stem) == 1 and not is_cvc(stem):
            word = stem
    return word


def step5b(word):
    if word[-1] == "l" and get_word_m(word) > 1 and is_double_consonant(word):
        word = word[:-1]
    return word


def step5(word):
    word = step5a(word)
    word = step5b(word)
    return word


def get_word_stem(word):
    word = step1(word)
    word = step2(word)
    word = step3(word)
    word = step4(word)
    word = step5(word)
    return word


while True:
    text = input("Word: ")
    print("Stem:", get_word_stem(text))
