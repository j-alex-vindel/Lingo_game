import requests
from bs4 import BeautifulSoup
import re
import random


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

word = master[pick][random.choice(range(len(pick)))]
#message = 'Enter a word starting with'+' '+pick+':  '
#guess = input(message).upper()

#### Core of the game ####
n = 0
while n < 5:
    message = 'Enter a word starting with'+' '+pick+':  '
    guess = input(message).upper()
    print('Guess %d'%(n+1))
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
        a1 = [0,0,0,0]
        c  = [0,0,0,0]
        c2 = [0,0,0,0] # populates with letters
        c3 = [0,0,0,0]
        for i in range(len(word)):
            a2 = [c[i] + a1[i] for i in range(4)]
            #c3 = [0,0,0,0]
            if word[i] == guess[i]:
                a1[i] = 1
                c2[i] = guess[i]
                a2 = [c[i] + a1[i] for i in range(4)]
                for j in range(len(word)):
                    if guess[j] in word:
                        c[j] = 1
                        c2[j] = guess[j]
                    a2 = [c[j] + a1[j] for j in range(4)]
                    for s in range(4):
                        if a2[s] >= 2:
                            c3[s] = c2[s]
                        elif a2[s] == 1:
                            c3[s] = 'o'
                        elif a2[s] == 0:
                            c3[s] = '-'
        n = n + 1
        #print(a1,'-','this is the first vector of answers')
        #print('***')
        #print(c,'-', 'this is the first vector of clues')
        #print('***')
        #print(a2,'-','this is a1 + c')
        #print('***')
        #print(c2,'-','This is the first list with letters')
        print([letter.upper() for letter in guess])
        print('*** CLUE ***')
        print(c3)
        print('Keep trying!!')


else:
    print('The correct answer is','---',word)
