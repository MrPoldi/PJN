


def merge(text: list, bigram):
    j = len(text) - 1
    i = 0
    while i < j:
        if text[i] + text[i+1] == bigram:
            text[i] += text[i+1]
            text.pop(i+1)
            j -= 1
        i += 1


def score(text):
    bigrams = set()
    freq = dict()

    for i in range(0, len(text) - 1):
        bigram = str(text[i] + text[i+1])
        if bigram in bigrams:
            freq[bigram] += 1
        else:
            bigrams.add(bigram)
            freq[bigram] = 1

    best = max(freq, key=freq.get)

    return freq, best


def prepare_corpus(corpus):
    corpus = corpus.replace(' ', '_')
    chars = list(corpus)
    chars.insert(0, "_")
    chars.insert(len(chars), "_")
    return chars


def bpe(corpus, vocab_size):
    chars = prepare_corpus(corpus)
    vocab = set(chars)

    i = 1
    while len(vocab) < vocab_size:
        print("Iteration no " + str(i))
        freq, best = score(chars)
        print(freq)
        vocab.add(best)
        merge(chars, best)
        print(vocab)
        i += 1

    freq, best = score(chars)

    return freq, vocab


# ----Main  program------ #
with open("bpe_input.txt", "r", encoding="utf-8") as file:
    corpus = file.read()

vocab_size = int(input("Desired size of vocabulary: "))
freq, vocab = bpe(corpus, vocab_size)
print("-------Results-------")
print("Bigram frequency:")
print(freq)
print("Vocabulary:")
print(vocab)
