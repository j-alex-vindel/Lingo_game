import requests
from bs4 import BeautifulSoup
import re
import random
import csv
import pandas as pd

def vocabulary(): ## gets the words from the web 4 letter list
    vgm_url = 'https://www.wordgamehelper.com/4-letter-words'
    html_text = requests.get(vgm_url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    words = []
    cap = []
    for i in soup.find_all('a'):
        word = i.string
        if len(word) <= 4:
            words.append(word.upper())
            if word.upper()[0] not in cap:
                cap.append(word.upper()[0])

    master = {m : [] for m in cap}

    for letter in cap:
        for word in words:
            if re.match(letter,word[0]):
                master[letter].append(word)

    return master, cap

master, cap = vocabulary()

pick = random.choice(cap)


wp1 = pd.read_csv('words_played.csv',header=None)[0].tolist()

print(wp1)

for i in range(4):
    wp1 = pd.read_csv('words_played.csv',header=None)[0].tolist()
    word = master[pick][random.choice(range(len(pick)))]
    word2 = master[pick][random.choice(range(len(pick)))]
    wp = [[word]]
    if word not in wp1:
    # opening the csv file in 'a+' mode
        file = open('words_played.csv', 'a+', newline ='')
    # writing the data into the file
        with file:
            write = csv.writer(file)
            write.writerows(wp)
print(wp1)
print(word)
print(word2)
