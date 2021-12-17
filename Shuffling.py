#https://www.reddit.com/r/dailyprogrammer/comments/3e0hmh/20150720_challenge_224_easy_shuffling_a_list/

import random

userInput = input('Enter the list here: ')
separator = input('What will be separating each of the elements? If left blank a space will be the separator by default. ')
if separator == '':
    separator = ' '
userInput = userInput.split(separator)
inputLength = []
inputLength.append(len(userInput))
shuffleList = []
while inputLength[0] != len(shuffleList):
    shuffleList.append(random.choice(userInput))
    userInput.remove(shuffleList[-1])
print(', '.join(shuffleList))