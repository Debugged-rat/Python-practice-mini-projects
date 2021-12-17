#https://www.reddit.com/r/dailyprogrammer/comments/5go843/20161205_challenge_294_easy_rack_management_1/

import sys
from os import path

mixedLetters = list(input('Enter the mixed letters here: '))
targetWord = list(input('Enter the target word here: '))

targetWordCount = 0

while targetWordCount != len(targetWord):
    try:
        mixedLetters.remove(targetWord[targetWordCount])
        targetWordCount += 1
    except:
        try:
            mixedLetters.remove('?')
            mixedLetters.append(targetWord[targetWordCount])
        except:
            print(False)
            sys.exit()

print(True)
sys.exit()