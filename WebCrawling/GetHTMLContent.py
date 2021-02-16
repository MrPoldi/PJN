from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

website = 'europa'
lan = 'hr'
i = 1
max = 19
with open(website + '-'+lan+'.txt', 'r') as urls:
    with open(website + '-'+lan+'-content.txt', 'w', encoding='utf-8') as out:
        for url in urls:
            print(str(i) + ' / ' + str(max))
            i += 1
            hdr = {
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                'Accept-Encoding': 'none',
                'Connection': 'keep-alive'}
            req = Request(url=url, headers=hdr)
            try:
                with urlopen(req) as response:
                    html = response.read()
                    soup = BeautifulSoup(html, 'html.parser')
                    out.write(soup.get_text() + '\n')
                    #out.write(url + '\n')
                    #print(url)
            except:
                print("Error")
