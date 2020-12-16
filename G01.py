# pip install spacy
# py -m spacy download pl_core_news_lg
import spacy


def is_imperative(word):
    if word and word.tag_ == "IMPT":
        return True
    else:
        return False


def get_verb(doc):
    for word in doc:
        if word.pos_ == "VERB":
            return word
        else:
            return None


def tokenize_sentence(doc):
    tokens = []
    for word in doc:
        tokens.append(word)
    return tokens


def get_pos_tag(tokens):
    pos_tags = dict()
    for token in tokens:
        pos_tags[token.text] = token.pos_
    return pos_tags


def get_deps(tokens):
    deps = dict()
    for token in tokens:
        deps[token.text] = token.dep_
    return deps


def get_obj(tokens):
    for token in tokens:
        if token.pos_ == "NOUN" and token.dep_ == "obj":
            return token
        elif token.pos_ == "PRON" and token.dep_ == "obj":
            return token
        elif token.pos_ == "PART" and token.dep_ == "expl:pv":
            return token
        elif token.pos_ == "NOUN" and token.dep_ == "nsubj":
            return token
        elif token.pos_ == "NOUN" and token.dep_ == "ROOT":
            return token
    return None


def get_mods(tokens):
    mods = list()
    for token in tokens:
        if (token.dep_ == "nmod" or token.dep_ == "amod" or token.dep_ == "det") and token.pos_ != "VERB":
            mods.append(token)
            conjs = token.conjuncts
            for conj in conjs:
                mods.append(conj)

    return mods


def build_obj_string(obj, mods):
    string = ""
    mods_copy = mods.copy()

    for mod in mods:
        if mod.i < obj.i:
            if mod.i > 0 and mod.nbor(-1).pos_ == "ADP":
                string += mod.nbor(-1).text + " "
            string += mod.text + " "
            mods_copy.pop(mods_copy.index(mod))

    string += obj.text

    for mod in mods_copy:
        if mod.i > 0 and mod.nbor(-1).pos_ == "ADP":
            string += " " + mod.nbor(-1).text
        string += " " + mod.text

    return string


def print_more_info(tokens):
    deps = get_deps(tokens)
    print("Zależności:", deps)
    obj = get_obj(tokens)
    print("Obiekt bez modyfikatorów:", obj)
    mods = get_mods(tokens)
    print("Modyfikatory:", mods)


def main():
    sentence = input("Podaj zdanie: ")
    doc = nlp(sentence)
    tokens = tokenize_sentence(doc)
    print("Tokeny:", tokens)
    pos_tags = get_pos_tag(tokens)
    print("Części mowy:", pos_tags)
    verb = get_verb(doc)
    if is_imperative(verb):
        print("Akcja:", verb)
        obj = get_obj(tokens)
        mods = get_mods(tokens)
        print("Obiekt:", build_obj_string(obj, mods))
    else:
        print("To nie był rozkaz")

    # print_more_info(tokens)


print("Wczytywanie modelu...")
nlp = spacy.load("pl_core_news_lg")
print("Wczytano")
while True:
    main()
