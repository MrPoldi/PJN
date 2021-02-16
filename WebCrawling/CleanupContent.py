from nltk.tokenize import sent_tokenize

website = 'europa'
lan = 'hr'

with open(website + '-'+lan+'-content.txt', 'r', encoding='utf-8') as file_in:
    with open(website + '-'+lan+'-content-clean.txt', 'w', encoding='utf-8') as file_out:
        for line in file_in:
            if line != '':
                sent_tokenize_list = sent_tokenize(line.strip())
                for sent in sent_tokenize_list:
                    file_out.write(sent + '\n')