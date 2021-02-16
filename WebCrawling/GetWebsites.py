import json
import re

website = 'europa'
lan = 'hr'

with open(website+'-'+lan+'.json', 'r') as json_file:
    with open(website + '-en.txt', 'a') as out_file_en:
        with open(website + '-'+lan+'.txt', 'a') as out_file_hr:
            for line in json_file:
                data = json.loads(line)
                url = data['url']
            # url_en = url.replace('/uk', '/hr')
                if url.endswith("_hr"):
                    out_file_hr.write(url + '\n')
                    url_en = re.sub(r'_hr$', '_en', url)
                    out_file_en.write(url_en + '\n')
