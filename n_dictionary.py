import requests
from bs4 import BeautifulSoup
import re
import json


vgm_url = 'https://www.dictionary.com/e/word-finder/4-letter-words/'
html_text = requests.get(vgm_url).text
soup = BeautifulSoup(html_text, 'html.parser')

dt = soup.find_all(re.compile('script'))[8]

text = dt.contents[0]
json_text = '{%s}' % (text.partition('{')[2].rpartition('}')[0],)
value = json.loads(json_text)

D = []
cap = []

for li in value['widgets'].keys():
    D = D + value['widgets'][li]['words']['1']
for words in D:
    if words[0] not in cap:
        cap.append(words[0])

master = {c : [] for c in cap}

for letter in cap:
    for word in D:
        if re.match(letter,word[0]):
            master[letter].append(word)
