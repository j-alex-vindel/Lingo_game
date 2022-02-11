import requests
from bs4 import BeautifulSoup
import re
import random


vgm_url = 'https://www.wordgamehelper.com/4-letter-words'
html_text = requests.get(vgm_url).text
soup = BeautifulSoup(html_text, 'html.parser')

#### Get a dictionary of starting letter and words ####

def vocabulary():
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

#print('Starts with:',pick,'word is:',master[pick][random.choice(range(len(pick)))])

word = master[pick][random.choice(range(len(pick)))]
#message = 'Enter a word starting with'+' '+pick+':  '
#guess = input(message).upper()

#### Core of the game ####
n = 0
a1 = [0,0,0,0]
c  = [0,0,0,0]
a2 = [c[i] + a1[i] for i in range(4)]
c2 = [0,0,0,0]
while n < 5:
    message = 'Enter a word starting with'+' '+pick+':  '
    guess = input(message).upper()
    if len(guess) != 4:
        print('This is not a four letter word!')
        #print('The correct answer is','---',word)
        n = 6
    elif guess not in master[pick]:
        print('The word is not in the dictionary!')
        n = 6
    elif guess == word:
        print('CONGRATULATIONS!!!!')
        n = 6
    else:
        for i in range(len(word)):
            if word[i] == guess[i]:
                a1[i] = 1
                c2[i] = guess[i]
                for j in range(len(word)):
                    if guess[j] in word:
                        c[j] = 1
                        c2[j] = guess[j]
        n = n + 1
        print('Keep trying!!',' ','guess %d'%n)
        print(a2)
        print('***')
        print(c2)


else:
    print('The correct answer is','---',word)
