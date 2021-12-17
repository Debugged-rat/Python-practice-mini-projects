# Link for question: https://www.reddit.com/r/dailyprogrammer/comments/ffxabb/20200309_challenge_383_easy_necklace_matching/
import sys
from os import path

necklace1 = input('Insert necklace 1 letters here: ')
necklace2 = input('Insert necklace 2 letters here: ')

necklaceLetters1 = list(necklace1)
necklaceLetters2 = list(necklace2)

length_of_necklace1 = len(necklace1)

emptyString = ""

repeatedTimes = 0

for i in range(length_of_necklace1):
    necklaceLetters1.append(necklaceLetters1[0])
    necklaceLetters1.remove(necklaceLetters1[0])
    joined_necklaceLetters1 = emptyString.join(necklaceLetters1)
    if joined_necklaceLetters1 == necklace2:
        repeatedTimes += 1

if repeatedTimes > 0:
    print('True')
    print('Repeated Times: ' + str(repeatedTimes))
else:
        print('False')
sys.exit()