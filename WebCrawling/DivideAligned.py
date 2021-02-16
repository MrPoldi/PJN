website = 'europa'

with open(website + '-align.txt', 'r', encoding='utf-8') as file_full:
    with open(website + '-align-en.txt', 'w', encoding='utf-8') as file_en:
        with open(website + '-align-hr.txt', 'w', encoding='utf-8') as file_hr:
            for line in file_full:
                data = line.split('\t')
                if len(data) > 2 and data[0] != '' and data[1] != '':
                    file_en.write(data[0] + '\n')
                    file_hr.write(data[1] + '\n')

# hunalign.exe -text -utf -realign tmp.dict en.txt hr.txt > eceuropa-align.txt
